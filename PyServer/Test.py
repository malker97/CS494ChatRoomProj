#!/usr/bin/python3
import User
import Room

defaultuser = User.creatuser(0,'Default','127.0.0.1')
users = [defaultuser,]
# print(users[0].username)
# creat virtual rooms
for i in range(10):
    users.append(User.creatuser(i,'Zhang_San_'+str(i),'192.168.0.'+str(i)))
defaultroom = Room.creatchatroom('DefaultRoom',0,users[0].username)
rooms = [ ]
# creat 10 rooms
for i in range(10):
    rooms.append(Room.creatchatroom('Room-'+str(i),i,users[i].username))
# list all rooms
def listrooms(roomslist):
    for i in range(len(rooms)):
        print(roomslist[i].name)
# listrooms(rooms)
for i in range(20):
    rooms[1].addmsg(users[1].username,'Test msg '+str(i))