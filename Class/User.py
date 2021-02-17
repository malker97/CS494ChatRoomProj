#!/usr/bin/python3
# import Room
import sys
import datetime
import os
import socket

class  creatuser:
    number = 0
    username = ''
    host = '0.0.0.0'
    enterdate = ''
    path = './Users/'
    def __init__(self,number,name,host):
        self.number = number
        self.path += str(number)+'_'+name
        self.username = name
        self.host = host
        self.enterdate = str(datetime.datetime.now())
        if os.path.exists(self.path) == False:
            file = open(self.path,"a")
            file.write("User: "+self.username+"\nNumber:"+str(self.number)+"\nDate:"+self.enterdate+"\nCreated")
            file.close
        # print("User: "+self.username+"\nNumber:"+str(self.number)+"\nCreated")
        
        

# print(user1.username)