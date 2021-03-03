import socket
import datetime
import sys
import User
import Room
import List

rooms = []
List.creatlotsroom(rooms,40)
def switchcases(s: str)->str:
    # b'Server status', # Client can connect to a server
    # b'Creat new room', # Client can create a room 
    # b'Get Room Info', # Client can list members of a room
    # b'Get Room List', # Client can list all rooms
    # b'Get Room Chat History', 
    # b'Send Message ~20~ This is a Test Message frome Client'# Client can send messages to a room
    # b'Disconnect!' # Client can disconnect from a server
    # b'Server plz shut down' # Server can disconnect from clients
    # # Client can gracefully handle server crashes
    # # Server can gracefully handle client crashes
    ans_str = ''
    if s == 'Server status':
        ans_str = "Connected Ok"
    elif s == 'Creat new room':
        rooms.append(Room.creatchatroom('Room-'+str(len(rooms)),len(rooms),'Test Uesr'))
        ans_str = 'Room has created'
    # elif s == 'Get Room Info':
    #     for i in range(len(rooms))
    return ans_str

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
        # s.sendto('Server get the shutdown command, it will shutdown now!'.encode('utf-8'),addr)
        break
    str_ans = ''
    if str_command == 'Get Room List':
        str_ans = List.listrooms(rooms)
    reply = str(x) + '\n'  + str_ans # + listrooms(rooms)
    str_ans = ''
    s.sendto(reply.encode('utf-8'), addr)
