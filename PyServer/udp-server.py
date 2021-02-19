import socket
import datetime
import sys
import User
import Room
# ####################################################################
# #                       这是测试用的代码                            #                      
# ####################################################################
# defaultuser = User.creatuser(0,'Default','127.0.0.1')
# users = [defaultuser,]
# # print(users[0].username)
# # 这是生成虚拟用户的功能
# for i in range(10):
#     users.append(User.creatuser(i,'Zhang_San_'+str(i),'192.168.0.'+str(i)))
# defaultroom = Room.creatchatroom('DefaultRoom',0,users[0].username)
# rooms = [ ]
# # 这是生成房间的功能
# for i in range(10):
#     rooms.append(Room.creatchatroom('Room-'+str(i),i,users[i].username))
# # 这个是显示房间信息的功能
# def listrooms(roomslist):
#     str_roomlist = ''
#     for i in range(len(rooms)):
#         str_roomlist += str(roomslist[i].name+'\n')
#     return str_roomlist
# # listrooms(rooms)
# for i in range(20):
#     rooms[1].addmsg(users[1].username,'Test msg '+str(i))
# ####################################################################
# #                       测试代码结束                                #                      
# ####################################################################
# ##############################################################
#生成了一个UDP服务器名字叫S
# Room_10 = Room.creatchatroom('Room-10',16,'Zhangsan')
# Room_10.joinuser('Li_Si')
# Room_10.getroominfo()
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
    # reply = str(x)
    # reply += '\nHello, %s!' % data.decode('utf-8')
    # if str_command = 
    reply = str(x) + '\n' # + Room_10.getroominfo() # + listrooms(rooms)
    s.sendto(reply.encode('utf-8'), addr)
