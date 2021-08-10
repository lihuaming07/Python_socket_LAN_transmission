# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(679, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.layout_form = QtWidgets.QVBoxLayout(Form)
        self.layout_form.setObjectName("layout_form")
        self.box_monitor = QtWidgets.QGroupBox(Form)
        self.box_monitor.setObjectName("box_monitor")
        self.layout_monitor = QtWidgets.QHBoxLayout(self.box_monitor)
        self.layout_monitor.setObjectName("layout_monitor")
        self.list_msg = QtWidgets.QListWidget(self.box_monitor)
        self.list_msg.setObjectName("list_msg")
        self.layout_monitor.addWidget(self.list_msg)
        self.tabWidget_member = QtWidgets.QTableWidget(self.box_monitor)
        self.tabWidget_member.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabWidget_member.setWordWrap(True)
        self.tabWidget_member.setObjectName("tabWidget_member")
        self.tabWidget_member.setColumnCount(2)
        self.tabWidget_member.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabWidget_member.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabWidget_member.setHorizontalHeaderItem(1, item)
        self.tabWidget_member.horizontalHeader().setVisible(True)
        self.tabWidget_member.horizontalHeader().setSortIndicatorShown(False)
        self.tabWidget_member.verticalHeader().setVisible(True)
        self.layout_monitor.addWidget(self.tabWidget_member)
        self.layout_form.addWidget(self.box_monitor)
        self.box_control = QtWidgets.QGroupBox(Form)
        self.box_control.setObjectName("box_control")
        self.layout_main_control = QtWidgets.QVBoxLayout(self.box_control)
        self.layout_main_control.setObjectName("layout_main_control")
        self.layout_ip = QtWidgets.QHBoxLayout()
        self.layout_ip.setObjectName("layout_ip")
        self.btn_ip_rush = QtWidgets.QPushButton(self.box_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ip_rush.sizePolicy().hasHeightForWidth())
        self.btn_ip_rush.setSizePolicy(sizePolicy)
        self.btn_ip_rush.setObjectName("btn_ip_rush")
        self.layout_ip.addWidget(self.btn_ip_rush)
        self.lab_ip_title = QtWidgets.QLabel(self.box_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_ip_title.sizePolicy().hasHeightForWidth())
        self.lab_ip_title.setSizePolicy(sizePolicy)
        self.lab_ip_title.setObjectName("lab_ip_title")
        self.layout_ip.addWidget(self.lab_ip_title)
        self.lab_ip = QtWidgets.QLabel(self.box_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_ip.sizePolicy().hasHeightForWidth())
        self.lab_ip.setSizePolicy(sizePolicy)
        self.lab_ip.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lab_ip.setObjectName("lab_ip")
        self.layout_ip.addWidget(self.lab_ip)
        self.layout_main_control.addLayout(self.layout_ip)
        self.layout_port = QtWidgets.QHBoxLayout()
        self.layout_port.setObjectName("layout_port")
        self.lab_port = QtWidgets.QLabel(self.box_control)
        self.lab_port.setObjectName("lab_port")
        self.layout_port.addWidget(self.lab_port)
        self.edit_port = QtWidgets.QLineEdit(self.box_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_port.sizePolicy().hasHeightForWidth())
        self.edit_port.setSizePolicy(sizePolicy)
        self.edit_port.setObjectName("edit_port")
        self.layout_port.addWidget(self.edit_port)
        self.lab_password = QtWidgets.QLabel(self.box_control)
        self.lab_password.setObjectName("lab_password")
        self.layout_port.addWidget(self.lab_password)
        self.edit_password = QtWidgets.QLineEdit(self.box_control)
        self.edit_password.setStatusTip("")
        self.edit_password.setWhatsThis("")
        self.edit_password.setText("")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.edit_password.setDragEnabled(False)
        self.edit_password.setReadOnly(False)
        self.edit_password.setObjectName("edit_password")
        self.layout_port.addWidget(self.edit_password)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_port.addItem(spacerItem)
        self.layout_main_control.addLayout(self.layout_port)
        self.layout_control = QtWidgets.QHBoxLayout()
        self.layout_control.setObjectName("layout_control")
        self.layout_send = QtWidgets.QGridLayout()
        self.layout_send.setObjectName("layout_send")
        self.btn_send_file = QtWidgets.QPushButton(self.box_control)
        self.btn_send_file.setObjectName("btn_send_file")
        self.layout_send.addWidget(self.btn_send_file, 2, 0, 1, 1)
        self.btn_send = QtWidgets.QPushButton(self.box_control)
        self.btn_send.setEnabled(False)
        self.btn_send.setObjectName("btn_send")
        self.layout_send.addWidget(self.btn_send, 2, 1, 1, 1)
        self.edit_sendmsg = QtWidgets.QTextEdit(self.box_control)
        self.edit_sendmsg.setObjectName("edit_sendmsg")
        self.layout_send.addWidget(self.edit_sendmsg, 1, 0, 1, 2)
        self.layout_control.addLayout(self.layout_send)
        self.layout_menber_set = QtWidgets.QGridLayout()
        self.layout_menber_set.setObjectName("layout_menber_set")
        self.edit_forbidden_time = QtWidgets.QLineEdit(self.box_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_forbidden_time.sizePolicy().hasHeightForWidth())
        self.edit_forbidden_time.setSizePolicy(sizePolicy)
        self.edit_forbidden_time.setObjectName("edit_forbidden_time")
        self.layout_menber_set.addWidget(self.edit_forbidden_time, 2, 1, 1, 2)
        self.box_forbidden_mode = QtWidgets.QComboBox(self.box_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_forbidden_mode.sizePolicy().hasHeightForWidth())
        self.box_forbidden_mode.setSizePolicy(sizePolicy)
        self.box_forbidden_mode.setObjectName("box_forbidden_mode")
        self.box_forbidden_mode.addItem("")
        self.box_forbidden_mode.addItem("")
        self.box_forbidden_mode.addItem("")
        self.layout_menber_set.addWidget(self.box_forbidden_mode, 2, 3, 1, 1)
        self.btn_forbidden = QtWidgets.QPushButton(self.box_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_forbidden.sizePolicy().hasHeightForWidth())
        self.btn_forbidden.setSizePolicy(sizePolicy)
        self.btn_forbidden.setObjectName("btn_forbidden")
        self.layout_menber_set.addWidget(self.btn_forbidden, 2, 0, 1, 1)
        self.layout_forbidden = QtWidgets.QHBoxLayout()
        self.layout_forbidden.setObjectName("layout_forbidden")
        self.btn_break_bidden = QtWidgets.QPushButton(self.box_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_break_bidden.sizePolicy().hasHeightForWidth())
        self.btn_break_bidden.setSizePolicy(sizePolicy)
        self.btn_break_bidden.setObjectName("btn_break_bidden")
        self.layout_forbidden.addWidget(self.btn_break_bidden)
        self.btn_kill = QtWidgets.QPushButton(self.box_control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_kill.sizePolicy().hasHeightForWidth())
        self.btn_kill.setSizePolicy(sizePolicy)
        self.btn_kill.setObjectName("btn_kill")
        self.layout_forbidden.addWidget(self.btn_kill)
        self.layout_menber_set.addLayout(self.layout_forbidden, 3, 0, 1, 4)
        self.btn_disconnect = QtWidgets.QPushButton(self.box_control)
        self.btn_disconnect.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_disconnect.sizePolicy().hasHeightForWidth())
        self.btn_disconnect.setSizePolicy(sizePolicy)
        self.btn_disconnect.setObjectName("btn_disconnect")
        self.layout_menber_set.addWidget(self.btn_disconnect, 0, 2, 1, 2)
        self.btn_connect = QtWidgets.QPushButton(self.box_control)
        self.btn_connect.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_connect.sizePolicy().hasHeightForWidth())
        self.btn_connect.setSizePolicy(sizePolicy)
        self.btn_connect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_connect.setObjectName("btn_connect")
        self.layout_menber_set.addWidget(self.btn_connect, 0, 0, 1, 2)
        self.layout_control.addLayout(self.layout_menber_set)
        self.layout_main_control.addLayout(self.layout_control)
        self.layout_form.addWidget(self.box_control)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "光之局聊-服务端"))
        self.box_monitor.setTitle(_translate("Form", "监控区"))
        item = self.tabWidget_member.horizontalHeaderItem(0)
        item.setText(_translate("Form", "用户名"))
        item = self.tabWidget_member.horizontalHeaderItem(1)
        item.setText(_translate("Form", "禁言情况"))
        self.box_control.setTitle(_translate("Form", "控制区"))
        self.btn_ip_rush.setText(_translate("Form", "刷新ip"))
        self.lab_ip_title.setText(_translate("Form", "本机ip地址是:"))
        self.lab_ip.setText(_translate("Form", "正在读取中..."))
        self.lab_port.setText(_translate("Form", "设置服务器端口:"))
        self.edit_port.setInputMask(_translate("Form", "0000"))
        self.edit_port.setText(_translate("Form", "3800"))
        self.lab_password.setText(_translate("Form", "进服密码:"))
        self.edit_password.setPlaceholderText(_translate("Form", "无"))
        self.btn_send_file.setText(_translate("Form", "上传文件"))
        self.btn_send.setText(_translate("Form", "系统广播"))
        self.edit_forbidden_time.setPlaceholderText(_translate("Form", "禁言时长"))
        self.box_forbidden_mode.setItemText(0, _translate("Form", "永久"))
        self.box_forbidden_mode.setItemText(1, _translate("Form", "分钟"))
        self.box_forbidden_mode.setItemText(2, _translate("Form", "小时"))
        self.btn_forbidden.setText(_translate("Form", "禁言"))
        self.btn_break_bidden.setText(_translate("Form", "解除禁言"))
        self.btn_kill.setText(_translate("Form", "踢人"))
        self.btn_disconnect.setText(_translate("Form", "关闭服务器"))
        self.btn_connect.setText(_translate("Form", "开启服务器"))
