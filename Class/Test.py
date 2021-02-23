#!/usr/bin/python3
import User
import Room
import List

# rooms = []
# List.creatlotsroom(rooms,30)
# print(List.listrooms(rooms))
# rooms = []
# List.creatlotsroom(rooms,20)
# print(List.listrooms(rooms))
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
#     for i in range(len(rooms)):
#         print(roomslist[i].name)
# # listrooms(rooms)
# for i in range(20):
#     rooms[1].addmsg(users[1].username,'Test msg '+str(i))