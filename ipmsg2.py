from socket import *
from datetime import datetime
cs = socket(AF_INET, SOCK_DGRAM)
# cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# cs.sendto(b'1:abc:abc:%s:%d:wefwef', ('255.255.255.255', 2425))
# cs.sendto(bytes("1_lbt6_0#130#2C56DC3A719B#0#0#0#4001#9:1488996819:Administrator:DESKTOP-2NQ89L3:0:", encoding = "utf8") , ('255.255.255.255', 2425))
# Server received from ('192.168.9.64', 2425):1_lbt6_0#130#2C56DC3A719B#0#0#0#4001#9:1488994780:Administrator:DESKTOP-2NQ89L3:0:
# Server received from ('192.168.9.64', 2425):1_lbt6_0#130#2C56DC3A719B#0#0#0#4001#9:1488996819:Administrator:DESKTOP-2NQ89L3:0:

cs.sendto(bytes("1:100:飞秋测试:MRchai:32:hello", encoding = "gbk") , ('192.168.9.64', 2425))
data, address = cs.recvfrom(65535)
print(data)

# ("1:" + new Date().getTime() + ":" + SENDER + ":" + HOST
# 39           + ":" + IPMSG_SENDMSG + ":" + MSG_CONTENT).getBytes();
cs.close()

# my_socket = socket(AF_INET, SOCK_DGRAM)
# my_socket.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
# my_socket.sendto("wearetherock", ('<broadcast>' ,2425))
# my_socket.close()