from socket import *
from datetime import datetime
cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# for a in range(14) :
cs.sendto(bytes("1:100:飞秋测试:MRchai:{}:hello".format(3), encoding = "gbk") , ('192.168.9.64', 2425))

# ("1:" + new Date().getTime() + ":" + SENDER + ":" + HOST
# 39           + ":" + IPMSG_SENDMSG + ":" + MSG_CONTENT).getBytes();
cs.close()

# my_socket = socket(AF_INET, SOCK_DGRAM)
# my_socket.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
# my_socket.sendto("wearetherock", ('<broadcast>' ,2425))
# my_socket.close()

# 3 online_notify
# 32 send_msg