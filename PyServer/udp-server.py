import socket
import datetime


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('192.168.0.106', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    x = datetime.datetime.now()
    print('Received from %s:%s.' % addr)
    # reply = str(x)
    # reply += '\nHello, %s!' % data.decode('utf-8')
    reply = str(x) + '\n' +data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)
