import sys
import os
import json
import socket
import threading
import time


class Server(object):
    def __init__(self, radio_command=None):
        # 获取本地ip(服务器ip)
        self.rush_ip()
        self.server_runState = False
        # 本次聊天的缓存
        self.msg_file = get_json_file()
        self.msg_data = []  # 缓存内容(消息列表)
        # 用户列表
        self.users = {}  # 服务端的用户socket等
        self.user_list = {}  # 字典：用户名:禁言时间
        # 接收用户消息的线程列表
        self.receive_thread = []
        # 发送时的回调函数
        self.radio_command = radio_command

    def rush_ip(self):
        # 重新获取电脑ip
        hostname = socket.gethostname()
        self.server_ip = socket.gethostbyname(hostname)

    def start(self, ip=None, port=3800):
        # 启动服务器
        if ip is None:
            ip = self.server_ip
        self.users.clear()  # 清空用户列表
        self.receive_thread.clear()  # 清空线程列表
        # socket嵌套字TCP的ipv4和相关协议
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定ip和端口号
        try:
            self.server.bind((ip, port))
        except:
            print('启动ip和端口失败')
            return 'fail to start ip_port'
        # 设置监听和连接的最大的数量
        self.server.listen(10)
        # 开启服务器等待连接线程
        threading.Thread(target=self.connect).start()
        # 更新变量,代表服务器在运行
        self.server_runState = True

    def close(self):
        self.server_runState = False
        self.server.close()  # 关闭服务器socket
        self.users.clear()  # 清空用户列表
        self.send_users()  # 在没有用户的情况下，只会调用self.command，即刷新Ui界面

    def connect(self, server=None):
        # 等待用户连接
        if not server:
            server = self.server
        # 服务器要一直运行所以使用死循环
        while True:
            # 接受所连接的客户端的信息
            try:
                connect, addrss = server.accept()
            except OSError:
                break  # 服务器关闭
            # 每连接一个客户端就开启一个线程
            t = threading.Thread(target=self.member_receive, args=(connect, addrss))
            t.start()
            self.receive_thread.append(t)

    def member_receive(self, connect, addrss):
        # 接收客户端登陆的信息
        try:
            userName = connect.recv(1024).decode("utf-8")
        except:
            try:
                sendStr = json.dumps(dict(sender='system', text='连接失败', type='msg', receive=''))
                connect.send(sendStr.encode())
            except:
                pass
            return
        # 解码并储存用户的信息
        self.users[userName] = {'socket': connect, 'forbidden': 0}
        # 向当前登录的客户端反馈登录信息
        # self.radio_msg(self.msg(f"{userName}上线"))
        # 向所有在线的客户端反馈新的好友登录信息并提供在线用户列表
        self.send_users()
        # 接受客户端发送的信息
        while self.server_runState:  # 服务器开启时循环
            try:
                rData = connect.recv(1024)
            except Exception as error:
                print(error)
                self.member_exit(userName)
                break
            if not rData:
                self.member_exit(userName)
                break
            rMSG = json.loads(rData.decode("utf-8"))  # 解码信息，将二进制转换为Json字符
            send = self.radio_msg(rMSG)
            if send is True:  # 将接收到的消息转发
                pass  # 转发成功
            elif send == 'no user':
                self.radio_msg(self.msg(f'发送失败，用户->{rMSG["receive"]}<-不存在', receive=rMSG["sender"]))
            elif send == 'sender forbidden':
                self.radio_msg(self.msg(f'发送失败，你已被禁言', receive=rMSG["sender"]))
            elif send == 'format mismatch':
                self.radio_msg(self.msg('发送失败，error format mismatch', receive=rMSG["sender"]))
            elif send == 'fail to send':
                pass

    def msg(self, text, sender='system', receive=''):
        return {'sender': sender, 'receive': receive, 'text': text}

    def send_users(self):
        # 向所有在线的客户端反馈新的好友登录信息并提供在线用户列表
        users_name = list(self.users.keys())  # 所有用户名
        users_time = [user['forbidden'] for user in self.users.values()]  # 所有用户禁言时间
        self.user_list = dict(zip(users_name, users_time))  # 生成字典：用户名:禁言时间
        send = self.radio_msg(self.msg(self.user_list), type='users')
        print(f'当前用户列表: {self.user_list}')

    def radio_msg(self, msg, type='msg', command=None):
        """msg:{'sender':username or 'system', 'type':'msg' or 'users' or 'exit' or 'kill', 'close', receive:'' or username,
        'text':text} """
        # 用json格式存储和传输，并定义每个信息的类型
        if type == 'exit':
            self.member_exit(msg['sender'])
        elif type == 'kill':
            if not msg['text']:  # 如果发送时没有内容即为函数调用,则踢群
                # 提示被踢成员
                self.radio_msg(self.msg('您被提出局聊', receive=msg["receive"]), 'kill')
                del self.users[msg["receive"]]  # 删掉该用户信息
                self.radio_msg(self.msg(f'{msg["receive"]}被踢出局聊'), 'msg')
                self.send_users()
                return True
        elif type == 'close':
            self.radio_msg(self.msg('服务器关闭'), 'close')
        if type:
            msg['type'] = type
        if type != 'users' and not ('sender' in msg and 'receive' in msg and msg['text']):  # 内容不符合格式
            print(f'format mismatch {msg}')
            return 'format mismatch'
        if msg['sender'] != 'system' and self.users[msg['sender']]['forbidden'] != 0:
            self.send_users()
            return 'sender forbidden'
        # 通过客户端要发送的信息中是否指定要发送到的用户，如果没有选择要发送的用户，则默认为群发消息
        receive = msg['receive']
        # print(f'system, {msg}')
        if receive == '':
            for key in list(self.users.keys()):
                user_socket = self.users[key]['socket']
                send_data = json.dumps(msg).encode()
                try:
                    user_socket.send(send_data)
                except:
                    return 'fail to send'
        elif receive in self.users:  # 检测私发的用户名是否在用户列表内
            user_socket = self.users[receive]['socket']
            send_data = json.dumps(msg).encode()
            try:
                user_socket.send(send_data)
            except:
                return 'fail to send'
        else:
            print('no user_socket')
            return 'no user_socket'
        if type != 'users' and type != 'exit' and type != 'kill':
            # 将记录缓存到本地文件
            self.msg_data.append(msg)
            with open(self.msg_file, 'w+', encoding='utf-8') as f:
                json.dump(self.msg_data, f, sort_keys=True)
            if len(self.msg_data) >= 119:
                self.msg_data.clear()
                self.msg_file = get_json_file()
        # 调用回调函数
        if command:
            command(msg)
        elif self.radio_command:
            self.radio_command(msg)
        return True

    def member_exit(self, user_name):
        del self.users[user_name]  # 删掉该用户信息
        # 向所有在线的客户端反馈新的好友登录信息并提供在线用户列表
        self.radio_msg(self.msg(f'{user_name}下线'))
        self.send_users()

    def kill_member(self, user_name):
        # 判断用户是否存在
        if user_name not in self.users.keys():
            print(f'no user {user_name}, users: {list(self.users.keys())}')
            return f'no user {user_name}'
        # 调用踢人广播
        self.radio_msg(self.msg('', receive=user_name), type='kill')

    def forbidden(self, user_name, time_stamp):
        if user_name not in list(self.users.keys()):
            return 'no user'
        self.users[user_name]['forbidden'] = time_stamp
        self.send_users()

    def break_forbidden(self, user_name):
        if user_name not in list(self.users.keys()):
            return 'no user'
        self.users[user_name]['forbidden'] = 0
        self.send_users()


