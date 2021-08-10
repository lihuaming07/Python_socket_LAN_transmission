# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/qq_42620328/article/details/108256970?ops_request_misc=&request_id=&biz_id=102&utm_term=python%20socket%E9%80%9A%E4%BF%A1%E5%B8%A6%E7%95%8C%E9%9D%A2&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-6-108256970.first_rank_v2_pc_rank_v29&spm=1018.2226.3001.4187
"""

import tkinter
import socket, threading

win = tkinter.Tk()  # 创建主窗口
win.title('服务器')
win.geometry("400x300+200+20")
users = {}  # 用户字典，也可以连接数据库


def run(connect, addrss):
    # 接收客户端登陆的信息
    userName = connect.recv(1024)
    # 解码并储存用户的信息
    users[userName.decode("utf-8")] = connect
    # 在连接显示框中显示是否连接成功
    printStr = "" + userName.decode("utf-8") + "连接\n"
    text.insert(tkinter.INSERT, printStr)
    # 向当前登录的客户端反馈登录信息并提供在线用户列表
    printStr = "登录成功!\n" + "当前在线的好友有：" + str(list(users.keys())) + "\n"
    connect.send(printStr.encode())
    # 向所有在线的客户端反馈新的好友登录信息并提供在线用户列表
    printStr = userName.decode("utf-8") + "已上线\n" + "当前在线的好友有：" + str(list(users.keys())) + "\n"
    for key in users:
        if key != userName.decode("utf-8"):
            users[key].send(printStr.encode())
    # 接受客户端发送的信息
    while True:
        rData = connect.recv(1024)
        dataStr = rData.decode("utf-8")
        # 分割字符串得到所要发送的用户名和客户端所发送的信息
        infolist = dataStr.split(":")
        # 通过客户端要发送的信息中是否指定要发送到的用户，如果没有选择要发送的用户，则默认为群发消息
        if infolist[0] == "":
            for key in users:
                if key != userName.decode("utf-8"):
                    users[key].send((userName.decode("utf-8") + "说（群发）:" + infolist[1]).encode("utf"))
                # 如果接收到的消息为客户端退出函数发送的“exit”则删掉该用户在users字典中的信息，并通知其他用户该用户已下线
        elif infolist[0] == "exit":
            del users[userName.decode("utf-8")]  # 删掉该用户信息
            printStr = "" + userName.decode("utf-8") + "下线\n"
            text.insert(tkinter.INSERT, printStr)
            for key in users:
                printStr = userName.decode("utf-8") + "已下线\n" + "当前在线的好友有：" + str(list(users.keys())) + "\n"
                users[key].send(printStr.encode())
        # 要发送信息的客户端向目标客户端发送信息
        else:
            if infolist[0] in users:
                users[infolist[0]].send((userName.decode("utf-8") + "说(私聊):" + infolist[1]).encode("utf"))
            else:
                printStr = infolist[0] + "不在线，上条消息未发出" + "\n"
                connect.send(printStr.encode())


# 界面启动按钮连接的函数
def startSever():
    # 启用一个线程开启服务器
    s = threading.Thread(target=start)
    s.start()


# 开启线程


def start():
    # 从输入端中获取ip和端口号
    ipStr = eip.get()
    portStr = eport.get()
    # socket嵌套字TCP的ipv4和相关协议
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定ip和端口号
    server.bind((ipStr, int(portStr)))
    # 设置监听和连接的最大的数量
    server.listen(10)
    # 服务器启动信息显示在信息窗口中
    printStr = "服务器启动成功！\n"
    text.insert(tkinter.INSERT, printStr)
    # 模拟服务器要一直运行所以使用死循环
    while True:
        # 接受所连接的客户端的信息
        connect, addrss = server.accept()
        # 每连接一个客户端就开启一个线程
        t = threading.Thread(target=run, args=(connect, addrss))
        t.start()


# 下面是关于界面的操作
labelIp = tkinter.Label(win, text='ip').grid(row=0, column=0)
eip = tkinter.Variable()

labelPort = tkinter.Label(win, text='port').grid(row=1, column=0)
eport = tkinter.Variable()

entryIp = tkinter.Entry(win, textvariable=eip).grid(row=0, column=1)
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=1, column=1)
button = tkinter.Button(win, text="启动", command=startSever).grid(row=1, column=2)
text = tkinter.Text(win, height=15, width=40)
labeltext = tkinter.Label(win, text='连接消息').grid(row=3, column=0)
text.grid(row=3, column=1)

win.mainloop()

