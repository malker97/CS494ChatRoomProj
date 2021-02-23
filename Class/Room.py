#!/usr/bin/python3
# import '../PyServer/udp-server.py'
import sys
import datetime
import time
import os
# 这是基于用户的测试部分
import User
# user_1 = User.creatuser(1,'李华','192.168.0.2')



class creatchatroom:
    name = ''
    contain = 4
    path = './Rooms/'
    infopath = ''# 懒得优化信息读取方法了，所以开了个info文件来存储信息
    passwd = 123456
    # 这个是构造函数，存储了房间的基本信息，包括构造者，容纳人数，和房间的名字
    def __init__(self,name,contain,creater):
        self.name = name
        self.contain = contain
        self.path += name
        self.infopath += self.path + '_info'
        if os.path.exists(self.path) == False:
            file = open(self.path,"a")
            file.write('Creat Date:\n'+str(datetime.datetime.now())+'\n'+'Creater:\n'+creater+'\n\n')
            file.write(' \n')
            file.close
            file = open(self.infopath,"a")
            file.write('Creat Date:\n'+str(datetime.datetime.now())+'\n'+'Creater:\n'+creater+'\n\n')
            file.write(' \n')
            file.close
    # 这个是给房间生成了更改密码的方法
    def changepasswd(self, newpasswd):
        self.passwd = newpasswd
    # 这个是增加信息到存储聊天记录的文件中
    def addmsg(self,username,msg):
        file = open(self.path,"a")
        addedstr = str(datetime.datetime.now())+'\n'+ username + ':\n' + msg + '\n'
        file.write(addedstr)
        file.close
        # print(addedstr)
        return addedstr
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
        file = open(self.infopath,'r')
        for line in file:
            lines.append(line)
        file.close
        lines.insert(userinfoLine,needinsertline)
        s = ''.join(lines)
        file = open(self.infopath,'w+')
        file.write(s)
        file.close()
        del lines[:]
        file = open(self.path,"a")
        file.write(needinsertline)
        file.write(' \n')
        file.close
    # 这个是实现获取谁曾经加入房间，事实上只需要输出回车之前的内容
    def getroominfo(self):
        lines = []
        file = open(self.infopath,'r')
        # 4 + contain
        # roomsize = 4 + self.contain
        # temp = 0 
        for line in file:
            lines.append(line)
            # print(line)
            # temp += 1
            # if temp == roomsize:
            #     # print("break生效了")
            #     break
            if lines == ' ':
                print("break生效了")
                break
        file.close()
        s = ''.join(lines)
        # print(s)
        return s
# Room_1 = creatchatroom('Room-1',16,'Zhangsan')
# Room_2 = creatchatroom('Room-2',16,'Zhangsan')
# Room_10 = creatchatroom('Room-16',16,'Zhangsan')
# Room_10.joinuser('Li_Si')
# Room_10.getroominfo()
# # print(Room_10.getroominfo())
# Room_10.addmsg(user_1.username,'李华随便说了句话')
# print(Room_10.getchathistory())
# print(Room_10.getroominfo())
# print(Room_10.addmsg(user_1,"李华加入了聊天"))
# print(Room_10.getchathistory())
# sleep.sleep(1)
# print(Room_2.getchathistory())
# room1 = chatroom('chatroomOne', 16,"张三")
# room1 = room1.addmsgtopath("张三","这是一条测试内容，来查看是否换行和生成新文件")
# print(room1.name)
