# from socket import * 
# from select import *
# import os,sys 
# import time
# # 创建套字节对象
# s=socket()
# # 关闭套字节就立即释放端口
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# name=input('昵称')
# # 绑定Ｉｐ端口号
# s.connect(('127.0.0.1',5555))
# # 开启监听ＩＰ是否有人链接
# while True:
#     # 初始化名字
#     while True:
#         s.send(name.encode())
#         data=s.recv(1024)
#         if data.decode()=='昵称重复':
#             name=input('昵称')
#             continue
#         else:
#             break
    


#     x_f=input('消息')
#     data1=s.send(x_f.encode())
#     if not data1:
#         break
#     pid=os.fork()
#     if pid<0:
#         print('error')
#     elif pid==0:
#         p=os.fork()
#         if p==0:
#             data2=s.recv(1024)
#             print(data2.decode())
#         else:
#             os._exit(0)
#     else:
#         os.wait()
#         continue




