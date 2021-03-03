import socket
import datetime
import sys
import User
import Room
import List

rooms = []
List.creatlotsroom(rooms,40)
# def switchcases(s: str)->str:


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
    if str_command == 'Server plz shut down':
        print('Server get the shutdown command, it will shutdown now!')
        s.sendto('Server get the shutdown command, it will shutdown now!'.encode('utf-8'),addr)
        break
    str_ans = ''
    if str_command == 'Get Room List':
        str_ans = List.listrooms(rooms)
    reply = str(x) + '\n'  + str_ans # + listrooms(rooms)
    str_ans = ''
    s.sendto(reply.encode('utf-8'), addr)
