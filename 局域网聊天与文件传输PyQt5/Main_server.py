import sys
import time

from PyQt5.Qt import *

import chat
import ui_qt
from ui_server import *


class MainServer(QWidget, Ui_Form):
    def __init__(self):
        super(MainServer, self).__init__()
        self.setupUi(self)  # 初始化界面
        self.chat = chat.Server(self.radio_command)  # 聊天类的实例化
        self.qt = ui_qt.Ui(self)
        self.set_ui_connect()  # 定义界面的槽函数等

    def set_ui_connect(self):
        self.lab_ip.setText(self.chat.server_ip)  # 显示服务端ip
        self.btn_ip_rush.clicked.connect(self.rush_ip_show)
        self.btn_connect.clicked.connect(self.startServer)  # 开启服务器按钮
        self.btn_disconnect.clicked.connect(self.closeServer)  # 关闭服务器按钮
        self.btn_send.clicked.connect(self.send_msg)  # ”系统广播“按钮按下的槽函数
        self.btn_forbidden.clicked.connect(self.forbidden)
        self.btn_break_bidden.clicked.connect(self.break_forbidden)
        self.btn_kill.clicked.connect(self.kill_member)
        self.edit_sendmsg.textChanged.connect(self.set_send_btn)  # 消息编辑框, 内容变化时的槽函数
        self.edit_forbidden_time.setEnabled(False)  # 不可编辑
        self.box_forbidden_mode.currentIndexChanged.connect(self.change_forbidden_mode)
        # 校验器,只允许输入4位数字
        portValidator = QIntValidator(self)
        portValidator.setRange(0, 9999)
        self.edit_port.setValidator(portValidator)  # 只允许输入数字

    def rush_ip_show(self):
        self.btn_ip_rush.setEnabled(False)
        self.chat.rush_ip()  # 更新ip变量
        self.lab_ip.setText(self.chat.server_ip)  # 显示服务端ip
        self.btn_ip_rush.setText('已刷新')
        time.sleep(1)
        self.btn_ip_rush.setText('刷新ip')
        self.btn_ip_rush.setEnabled(True)

    def startServer(self):
        self.btn_connect.setEnabled(False)
        self.edit_port.setEnabled(False)
        try:
            port = int(self.edit_port.text())
        except:
            self.btn_connect.setEnabled(True)
            self.edit_port.setEnabled(True)
            return
        if self.chat.start(port=port) == 'fail to start ip_port':
            self.Qmsg('提升', '启动服务器失败，可能端口被占用，请切换端口')
            self.btn_connect.setEnabled(True)
            self.edit_port.setEnabled(True)
            return False
        self.btn_disconnect.setEnabled(True)
        self.qt.clearQList()
        self.list_msg.clear()
        self.list_msg.addItem('启动成功')

    def closeServer(self):
        if not self.Qask('警告', '确定关闭服务器吗？？？！'):
            return False
        self.btn_disconnect.setEnabled(False)
        self.chat.close()
        self.btn_connect.setEnabled(True)
        self.edit_port.setEnabled(True)
        return True

    def radio_command(self, msg):
        if msg['type'] == 'users':  # 用户列表
            self.qt.rush_memberQList(self.chat.user_list)  # 显示用户列表
        elif msg['type'] == 'msg':
            print(msg)
            msgSender = '系统消息' if msg['sender'] == 'system' else msg['sender']
            msgStr = f"{msgSender}: {msg['text']}"
            self.list_msg.addItem(QListWidgetItem(msgStr))

    def send_msg(self):
        self.chat.radio_msg(self.chat.msg(self.edit_sendmsg.toPlainText()))
        self.edit_sendmsg.clear()

    def set_send_btn(self):
        # 当消息变化时设置发送按钮的可点击状态
        if self.chat.server_runState:
            if self.edit_sendmsg.toPlainText():
                self.btn_send.setEnabled(True)
            else:
                self.btn_send.setEnabled(False)
        else:
            self.btn_send.setEnabled(False)

    def member_selected_rows(self):
        items = self.tabWidget_member.selectedItems()  # 获取成员列表所选的所有QTableWidget的items
        if items:
            rows = set()  # 所选择的行的序号的集合
            for item in items:  # 因为items的行序号重合，所有用集合保证唯一性
                row = self.tabWidget_member.row(item)
                rows.add(row)
            return rows
        return False

    def forbidden(self):
        rows = self.member_selected_rows()
        if rows:
            for row in rows:
                user_name = self.tabWidget_member.item(row, 0).text()  # 获取禁言的名称
                forbidden_mode = self.box_forbidden_mode.itemText(self.box_forbidden_mode.currentIndex())  # 禁言模式
                if forbidden_mode == '永久':
                    time_stamp = -1
                else:
                    if forbidden_mode == '小时':
                        multiple = 3600
                    elif forbidden_mode == '分钟':
                        multiple = 60
                    time_long = int(self.edit_forbidden_time.text()) * multiple
                    time_stamp = time.time() + time_long
                self.chat.forbidden(user_name, time_stamp)

    def break_forbidden(self):
        rows = self.member_selected_rows()
        if rows:
            for row in rows:
                user_name = self.tabWidget_member.item(row, 0).text()
                self.chat.break_forbidden(user_name)

    def kill_member(self):
        rows = self.member_selected_rows()
        if rows:
            for row in rows:
                user_name = self.tabWidget_member.item(row, 0).text()
                self.chat.kill_member(user_name)

    def change_forbidden_mode(self):
        forbidden_mode = self.box_forbidden_mode.itemText(self.box_forbidden_mode.currentIndex())
        if forbidden_mode == '永久':
            self.edit_forbidden_time.setEnabled(False)
        else:
            self.edit_forbidden_time.setEnabled(True)

    def Qmsg(self, title, info, mode=QMessageBox.Warning):
        msg_box = QMessageBox(mode, title, info)
        msg_box.exec_()

    def Qask(self, title, info):
        msg_box = QMessageBox.critical(self, title, info, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        return msg_box == QMessageBox.Yes  # 确认返回True，否则为False

    def closeEvent(self, event):
        if self.closeServer():
            event.accept()


# 启动主窗口程序
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainServer()
    main.show()
    sys.exit(app.exec_())

