from  socket import *
import os,sys
import signal,time
host=''
port=8888
Addr=(host,port)


class Fs:
    def __init__(self,c):
        self.c=c
    def cfile(self):
        l=os.listdir('.')
        l1=[]
        for i in l:
            if os.path.isfile(i) and i[0]!='.':
                l1.append(i)
            else:
                continue
        file='#'.join(l1)
        if not l1:
            self.c.send('空文件'.encode())
            return
        else:
            self.c.send('ok'.encode())
            time.sleep(1)
        
        self.c.send(file.encode())
    def getfilename(self):
        l=os.listdir('.')
        l1=[]
        for i in l:
            if os.path.isfile(i) and i[0]!='.':
                l1.append(i)
            else:
                continue
        file='#'.join(l1)
        return file

    def getfile(self):

        file=self.getfilename()
        self.c.send(file.encode())
        x=self.c.recv(1024)#收到文件名字序列号
        print(x.decode())
        y=file.split('#')[int(x.decode())]
        f=open(y,'rb')
        
        while True:
            data=f.read(1024)
            if not data:
                time.sleep(0.1)
                self.c.send('q'.encode())
                f.close()
                print('完成')
                break
            self.c.send(data)
    def upfile(self):
        
        filename=self.c.recv(1024).decode()
        print(filename)
        f=open(filename,'wb')
        print('等待接收')
        while True:
            data=self.c.recv(1024)
            print('接收成功')
            print(data.decode())
            if data.decode()=='q':
                f.close()
                print('完成')
                break
            f.write(data)




    #处理客户端请求

    def client_handler(self):
        print('处理子进程的请求',self.c.getpeername())
        try:
            while True:
                data =self.c.recv(1024)
                print(data.decode())
                if not data.decode():
                    sys.exit('客户退出')
                    self.c.close()
                elif data.decode()=='c':
                    print('收到命令')
                    self.cfile()
                elif data.decode()=='d':
                    print('收到命令')
                    self.getfile()
                elif data.decode()=='u':
                    print('收到命令')
                    self.upfile()
                elif data.decode()=='q':
                    break
                else:
                    self.c.send('错误'.encode())
        except (KeyboardInterrupt,SyntaxError):
            sys.exit('客户退出')
        except Exception as e:
            print(e) 
        self.c.close()
        sys.exit()

# 创建套接字
def main():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(Addr)
    s.listen(3)
    print('等待连接%s'%os.getpid())
    # 在父进程中忽略子进程状态　子进程退出自动由系统处理避免僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while  True:
        try:
            c,addr=s.accept()
        except KeyboardInterrupt:
            sys.exit('服务器退出')
        except Exception as e:
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