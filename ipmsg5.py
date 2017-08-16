#!/usr/bin/python3
# coding=UTF-8

from socket import *
from datetime import datetime
import re
import  threading
import  string

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# cs.sendto(b'1:abc:abc:%s:%d:wefwef', ('255.255.255.255', 2425))
cs.bind(('192.168.9.55',2425))
# for a in range(10):
#     print(a)

# send online message
import ipaddress
def allAddr(start,end) :

    for a in range(start,end+1) :
        # print(a)

        MIP = "192.168."+str(a)+".0/24"
        ### 创建一个网段的对象，ipv4的网段地址
        ips = ipaddress.ip_network(MIP)
        ### 查看对象ips的类型
        # print(type(ips))
        ### 查看网段的广播地址
        # print(ipaddress.ip_network(MIP).broadcast_address)

        # print(ipaddress.ip_network(MIP).hostmask)
        ### ipaddress
        hosts = ipaddress.ip_network(MIP).hosts()
        ### 使用循环读取对象中的每个IP
        # print('hosts:' + str(type(hosts)))
        for IP in hosts:
            yield str(IP)
            # print(IP)

for bb in allAddr(1,40) :
    # print(bb)
    cs.sendto(bytes("1:100:飞秋测试:MRchai:"+str(1)+":", encoding = "gb2312") , (bb, 2425))

add = 0
def dia() :
    # cs2 = socket(AF_INET, SOCK_DGRAM)
    # cs2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # cs2.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    while True:
        input1 = input("")

        split = re.split(r':', input1)
        if('@' in split) :
            print('@ ' + d_name[split[1]])
            add =split[1]
        else:
            cs.sendto(bytes("1:100:飞秋测试:MRchai:288:"+input1, encoding="gb2312"), (d_address[add], 2425))


t = threading.Thread(target=dia, name='LoopThread')
t.start()


a = int(0)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d_name = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d_name2 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d_address = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
while True :
    data, address = cs.recvfrom(65535)
    decode = data.decode('gb2312')

    # print(decode)

    # print(a)

    d[str(a)]=decode
    # print(d)

    split = re.split(r':', decode)
    # print(split)
    print(str(a)+" "+split[5])

    # d_name[str(a)] =split[5]
    # d_name2[str(address[0])] = split[5]
    # d_address[str(a)] = address[0]

    # print(d_name2)
    # print(d_address)

    # print("-----------")
    # print(split[4]) #cmd
    # print(split[3]) #host
    # print("-----------==")
    if(split[4] == '0') :
        print("send online msg")
        print(address)
        cs.sendto(bytes("1:100:飞秋测试:MRchai:6291459:", encoding="gb2312"), address) # send I'm online

    elif (split[4] == '6291459') :
        d_name[str(a)] = split[5]
        d_name2[str(address[0])] = split[5]
        # print(d_name)
        d_address[str(a)] = address[0]
    elif (split[4] == '114') :
        cs.sendto(bytes("1:100:飞秋测试:MRchai:6291459:", encoding="gb2312"), address)
    elif (split[4] =='288'):
        # print(decode)
        print(d_name2[address[0]]+": " + split[5])
        cs.sendto(bytes("1:100:飞秋测试:MRchai:33:"+split[1]+":", encoding="gb2312"), address)

    a = a + 1


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
