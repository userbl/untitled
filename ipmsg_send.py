from socket import *
from datetime import datetime
import re

cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

cs.sendto(bytes("1:100:飞秋测试:MRchai:32:hello:1001", encoding = "gb2312") , ('192.168.9.64', 2425))
cs.sendto(bytes("1:100:飞秋测试:MRchai:288:hello:1001", encoding = "gb2312") , ('192.168.9.64', 2425))
while True :
    data, address = cs.recvfrom(65535)
    decode = data.decode('gb2312')
    split = re.split(r':', decode)
    print(split)
    if(split[4] =='288'):
        cs.sendto(bytes("1:100:飞秋测试:MRchai:33:"+split[1]+":", encoding="gb2312"), address)

cs.close()

# require message check send cmd 288
# do not require message check send cmd 32
# response require check message cmd 33

