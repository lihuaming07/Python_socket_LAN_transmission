import sys
import time

from PyQt5.Qt import *

import chat
import ui_qt
from ui_client import *


class MainServer(QWidget, Ui_Form):
    def __init__(self):
        super(MainServer, self).__init__()
        self.setupUi(self)  # 初始化界面
        self.chat = chat.Client(self.receive_command)  # 聊天类的实例化
        self.qt = ui_qt.Ui(self)
        self.set_ui_connect()  # 定义界面的槽函数等

    def set_ui_connect(self):
        self.edit_set_name.setPlaceholderText(self.chat.user_name)
        self.btn_connect.clicked.connect(self.start_client)  # 连接服务器按钮
        self.btn_disconnect.clicked.connect(self.break_client)  # 关闭服务器按钮
        self.btn_send.clicked.connect(self.send_msg)  # ”系统广播“按钮按下的槽函数
        self.edit_set_name.textChanged.connect(self.set_name)
        self.edit_sendmsg.textChanged.connect(self.set_send_btn)  # 消息编辑框, 内容变化时的槽函数
        # 校验器,只允许输入4位数字
        portValidator = QIntValidator(self)
        portValidator.setRange(0, 9999)
        self.edit_port.setValidator(portValidator)  # 只允许输入数字
        # 校验器，只允许输入数字
        reg = QRegExp('[0-9]{8}')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

    def start_client(self):
        self.btn_connect.setEnabled(False)
        self.edit_ip.setEnabled(False)
        self.edit_port.setEnabled(False)
        self.edit_set_name.setEnabled(False)
        try:
            port = int(self.edit_port.text())
        except:
            self.Qmsg('提示', '端口错误')
            self.btn_connect.setEnabled(True)
            self.edit_ip.setEnabled(True)
            self.edit_port.setEnabled(True)
            self.edit_set_name.setEnabled(True)
            return
        if self.chat.start(self.edit_ip.text(), port, self.edit_set_name.text()) == 'fail to connect':
            self.btn_connect.setEnabled(True)
            self.edit_ip.setEnabled(True)
            self.edit_port.setEnabled(True)
            self.edit_set_name.setEnabled(True)
            self.Qmsg('提示', '连接失败')
            return
        self.btn_disconnect.setEnabled(True)
        self.qt.clearQList()
        self.list_msg.clear()
        self.list_msg.addItem('连接成功')

    def break_client(self, show='你已下线', send=True):
        # send参数为是否通知服务器
        self.btn_disconnect.setEnabled(False)
        if send:
            self.chat.break_client()
        if show:
            self.list_msg.addItem(show)
        self.edit_ip.setEnabled(True)
        self.edit_port.setEnabled(True)
        self.edit_set_name.setEnabled(True)
        self.btn_connect.setEnabled(True)

    def receive_command(self, msg):
        if msg['type'] == 'users':  # 用户列表
            self.qt.rush_memberQList(self.chat.user_list, True, self.chat.user_name)
        elif msg['type'] == 'msg':
            msgSender = '系统消息' if msg['sender'] == 'system' else msg['sender']
            msgStr = f"{msgSender}: {msg['text']}"
            self.list_msg.addItem(msgStr)
        elif msg['type'] == 'close':
            self.break_client('服务器断开连接', False)
        elif msg['type'] == 'kill':
            self.break_client('你被踢出局聊', False)

    def send_msg(self):
        send_name = self.box_send_to.itemText(self.box_send_to.currentIndex())
        if send_name == '全员':
            receive = ''
        else:
            receive = send_name
        self.chat.send(self.chat.msg(self.edit_sendmsg.toPlainText()))
        self.edit_sendmsg.clear()

    def set_name(self):
        # 当名称框内容变化时设置变量
        if not self.chat.client_runState:
            self.chat.user_name = self.edit_set_name.text()
        else:
            self.edit_set_name.setText(self.chat.user_name)  # 如果有连接，则恢复原来的名称

    def set_send_btn(self):
        # 当消息变化时设置发送按钮的可点击状态
        print(f'set send btn runState is {self.chat.client_runState}, {self.chat.user_list[self.chat.user_name] != 0}')
        if self.chat.client_runState and self.chat.user_list[self.chat.user_name] == 0:
            if self.edit_sendmsg.toPlainText():
                self.btn_send.setEnabled(True)
            else:
                self.btn_send.setEnabled(False)
        else:
            self.btn_send.setEnabled(False)

    def Qmsg(self, title, info, mode=QMessageBox.Warning):
        msg_box = QMessageBox(mode, title, info)
        msg_box.exec_()

    def Qask(self, title, info):
        msg_box = QMessageBox.critical(self, title, info, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        return msg_box == QMessageBox.Yes  # 确认返回True，否则为False

    def closeEvent(self, event):
        self.break_client()
        event.accept()


# 启动主窗口程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainServer()
    main.show()
    sys.exit(app.exec_())

