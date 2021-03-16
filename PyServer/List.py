#!/usr/bin/python3
# creat rooms
import Room
def creatlotsroom(arr_room,num):
    for i in range(num):
        arr_room.append(Room.creatchatroom('Room-'+str(i),i,'Test Uesr'))
    # return arr_room
# show all infomation
def listrooms(arr_room):
    str_roomlist = ''
    for i in range(len(arr_room)):
        str_roomlist += str(arr_room[i].name+'\n')
    return str_roomlist
# rooms = []
# creatlotsroom(rooms,20)
# print(listrooms(rooms))