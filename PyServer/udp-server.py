import socket
# import base64
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
        rooms.append(Room.creatchatroom('Room-'+str(len(rooms)+1),len(rooms),'Test Uesr'))
        ans_str = 'Room has created'
    elif str_command == 'Get Room List':
        ans_str = List.listrooms(rooms)
    elif s == 'Get Room Info':
        ans_str = rooms[1].getroominfo()
    elif s == 'Get Room Chat History':
        ans_str = rooms[1].getchathistory()
    elif s == 'Send Message ~20~ This is a Test Message frome Client':
        rooms[20].addmsg('Test User', 'This is a Test Message frome Client')
        ans_str = rooms[20].getchathistory()
    elif s == 'Disconnect!':
        ans_str = 'Client will Disconnect'
    elif s == 'Join in Rooms 1,2,3,5':
        rooms[1].joinuser('Test User')
        rooms[2].joinuser('Test User')
        rooms[3].joinuser('Test User')
        rooms[5].joinuser('Test User')
        ans_str = rooms[1].getchathistory() + rooms[2].getchathistory() + rooms[3].getchathistory() + rooms[5].getchathistory()
    elif s == 'Send Message to ~1,2,5~ This is a Test Message frome Client':
        rooms[1].addmsg('Test User', 'This is a Test Message frome Client')
        rooms[2].addmsg('Test User', 'This is a Test Message frome Client')
        rooms[5].addmsg('Test User', 'This is a Test Message frome Client')
        ans_str = rooms[1].getchathistory() + rooms[2].getchathistory() + rooms[5].getchathistory()
    elif s == '':
        ans_str = 'Empty Command'
    #     for i in range(len(rooms)):
    
    return ans_str
def savetolog(s : str):
    file = open('log.txt',"a")
    file.write(s)
    file.close
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Combine the host to port 9999:
s.bind(('172.21.14.169', 9999))

print('Bind UDP on 9999...')

while True:
    # get msg from clint:
    str_command, addr = s.recvfrom(1024)
    x = datetime.datetime.now()
    print('Received from %s:%s.' % addr)
    str_command = str_command.decode('utf-8')
    print(str_command)
    savetolog(str_command)
    if str_command == 'Server plz shut down':
        print('Server get the shutdown command, it will shutdown now!')
        # s.sendto('Server get the shutdown command, it will shutdown now!'.encode('utf-8'),addr)
        break
    str_ans = ''
    
    str_ans = switchcases(str_command)
    str_ans = str(x) + '\n'  + str_ans
    # str_ans = base64.b64encode(str_ans.encode())
    reply = str_ans # + listrooms(rooms)
    str_ans = ''
    # s.sendto(reply.encode('Testencode'), addr)
    s.sendto(reply.encode('utf-8'), addr)
