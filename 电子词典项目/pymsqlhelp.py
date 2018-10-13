from pymysql import connect
class MysqlHelp:
    def __init__(self,database,host='localhost',user='root',password='123456',charset='utf8',port=3306):
        self.port=port
        self.charset=charset
        self.user=user
        self.host=host
        self.password=password
        self.database=database
    def open(self):
        
        self.conn=connect(host=self.host,user=self.user,password=self.password,charset=self.charset,port=self.port,database=self.database)

        self.cur= self.conn.cursor()
    def close(self):
        self.conn.close()
        self.cur.close()
        #写改删
    def workon(self,sql,l=[]):
        self.open()
        try:

            self.cur.execute(sql,l)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        self.close()
        #查
    def getall(self,sql,l=[]):
        data=[]
        self.open()
        try:

            self.cur.execute(sql,l)
            print('ok')
            data=self.cur.fetchall()   
        except Exception as e:
            self.conn.rollback()
            print(e)
        
        else:
            self.close()
            return data















