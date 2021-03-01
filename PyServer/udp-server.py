import socket
import datetime
import sys
import User
import Room
import List

rooms = []
List.creatlotsroom(rooms,40)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('192.168.0.183', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    str_command, addr = s.recvfrom(1024)
    x = datetime.datetime.now()
    print('Received from %s:%s.' % addr)
    str_command = str_command.decode('utf-8')
    print(str_command)
    str_ans = ''
    if str_command == 'Get Room Info':
        str_ans = List.listrooms(rooms)
    elif str_command == 'Creat new room':
        # name,contain,creater
        newroom = Room.creatchatroom(('Created New Room - 20' + 's Room',16,addr)

    reply = str(x) + '\n'  + str_ans # + listrooms(rooms)
    str_ans = ''
    s.sendto(reply.encode('utf-8'), addr)