class Client:
    def __init__(self, receive_command=None):
        hostname = socket.gethostname()  # 获取本地计算机名
        self.user_name = hostname  # 初始的用户名称为计算机名
        self.msg_data = []  # 缓存内容(消息列表)
        self.client_runState = False  # 连接情况, True为已连接
        self.user_list = {}  # 字典：用户名:禁言时间
        # 消息接收的回调函数
        self.receive_command = receive_command

    def start(self, server_ip, port, user_name=None):
        if not user_name:
            user_name = self.user_name
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socked所准守ipv4相关协议4
        try:
            self.client.connect((server_ip, port))  # 连接服务器
            print(f'连接 ip:{server_ip} port: {port}')
        except:
            print(f'连接失败 ip:{server_ip} port: {port}')
            return 'fail to connect'
        self.client.send(user_name.encode("utf-8"))  # 将自己的登录名发送给服务器，函数会附带自己的IP信息
        threading.Thread(target=self.receive).start()

    def receive(self):
        self.client_runState = True
        while True:
            try:
                data = self.client.recv(1024)  # 用于接受服务其发送的信息
            except:  # 可能服务器停止
                if self.receive_command:
                    self.receive_command({'sender': 'system', 'receive': '', 'type': 'close', 'text':''})
                break
            # 接收消息时同步获取系统时间并显示在消息显示框上
            msg = json.loads(data.decode('utf-8'))
            # print(f'user, {msg}')
            if msg['type'] == 'msg':  # 判断类型
                if msg["sender"] == 'system':
                    if not msg['receive']:
                        print(f'系统消息: {msg["text"]}')
                else:
                    if not msg['receive']:
                        print(f'{msg["sender"]}: {msg["text"]}')
                    else:
                        print(f'{msg["sender"]} 对你说: {msg["text"]}')
            elif msg["type"] == 'users':
                self.user_list = msg["text"]
                print(f'当前用户列表: {self.user_list}')
            elif msg["type"] == 'kill':
                print(f'系统消息: {msg["text"]}')  # 被踢
                break
            elif msg['type'] == 'close':
                print(f'系统消息: {msg["text"]}')  # 服务器关闭
                break
            if self.receive_command:
                self.receive_command(msg)
        self.client_runState = False

    def break_client(self):
        self.send('', type='exit')

    def msg(self, text, receive=''):
        return {'sender': self.user_name, 'receive': receive, 'text': text}

    def send(self, text, receive='', type='msg'):
        msg = self.msg(text, receive)
        msg['type'] = type
        send_data = json.dumps(msg).encode()
        try:
            self.client.send(send_data)
        except:
            return False


