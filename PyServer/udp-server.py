import socket
import datetime
import sys
import User
import Room
import List


# 构造测试房间组的方法
# rooms = []
# List.creatlotsroom(rooms,40)
#
# #测试用的字符串
# str_getroomhis = 'GET ROOM HIS'
# str_getroomlist = 'GET ROOM LIST'
# str_getroominfo = 'GET ROOM INFO'
#生成了一个UDP服务器名字叫S


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('192.168.0.183', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    str_command, addr = s.recvfrom(1024)
    x = datetime.datetime.now()
    print('Received from %s:%s.' % addr)
    # print(addr)
    str_command = str_command.decode('utf-8')
    print(str_command)
    str_ans = ''
    #测试部分
    # str_ans = List.listrooms(rooms)
    #
    reply = str(x) + '\n'  + str_ans # + listrooms(rooms)
    s.sendto(reply.encode('utf-8'), addr)
