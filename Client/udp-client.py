import time ## Using the sleep func to help the test clear
import socket
# import base64

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
commad_lib = [
    b'Server status', # Client can connect to a server
    b'Creat new room', # Client can create a room / join a room
    # b'Join in the new Room' # Client can join a room
    b'Get Room Info', # Client can list members of a room
    b'Get Room List', # Client can list all rooms
    b'Get Room Chat History', 
    b'Send Message ~20~ This is a Test Message frome Client',# Client can send messages to a room
    b'Join in Rooms 1,2,3,5', #  Client can join multiple (selected) rooms
    b'Send Message to ~1,2,5~ This is a Test Message frome Client', #Client can send distinct messages to multiple (selected) rooms
    b'',
    b'Disconnect!', # Client can disconnect from a server
#    b'Server plz shut down', # Server can disconnect from clients
   
    # Client can gracefully handle server crashes
    # Server can gracefully handle client crashes
]
def savetolog(s : str):
    file = open('log.txt',"a")
    file.write(s)
    file.close
for data in commad_lib:
    # send msg
    # b64cmd = base64.b64encode(data.encode())
    s.sendto(data, ('malker.cn', 9999))
    # get msg:
    reciv = s.recv(1024).decode('utf-8')
    print(reciv)
    savetolog(reciv)
    time.sleep(2)
    if reciv == 'Client will Disconnect':
        break
    
s.close()