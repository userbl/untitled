#!/bin/bash


_new_jdk_name=$(tar -tvf /home/cat/PycharmProjects/untitled/jdk-8u144-linux-x64.tar.gz| grep ^d |awk 'NR<2 {print $0}'| awk '{print $6}')
new_jdk_name=${_new_jdk_name:0:${#_new_jdk_name}-1}
#echo ${new_jdk_name:0:${#new_jdk_name}-1}

system_jdk_name=$(ls /usr/local/ | grep jdk | tail -1)
echo "new jdk:$new_jdk_name"
echo "sys jdk:$system_jdk_name"
if [ $new_jdk_name != $system_jdk_name ]; then
    echo 'JDK need to be updated!'
    echo "Setup new JDK  $new_jdk_name"
    tar -xzf /home/cat/PycharmProjects/untitled/jdk-8u144-linux-x64.tar.gz -C /usr/local/
    if [ $? -eq 0  ]; then
	echo "unzip success！"
	echo "set env"
	>/etc/profile.d/java.sh
	cat << EOF > /etc/profile.d/java.sh
	export JAVA_HOME=/usr/local/$new_jdk_name
	export CLASSPATH=.:\$JAVA_HOME/lib/dt.jar:\$JAVA_HOME/lib/tools.jar
	export PATH=\$JAVA_HOME/bin:\$PATH
EOF
	chmod 755  /etc/profile.d/java.sh
	echo " update time： $(date)" | /usr/bin/mailx   -r "userbl <userbl@126.com>"  -s "Update JDK to  $new_jdk_name"  -S smtp="smtp.126.com"  -S smtp-auth=login  -S smtp-auth-user="userbl@126.com"  -S smtp-auth-password="@makelove*"  bailong@huihaiedu.net
    fi
else
	echo "Don't need update!"
fi


#tar -xzf /home/cat/PycharmProjects/untitled/jdk-8u144-linux-x64.tar.gz -C /usr/local/


# ls /usr/local/ | grep jdk | awk 'END {print}'
#new_jdk_name2=$(ls /usr/local/ | grep jdk | tail -1)
#echo $new_jdk_name
