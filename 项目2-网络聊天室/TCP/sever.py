# epoll 方法

# from socket import * 
# from select import *
# import os,sys 
# import time
# i_l=[]
# n_l=[]
# c_l=[]
# n_j=[]
# # 创建套字节对象
# s=socket()
# # 关闭套字节就立即释放端口
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# # 绑定Ｉｐ端口号
# s.bind(('0.0.0.0',5555))
# # 开启监听ＩＰ是否有人链接
# s.listen(5)
# #创建ＩＯ注册监视对象
# p=epoll()
# #创建一个字典来记录链接来套字节使用ＩＯ描述符对ＩＯ操作对象进行标记方便处理
# fdmap ={s.fileno():s}
# #启动ＰＯｌｌ监视链接过来的ＩＯ
# p.register(s,EPOLLIN | EPOLLERR)

# while True:
#     #进行ＩＯ监控
#     events=p.poll()#若有ＩＯ操作则返回套字节对象和ＩＯ描述符
#     for fd,event in events:
#         if fd ==s.fileno():
#         #若是有链接则恢复同意链接且返回套字节对象与Ｉｐ
#             c,addr = fdmap[fd].accept()
#             print(addr)

#             #初始化套接字和IP列表
#             if addr not in i_l:

#                 i_l.append(addr[0])
#                 c_l.append(c)
                



#             #将新的套字节对象加入监视列表
#             p.register(c,EPOLLIN | EPOLLHUP)
#             # 记录新的套字节对象并将其用ＩＯ操作描述符标记存在字典中
#             fdmap[c.fileno()]=c
#         elif event&EPOLLIN:#判断事件是不是ＰＯＬＬＩＮＩＯ操作
#         # 使用描述符调用在字典中的套字节对象进行相应的套字节接收
#             print(c_l)
#             while True:
#                     name=fdmap[fd].recv(1024)
#                     n_j.append(name)
#                     if n_j.count(name)>1:
#                         break

#                     if name.decode() not in n_l:
#                         fdmap[fd].send('昵称没问题'.encode())
#                         n_l.append(name.decode())
#                         break
#                     else:
#                         c.send('昵称重复'.encode())
#                         continue
            



#             data= fdmap[fd].recv(1024)
#             print(data.decode())


#             # 若收到数据为空证明对方不在发送数据了则退去对该ＩＯ描述符的监视　关闭该套字节对象且删除字典中该套字节对象        
#             if not data:
#                 p.unregister(fd)
#                 fdmap[fd].close()
#                 del fdmap[fd]
#             else:
#               # 将收到的消息发给除了fd以外的人
#                 pid= os.fork()
#                 if pid<0:
#                     print('error')
#                 elif pid==0:
#                     pi=os.fork()
#                     if pi==0:
#                         if len(c_l)>1:
#                             for k in fdmap:
#                                 if fdmap[k]==fdmap[fd] and fdmap[k]==fdmap[s.fileno()] :
#                                     continue
#                                 else:
#                                     n_d=c_l.index(fdmap[fd])
#                                     fdmap[k].send(n_l[n_d].encode()+'说'.encode()+data)
#                     else:
#                         os._exit(0)
#                 else:
#                     os.wait()
#
# continue
