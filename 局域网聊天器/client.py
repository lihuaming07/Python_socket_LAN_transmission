# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/qq_42620328/article/details/108256970?ops_request_misc=&request_id=&biz_id=102&utm_term=python%20socket%E9%80%9A%E4%BF%A1%E5%B8%A6%E7%95%8C%E9%9D%A2&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-6-108256970.first_rank_v2_pc_rank_v29&spm=1018.2226.3001.4187
"""
import tkinter
import socket
import threading
import time

win = tkinter.Tk()
win.title("客户端")
win.geometry("400x300+300+200")
ck = None


def getInfo():
    while True:
        data = ck.recv(1024)  # 用于接受服务其发送的信息
        # 接收消息时同步获取系统时间并显示在消息显示框上
        text.insert(tkinter.INSERT, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n')
        text.insert(tkinter.INSERT, data.decode("utf-8"))


def connectServer():
    global ck  # 全局
    ipStr = eip.get()
    portStr = eport.get()
    userStr = euser.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socked所准守ipv4相关协议
    client.connect((ipStr, int(portStr)))  # 连接服务器
    client.send(userStr.encode("utf-8"))  # 将自己的登录名发送给服务器，函数会附带自己的IP信息
    ck = client
    t = threading.Thread(target=getInfo)
    t.start()


def sendMail():
    friend = None
    friend = efriend.get()
    sendStr = esend.get()
    # 自己发出的消息服务器不会重发会给自己，所以在客户端定义界面显示自己发送的消息
    if friend != "":
        text.insert(tkinter.INSERT,
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n' + '我对' + friend + '说：' + sendStr + '\n')
    else:
        text.insert(tkinter.INSERT,
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n' + '我(群发）说：' + sendStr + '\n')
    # 将消息发给服务器，添加“：”分割是要方便服务器端用正则表达式分出要发送的用户名和要发送的消息
    sendStr = friend + ":" + sendStr + "\n"
    ck.send(sendStr.encode("utf-8"))
    # 清空文本框
    # esend.set("")  # 考虑到多发，不清楚消息框


def Exit():
    # 我在服务器端定义了接收到“exit”就判定该用户下线，并删掉该用户的资料
    sendStr = "exit" + ":" + ""
    ck.send(sendStr.encode("utf-8"))
    text.insert(tkinter.INSERT, "您已下线，如需接收信息请重新登录。\n")


# 下面是界面
labelUse = tkinter.Label(win, text="userName").grid(row=0, column=0)
euser = tkinter.Variable()
entryUser = tkinter.Entry(win, textvariable=euser).grid(row=0, column=1)

labelIp = tkinter.Label(win, text="服务器ip").grid(row=1, column=0)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=1, column=1)

labelPort = tkinter.Label(win, text="port").grid(row=2, column=0)
eport = tkinter.Variable()
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=2, column=1)

button = tkinter.Button(win, text="登录", command=connectServer).grid(row=0, column=2)

text = tkinter.Text(win, height=10, width=40)
labeltext = tkinter.Label(win, text="显示消息").grid(row=4, column=0)
text.grid(row=4, column=1)

esend = tkinter.Variable()
labelesend = tkinter.Label(win, text="发送的消息").grid(row=5, column=0)
entrySend = tkinter.Entry(win, textvariable=esend).grid(row=5, column=1)

efriend = tkinter.Variable()
labelefriend = tkinter.Label(win, text="发给谁").grid(row=6, column=0)
entryFriend = tkinter.Entry(win, textvariable=efriend).grid(row=6, column=1)

button2 = tkinter.Button(win, text="发送", command=sendMail).grid(row=6, column=2)
button2 = tkinter.Button(win, text="下线", command=Exit).grid(row=2, column=2)
win.mainloop()

