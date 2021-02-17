#!/usr/bin/python3
# import '../PyServer/udp-server.py'
import sys
import datetime
import os


class creatchatroom:
    name = ''
    contain = 4
    path = './Rooms/'
    passwd = 123456
    # 这个是构造函数，存储了房间的基本信息，包括构造者，容纳人数，和房间的名字
    def __init__(self,name,contain,creater):
        self.name = name
        self.contain = contain
        self.path += name
        if os.path.exists(self.path) == False:
            file = open(self.path,"a")
            file.write('Creat Date:\n'+str(datetime.datetime.now())+'\n'+'Creater:\n'+creater+'\n\n\n')
            file.close
    # 这个是给房间生成了更改密码的方法
    def changepasswd(self, newpasswd):
        self.passwd = newpasswd
    # 这个是增加信息到存储聊天记录的文件中
    def addmsg(self,username,msg):
        file = open(self.path,"a")
        addedstr = str(datetime.datetime.now())+'\n'+ username + '\n' + msg + '\n'
        file.write(addedstr)
        file.close
    def getroomname(self):
        return self.name
        
# room1 = chatroom('chatroomOne', 16,"张三")
# room1 = room1.addmsgtopath("张三","这是一条测试内容，来查看是否换行和生成新文件")
# print(room1.name)
