# 
#coding=utf-8
'''
name:chenyang
email: 2898891726@qq.com
date : 2018-09-11
class : aid
introduce: chatroom server
env: python3
'''
from socket import *
import os,sys
import time
# 登录判断
def do_login(s,name,user,addr):
    if (name in user) or name=='管理员':
        s.sendto('该用户已存在'.encode(),addr)
        return
    s.sendto('ok'.encode(),addr)
    msg='\n欢迎%s进入聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
# 插入用户数据
    user[name]=addr
# 说话
def do_chat(s,user,name,text):
    msg = "\n%s 说:%s"%(name,text)
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])
# 退出
def do_quit(s,user,name):
    msg ='\n'+name+'退出聊天室'
    for i in user:
        if i ==name:
            s.sendto(b'exit',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    del user[name]


# 接收请求
def do_parent(s):
    # 存储结构
    user={}

    while True:
        c,addr=s.recvfrom(1024)
        clist=c.decode().split(' ')
        # 区分请求类类型
        if clist[0]=='l':
           do_login(s,clist[1],user,addr)
        elif clist[0]=='c':
            do_chat(s,user,clist[1],' '.join(clist[2:]))
        elif clist[0]=="Q":
            do_quit(s,user,clist[1])

#管理员喊话 
def do_child(s,addr):
    while True:
        msg=input('管理员')
        msg='c 管理员 '+msg
        s.sendto(msg.encode(),addr)


#创建网络创建进程调用功能函数
def main():
    #sever address
    ADDR=('0.0.0.0',7898)
    #创建套接字
    s=socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    #创建一个单独的进程处理管理员喊话
    pid = os.fork()
    if pid <0:
        sys.exit()
    elif pid==0:
        do_child(s,ADDR)
    else:
        do_parent(s)

if __name__=="__main__":
    main()