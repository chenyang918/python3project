import pymongo
class Findword:
    def __init__(self):
        pass
    def find_word(self,word):
        try:

            cnn = pymongo.MongoClient('localhost', 27017)
            myset = cnn.dictor.wdata
            # myset.insert({'wordid':word,'wordname':wordis})
            data = myset.find_one({'wordid':word}, {'_id': 0, 'wordname': 1}) 

            data=data['wordname'].strip()
        except Exception as e:
            print(e)
            data='没有查到'
        return data
# 将数据写入数据库
# import pymongo
# f = open('dict.txt', 'rt')
# cnn = pymongo.MongoClient('localhost', 27017)
# myset = cnn.dictor.wdata
# i=0
# while True:
#     i+=1
#     try:
#         data = f.readline()
#         if not data:
#             break
#         l = data.split(' ')
#         word = l.pop(0)
#         wordis = ''.join(l)
#         wordis = wordis.lstrip()
#         myset.insert({'wordid':word,'wordname':wordis})
#     except Exception as e:
#         print(e)
#         continue
# print(i)
# f.close()
# 从MongoDB中查找数据