def get_json_file():
    # 读取本地缓存的文件列表并排序
    msg_file_list = os.listdir('./msg_data')
    msg_file_list.sort()
    msg_index = int(msg_file_list[-1][3:-5])  # 找到列表末项并切片出数字，获取最新文件索引
    msg_file = f'./msg_data/msg{msg_index}.json'  # 最新文件路径
    return msg_file


def json_test():
    # https://blog.csdn.net/whjkm/article/details/81159888
    # data = [{'data': "data"}]
    # msg_data_file = open('./msg_data/msg1.json', 'w+', encoding='utf-8')
    # json.dump(data, msg_data_file, indent='', sort_keys=True)  # indent为缩进
    msg_data_file = open('./msg_data/msg1.json', 'r', encoding='utf-8')
    msg_data = json.load(msg_data_file)
    msg_data_file.close()
    print(len(msg_data), msg_data)


if __name__ == '__main__':
    client = Client()
    client2 = Client()
    server = Server()
    server.start()
    print('server ip: ', server.server_ip)
    client.start(server_ip=server.server_ip, port=3800, user_name='1')
    client2.start(server_ip=server.server_ip, port=3800, user_name='2')
    client.send('163')
    time.sleep(1)
    server.kill_member('1')
    time.sleep(1)
    server.close()
    # json_test()
