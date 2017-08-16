#!/bin/bash
rm ~/hosts -rf
unzip -P laod.org -u ~/Android安卓跟Linux系列.zip

> /etc/hosts

cat << eof >/etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6


192.168.12.100 git.hhedu.cn
192.168.12.101 wiki.hhedu.cn

192.168.11.210 maven.hhedu.cn

0.0.0.0 account.jetbrains.com
192.168.9.105 monitor.hhedu.cn
61.213.171.9 download.oracle.com
182.92.213.160 toutiao.io

eof
cat /home/cat/my-hosts >>/etc/hosts
awk 'NR>18 {print $0}' ~/hosts >>/etc/hosts

echo "`date`  update hosts is ok" >> ok.txt
