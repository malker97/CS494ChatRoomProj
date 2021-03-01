import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
commad_lib = [
    b'Creat new room',
    b'Get Room Info',
    b'Get Room Chat History',
]
for data in commad_lib:
    # 发送数据:
    s.sendto(data, ('malker.cn', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()