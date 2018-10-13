from pymsqlhelp import MysqlHelp
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
f=Findword()
class Mysql_s(MysqlHelp):
    def __init__(self):
        super().__init__('wordproject')
    def sign_in(self,data):
        sql='select count(username) from user where username=%s'
        sql1="insert into user(username,password) values(%s,%s)"
        data1=self.getall(sql,data[0:1])
        if data1!=((1,),):
            self.workon(sql1,data)
            return True
        else:
            return False
    def line_in(self,data):
        sql='select count(username) from user where username=%s'
        sql1='select count(password) from user where username=%s'
        data1=self.getall(sql,data[0:1])
        data2=self.getall(sql1,data[0:1])
        if data1==((1,),) and data2==((1,),): 
            return True
        else:
            return False  
    def f_word(self,data):
        data1=f.find_word(data[1])
        print(data1,'查到的单词')
        if len(data1)!=0:
            sql='select id from user where username=%s'
            sql1='insert into history(h_id,word) values(%s,%s)'
            idor=self.getall(sql,data[0:1])
            self.workon(sql1,[idor,data[1]])
            return data1
        else:
            return
    def f_history(self,data):
        if len(data)!=0:
            sql='select id from user where username=%s'
            sql1='select word,h_date from history where h_id=%s'
            idor=self.getall(sql,data[0:1])
            data1=self.getall(sql1,[idor])
            return data1
        else:
            return