#!/usr/bin/python
### 引入模块
import ipaddress
MIP = "192.168.20.0/24"
### 创建一个网段的对象，ipv4的网段地址
ips = ipaddress.ip_network(MIP)
### 查看对象ips的类型
print(type(ips))
### 查看网段的广播地址
print(ipaddress.ip_network(MIP).broadcast_address)

print(ipaddress.ip_network(MIP).hostmask)
### ipaddress
hosts = ipaddress.ip_network(MIP).hosts()
### 使用循环读取对象中的每个IP
print('hosts:'+str(type(hosts)))
# for IP in hosts:
    # print (IP)


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

for bb in allAddr(2,4) :
    print(bb)