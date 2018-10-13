#
#coding=utf-8
'''
name:chenyang
email: 2898891726@qq.com
date : 2018-09-11
class : aid
introduce: chatroom client
env: python3
'''
from socket import *
import os,sys
import time
# 发消息
def send_msg(s,name,addr):
    while True:
        text=input('发言')
        if text.strip()=='quit':
            msg = 'Q '+name
            s.sendto(msg.encode(),addr)
            sys.exit()
        msg='c %s %s'%(name,text)
        s.sendto(msg.encode(),addr)
# 接收消息
def recv_msg(s):
    while True:
        data,addr =s.recvfrom(1024)
        if data.decode()=='exit':
            sys.exit()
        print(data.decode(),'\n%20s'%'发言:',end='')


def main():
    #client address
    ADDR=('127.0.0.1',7898)
    #创建套接字
    s=socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    while True:
        name = input('请输入姓名')
        msg ='l '+name
        # 发送登录请求
        s.sendto(msg.encode(),ADDR)
        # 等待服务器回复
        data,addr = s.recvfrom(1024)
        if data.decode()=='ok':
            print('你已经进入聊天')
            break
        else:
            print(data.decode())
    #创建父子进程
    pid=os.fork()
    if pid<0:
        sys.exit()
    elif pid==0:
        send_msg(s,name,addr)
    else:
        recv_msg(s)


if __name__=='__main__':
    main()