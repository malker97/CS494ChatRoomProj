#!/usr/bin/python3
# import '../PyServer/udp-server.py'
import sys
import datetime
import time
import os
# Test for the virtual user
import User
# user_1 = User.creatuser(1,'李华','192.168.0.2')



class creatchatroom:
    name = ''
    contain = 4
    path = './Rooms/'
    infopath = ''# get the infomation
    passwd = 123456
    # this is creat function, to creat room name, contain creater
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
    # to protect the passwd
    def changepasswd(self, newpasswd):
        self.passwd = newpasswd
    # add some msg to chat history file
    def addmsg(self,username,msg):
        file = open(self.path,"a")
        addedstr = str(datetime.datetime.now())+'\n'+ username + ':\n' + msg + '\n'
        file.write(addedstr)
        file.close
        # print(addedstr)
        return addedstr
    # a simple get method
    def getroomname(self):
        return self.name
    # to get all chat history
    def getchathistory(self):
        file = open(self.path,'r')
        chathistory = file.read()
        # print(chathistory)
        file.close()
        return chathistory
    # the join infomation in 
    def joinuser(self, str_username):
        userjoindate = str(datetime.datetime.now())
        userinfoLine = 4 # actually 5
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
        # get room infomation
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
                print("break is working")
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
