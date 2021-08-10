"""server和client中qt的重复代码移至此"""
from PyQt5.Qt import *


class Ui(QObject):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent=parent)

    def rush_memberQList(self, member_dict, send_box=False, myName=None):
        """
        刷新在线用户列表
        :param member_dict: 成员字典 user_list
        :param send_box: 是否修改发送对象框，在client_ui中有，但在server_ui中没有
        :param myName: 自己的名字,当send_box为真，发送对象框中是不能出现自己的，不能发给自己
        :return: None or "Name Key Error"名字错误，member_dict中没有此名
        """
        print(member_dict)
        self.parent().tabWidget_member.clear()
        self.parent().tabWidget_member.setHorizontalHeaderLabels(['用户名', '禁言情况'])
        if send_box:
            self.parent().box_send_to.clear()
        if member_dict:
            row = 0
            user_list = list(member_dict.keys())
            # 设置显示的数量
            self.parent().tabWidget_member.setColumnCount(2)
            self.parent().tabWidget_member.setRowCount(len(user_list))
            # self.parent.tabWidget_member.setRowCount(1)
            for user_name in user_list:
                forbidden = member_dict[user_name]
                # 显示禁言情况的变量
                if forbidden == 0:
                    forbidden = '无'
                elif forbidden == -1:
                    forbidden = '已禁言'
                else:
                    forbidden = '禁言中'
                self.parent().tabWidget_member.setItem(row, 0, QTableWidgetItem(user_name))  # 显示用户名
                self.parent().tabWidget_member.setItem(row, 1, QTableWidgetItem(forbidden))  # 显示禁言情况
                if send_box and user_name != myName:  # 自己不能发给自己
                    self.parent().box_send_to.addItem(user_name)  # 添加发送目标的选项
            if send_box:
                self.parent().box_send_to.addItem('全员')
                if myName in member_dict.keys():
                    if member_dict[myName] != 0:
                        self.parent().edit_sendmsg.setEnabled(False)
                        self.parent().edit_sendmsg.setPlaceholderText('你已被禁言')
                    else:
                        self.parent().edit_sendmsg.setEnabled(True)
                        self.parent().edit_sendmsg.setPlaceholderText('')
                else:
                    print(f'Key Error ,ui_qt.Ui.rush_memberQList, in 44 line, member_dict has no {myName}')
                    return 'Name Key Error'

    def clearQList(self):
        self.parent().tabWidget_member.clear()
        self.parent().tabWidget_member.setHorizontalHeaderLabels(['用户名', '禁言情况'])
