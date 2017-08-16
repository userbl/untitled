from socket import *
from datetime import datetime
import re
import  threading

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# cs.sendto(b'1:abc:abc:%s:%d:wefwef', ('255.255.255.255', 2425))
cs.bind(('192.168.9.194',2425))
# for a in range(10):
#     print(a)

# send online message
cs.sendto(bytes("1:100:飞秋测试:MRchai:"+str(1)+":", encoding = "gb2312") , ('255.255.255.255', 2425))


# def dia() :
#
#     input1 = input("msg:")
#     print(input1)
#     pass
#
# t = threading.Thread(target=dia, name='LoopThread')
# t.start()
# t.join()

a = int(0)
while True :
    data, address = cs.recvfrom(65535)
    decode = data.decode('gb2312')

    print(decode)
    a=a+1
    print(a)


    split = re.split(r':', decode)
    # print(split)

    # print("-----------")
    # print(split[4]) #cmd
    # print(split[3]) #host
    # print("-----------==")
    if(split[4] == '0') :
        print("send online msg")
        print(address)
        cs.sendto(bytes("1:100:飞秋测试:MRchai:6291459:", encoding="gb2312"), address)
    elif (split[4] == '114') :
        cs.sendto(bytes("1:100:飞秋测试:MRchai:6291459:", encoding="gb2312"), address)

# Server received from ('192.168.9.64', 2425):1_lbt6_0#130#2C56DC3A719B#0#0#0#4001#9:1488994780:Administrator:DESKTOP-2NQ89L3:0:
# Server received from ('192.168.9.64', 2425):1_lbt6_0#130#2C56DC3A719B#0#0#0#4001#9:1488996819:Administrator:DESKTOP-2NQ89L3:0:

# cs.sendto(bytes("1:100:飞秋测试:MRchai:32:hello", encoding = "gb2312") , ('192.168.9.64', 2425))
# while True :
#     data, address = cs.recvfrom(65535)
#     decode = data.decode('gb2312')
#     print(decode)
#     split = re.split(r':', decode)
#     print(split)
#     # 1:XXX:<用户名>:<主机名>:IPMSG_RECVMSG:12345
#     # for a in range(50):
#     cs.sendto(bytes("1_lbt6_0#130#2C56DC3A719B#0#0#0#4001#9:1489066184:飞秋测试:MRchai6291457:abc"), encoding = "gb2312") , ('192.168.9.64', 2425))

# data, address = cs.recvfrom(65535)
# print(data)

# ("1:" + new Date().getTime() + ":" + SENDER + ":" + HOST
# 39           + ":" + IPMSG_SENDMSG + ":" + MSG_CONTENT).getBytes();
cs.close()

# my_socket = socket(AF_INET, SOCK_DGRAM)
# my_socket.setsockopt(SOL_SOCKET, SO_BROADCAST,1)
# my_socket.sendto("wearetherock", ('<broadcast>' ,2425))
# my_socket.close()

# 4 online_notify
# 32 send_msg

# off line 6291458
# on line 6291459
