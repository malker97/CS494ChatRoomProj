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
            file.write('Creat Date:\n'+str(datetime.datetime.now())+'\n'+'Creater:\n'+creater+'\n')
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
    # 这应该只是个封装了get方法，但是目测可能用不到
    def getroomname(self):
        return self.name
    # 这个是获取聊天记录，但是懒得实现了，所以调取了读取文件内的所以内容
    def getchathistory(self):
        file = open(self.path,'r')
        chathistory = file.read()
        # print(chathistory)
        file.close()
        return chathistory
    # 这个是记录用户加入的时间在第5行
    def joinuser(self, str_username):
        userjoindate = str(datetime.datetime.now())
        userinfoLine = 4 # 这是事实上是第五行
        needinsertline = 'User: '+ str_username +'\tJoined at '+ userjoindate + '\n'
        lines = []
        file = open(self.path,'r')
        for line in file:
            lines.append(line)
        file.close
        lines.insert(userinfoLine,needinsertline)
        s = ''.join(lines)
        file = open(self.path,'w+')
        file.write(s)
        file.close()
        del lines[:]
    # 这个是实现获取谁曾经加入房间，事实上只需要输出回车之前的内容
    def getroominfo(self):
        lines = []
        file = open(self.path,'r')
        for line in file:
            lines.append(line)
            if lines == '\n':
                break
        file.close()
        s = ''.join(lines)
        print(s)
# Room_1 = creatchatroom('Room-1',16,'Zhangsan')
# Room_2 = creatchatroom('Room-2',16,'Zhangsan')
Room_10 = creatchatroom('Room-10',16,'Zhangsan')
Room_10.joinuser('Li_Si')
Room_10.getroominfo()
# print(Room_2.getchathistory())
# room1 = chatroom('chatroomOne', 16,"张三")
# room1 = room1.addmsgtopath("张三","这是一条测试内容，来查看是否换行和生成新文件")
# print(room1.name)
