from  socket import *
import time
class Fs:
    def __init__(self,s):
        self.s=s

        
    def checkf(self):
        # 发送请求
        print('查看文件')
        self.s.send('c'.encode())
        data=self.s.recv(1024)
        if  data.decode()=='ok':
            data1=self.s.recv(4096).decode()
            files=data1.split('#')
            for i in files:
                print(i)
        else:
            print(data.decode())
    def dload(self):
        self.s.send('d'.encode())
        file=self.s.recv(4096)
        j=0
        for i in file.decode().split('#'):
            print(j,i)
            j+=1
        z=input('请选择要下载的文件序号')
        x=input('要存文件名字为')
        self.s.send(z.encode())
        f=open(x,'wb')
        while True:
            data=self.s.recv(1024)
            if data.decode().strip()=='q':
                f.close()
                print('下载完成')
                break
            f.write(data)

    def upload(self):
        self.s.send('u'.encode())
        x=input('请输入上传路径')
        y=x.split('/')
        filename=y.pop()
        self.s.send(filename.encode())
        time.sleep(0.2)
        f=open(x,'rb')
        while True:
            data=f.read(1024)
            if not data:
                time.sleep(1)
                self.s.send('q'.encode())
                print('上传完成')
                f.close()
                break
            self.s.send(data)
            print('上传完成')
    def f_quit(self):
        self.s.send('q'.encode())


def main():
    x=input('ip')
    y=int(input('port'))
    addr=(x,y)
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    try:
        s.connect(addr)
    except:
        print('连接失败')
        return
    f=Fs(s)
    while True:
        print("****************' 功能选项'***********************")
        print("****************'１查看文件'**********************")
        print("****************'２下载文件'**********************")
        print("****************'３上传文件'**********************")
        print("****************'４退出网盘'**********************")

        x=int(input('请输入功能选项'))
        if x == 1:
            f.checkf()
        elif x == 2:
            f.dload()
        elif x == 3:
            print('上传')
            f.upload()
        elif x==4:
            f.f_quit()
            s.close()
            break

if __name__=='__main__':
    main()