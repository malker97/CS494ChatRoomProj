import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
commad_lib = [
    b'Server status', # Client can connect to a server
    b'Creat new room', # Client can create a room 
    b'Get Room Info', # Client can list members of a room
    b'Get Room List', # Client can list all rooms
    b'Get Room Chat History', 
    b'Send Message ~20~ This is a Test Message frome Client'# Client can send messages to a room
    b'Disconnect!' # Client can disconnect from a server
    b'Server plz shut down' # Server can disconnect from clients
    # Client can gracefully handle server crashes
    # Server can gracefully handle client crashes
]
for data in commad_lib:
    # 发送数据:
    s.sendto(data, ('malker.cn', 9999))
    # 接收数据:
    reciv = s.recv(1024).decode('utf-8')
    print(reciv)
    if reciv == 'Client will Disconnect':
        break
s.close()