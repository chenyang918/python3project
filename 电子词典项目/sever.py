from  socket import *
import os,sys
import signal,time
from file_mysql_func import Mysql_s
Addr=('',6666)
class Fs(Mysql_s):
    def __init__(self,c):
        self.c=c
        super().__init__()
    def client_handler(self):
        # try:
        while True:
            sin=self.c.recv(1024).decode()
            print(sin)
            if sin=='q':
                sys.exit('客户端退出')     
            elif sin=='sin':
                data=self.c.recv(1024).decode()
                data=data.split('#')
                data1=self.sign_in(data)
                if data1:
                    self.c.send('ok'.encode())                      
                else:
                    self.c.send('no'.encode())
            elif sin=='lin':
                data=self.c.recv(1024).decode()
                data=data.split('#')
                data1=self.line_in(data)
                if data1:
                    self.c.send('ok'.encode())
                else:
                    self.c.send('no'.encode())
            elif sin=='f':
                while True:
                    data=self.c.recv(1024).decode()
                    data=data.split('#')
                    if data[0]=='q':
                        break
                    data1=self.f_word(data)
                    if len(data1)!=0:
                        data2='ok'+'#'+data1
                        self.c.send(data2.encode())
                        break
                    else:
                        self.c.send('no#'.encode())
                        break
            elif sin=='h':
                while True:
                    data=self.c.recv(1024).decode()
                    data=data.split('#')
                    if data[0]=='q':
                        break
                    data1=self.f_history(data)
                    if len(data1)!=0:
                        data2='ok'+'#'+str(data1)
                        self.c.send(data2.encode())
                        break
                    else:
                        self.c.send('no#'.encode())
                        break
        # except Exception as e:
        #     print('error',e)

# 创建套接字
def main():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(Addr)
    s.listen(5)
    print('等待连接%s'%os.getpid())
    # 在父进程中忽略子进程状态　子进程退出自动由系统处理避免僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while  True:
        try:
            c,addr=s.accept()
        except KeyboardInterrupt:
            sys.exit('服务器退出')
        except Exception as e:
            input()
            print('error',e)
            continue
        else:
            print('已经连接客户端')
        # 为客户端创建新的进程处理请求
            pid=os.fork()
            if pid==0:
                s.close()
                f=Fs(c)
                f.client_handler()
            # 无论是父进程还是失败都继续等待下个客户连接
            else:

                c.close()
                continue
if __name__=="__main__":
    main()