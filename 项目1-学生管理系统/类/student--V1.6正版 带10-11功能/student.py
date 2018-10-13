class Student:
  def __init__(self,name,age,score):
    self.name=name
    self.age=age
    self.score=score
  def get_info(self):
    return (self.name,self.age,self.score)
  def get_score(self):
    return self.score
  def get_age(self):
    return self.age
  def get_name(self):
    return self.name
  def set_score(self,x):
    self.score=x
    return self.score
  def set_age(self,y):
    self.age=y
    return self.age
  def set_name(self,z):
    self.name=z
    return self.name
