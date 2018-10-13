class Student:
  def __init__(self,name,age,score):
    self.__name=name
    self.__age=age
    self.__score=score
  def get_info(self):
    return (self.__name,self.__age,self.__score)
  def get_score(self):
    return self.__score
  def get_age(self):
    return self.__age
  def get_name(self):
    return self.__name
  def set_score(self,x):
    self.__score=x
    return self.__score
  def set_age(self,y):
    self.__age=y
    return self.__age
  def set_name(self,z):
    self.__name=z
    return self.__name
