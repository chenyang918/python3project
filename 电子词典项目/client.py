from  socket import *
import os,sys,re
import signal,time
class Fs:
    def __init__(self,s):
        self.s=s
        self.username=''
    def sign_in(self):
        while True:
            self.s.send('sin'.encode())
            username=input('输入用户名字')
            password=input('输入用户密码')
            data=username+'#'+password
            self.s.send(data.encode())
            sin=self.s.recv(1024).decode()
            if sin=='ok':
                print('注册成功')
                self.username=username
                return True
            else:
                print('用户名字错误或者失败请重试')
                return False 
    def line_in(self):
        while True:
            self.s.send('lin'.encode())
            username=input('输入用户名字')
            password=input('输入用户密码')
            data=username+'#'+password
            self.s.send(data.encode())
            sin=self.s.recv(1024).decode()
            if sin=='ok':
                print('登录成功')
                self.username=username
                return True
            else:
                print('用户名字错误或密码错误请重试')
                return False 
    def f_word(self):
        while True:
            self.s.send('f'.encode())
            x=input('请输入单词')
            data=self.username+'#'+x
            if x=='##':
                self.s.send("q#q".encode())
                break
            else:
                self.s.send(data.encode())
                data=self.s.recv(1024).decode()
                data=data.split('#')
                if data[0]=='ok':
                    print('单词的意思是',data[1])
                else:
                    print('未找到单词')


    def f_history(self):
        print('history')
        while True:
            self.s.send('h'.encode())
            x=input('按任意键看历史记录输入##退出查看')
            data=self.username+'#'
            if x=='##':
                self.s.send("q#q".encode())
                break
            else:
                self.s.send(data.encode())
                data=self.s.recv(1024).decode()
                data=data.split('#')
                if data[0]=='ok':
                    print(l)
                    l=re.findall("('.+),?",data[1][1:-2])
                    for i in l:
                        print(i)
            
                else:
                    print('no history')
    def er_table(self,sig):
        while sig:
                print("****************' 功能选项'***********************")
                print("****************'  1查找  '**********************")
                print("****************'  ２历史 '**********************")
                print("****************'  3退出  '**********************")
                sin=int(input('请输入功能选项'))
                if sin==1:
                    data=self.f_word()
                elif sin==2:
                    data=self.f_history()
                elif sin==3:
                    break
    def f_quit(self):
        sys.exit('exit client')
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
    print('连接成功')
    while True:
        print("****************'功能选项'***********************")
        print("****************' １注册 '**********************")
        print("****************' ２登录 '**********************")
        print("****************' 3退出  '**********************")
        x=int(input('请输入功能选项'))
        if x==1:
            sin=f.sign_in()
            f.er_table(sin)
        elif x==2:
            print('bei')
            sin=f.line_in()
            f.er_table(sin)  
        elif x==3:
            f.f_quit()
            s.close()
            break

if __name__=='__main__':
    main()