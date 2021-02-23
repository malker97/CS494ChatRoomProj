#!/usr/bin/python3
# 这是生成房间的功能
import Room
def creatlotsroom(arr_room,num):
    for i in range(num):
        arr_room.append(Room.creatchatroom('Room-'+str(i),i,'Test Uesr'))
    # return arr_room
# 这个是显示房间信息的功能
def listrooms(arr_room):
    str_roomlist = ''
    for i in range(len(arr_room)):
        str_roomlist += str(arr_room[i].name+'\n')
    return str_roomlist
# rooms = []
# creatlotsroom(rooms,20)
# print(listrooms(rooms))