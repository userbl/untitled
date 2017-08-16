import requests
import bs4

root_url='https://toutiao.io/prev/'
index_url = root_url+'2017-03-02'
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6'}



def get_news():
    # 格式化成2016-03-20 11:45:39形式
    today = '2017-03-01'#time.strftime("%Y-%m-%d", time.localtime())
    print(today)
    response = requests.get('https://toutiao.io/prev/'+today,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.content.decode("utf-8"),"html.parser")
    #print(response.content.decode("utf-8"))
    return [a for a in soup.select('div.content h3 a')]
    #print(links)


print("-----------------------------")
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
import  time

pp='@makelove*'
my_sender='userbl@126.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='bailong@huihaiedu.net' #收件人邮箱账号，为了后面易于维护，所以写成了变量


ret=True
try:


    server=smtplib.SMTP("smtp.126.com",25)  #发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender,pp)    #括号中对应的是发件人邮箱账号、邮箱密码
    for a in get_news():
        # print('https://toutiao.io'+a.get_text())
        msg = MIMEText('https://toutiao.io' + a.attrs.get('href'), 'plain', 'utf-8')
        msg['From'] = formataddr(["userbl", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["bailong", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = a.get_text() # 邮件的主题，也可以说是标题
        print(a.get_text() + '  ' + 'https://toutiao.io' + a.attrs.get('href'))
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        time.sleep(10)
    server.quit()   #这句是关闭连接的意思
except Exception as e:   #如果try中的语句没有执行，则会执行下面的ret=False
    ret=False
    print(e)





#print(get_news())
