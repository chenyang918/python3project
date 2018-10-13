# -*- coding: utf-8 -*-
l=[]
class Student:
    def __init__(self,name='',age=0,score=0):
        self.name = name
        self.age = age
        self.score = score
    def set_score(self, new_score):
        self.score = new_score
    def set_age(self,new_age):
        self.age=new_age
    def input_student(self):
        while True:
            x = input('name')
            if x == '':
                break
            while True:
                try:
                    y = int(input('age'))
                    assert 1 < y < 150
                except ValueError:
                    print('输入类型错误，请重新输入')

                    continue
                except AssertionError:
                    print('输入范围错误，请重新输入')
                    continue
                else:
                    break
            while True:
                try:
                    z = int(input('score'))
                    assert 1 < z < 100
                except ValueError:
                    print('输入类型错误，请重新输入')

                    continue
                except AssertionError:
                    print('输入范围错误，请重新输入')

                    continue
                else:
                    break
            l.append(Student(x,y,z))
        return l
       

    def del_student(self, l):

        print(l)  # jian
        a = len(l)
        q = 0
        while True:
            x = input('请输入要删除学生的名字')

            for i in l:
                if i.name== x:
                    l.pop(l.index(i))
                    print('删除成功')
            else:
                if len(l) == a:
                    print('输入错误请重新输入')
                    q += 1
                    if q == 3:
                        break
                else:
                    break
        return l

    def change_student(self, l):

        a = len(l)
        q = 0
        while True:
            x = input('请输入要修改学生的名字')
            if x == '':
                break

            for i in l:
                if i.name == x:
                    x1 = input('请输入要修改的项目名')
                    if x1 == 'age':
                        x2 = int(input('请输入新的age'))
                        i.age = x2
                        print('修改成功')
                    elif x1 == 'name':
                        x3 = int(input('请输入新的name'))
                        i.name= x2
                        print('修改成功')
                    elif x1 == 'score':
                        x4 = int(input('请输入新的score'))
                        i.score = x2
                        print('修改成功')
                    else:
                        break
        return l

    def read_data(self):
        try:

            l1 = []
            f = open('info.txt', 'r')
            l = f.readlines()
            f.close()
            for line in l:
                s = line.strip()
                name, age, score = s.split(' ')
                age = int(age)
                score = int(score)
                l1.append(Student(name,age,score))
        except OSError:
            print('读取文件失败')
        return l1

    def save_data(self, l):
        try:
            f = open('info.txt', 'w')
            for i in l:
                f.write(i.name)
                f.write(' ' + str(i.age))
                f.write(' ' + str(i.score) + '\n')
            f.close()
        except OSError:
            print('打开失败')
    def output_student(self, l):
        print(l)


        print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
        print('|', 'name'.center(30), '|', 'age'.center(
            20), '|', 'score'.center(20), '|', sep='')
        print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
        for i in l:
            g = self.get_chinese_char_count(i.name)
            print('|', (i.name).center(30 - g), '|', str(i.age).center(
                20), '|', str(i.score).center(20), '|', sep='')
        print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')

    def cao_jiemian(self):
        print('+', '-' * 30, '-', '-' * 20, '-', '-' * 20, '+', sep='')
        print('|', '　1)  添加学生信息', ' ' * 54, '|', sep='')
        print('|', '　2)  显示学生信息', ' ' * 54, '|', sep='')
        print('|', '　3)  删除学生信息', ' ' * 54, '|', sep='')
        print('|', '　4)  修改学生信息', ' ' * 54, '|', sep='')
        print('|', '　5)  查找学生信息', ' ' * 54, '|', sep='')
        print('|', '　6)  成绩高低排序', ' ' * 54, '|', sep='')
        print('|', '　7)  成绩低高排序', ' ' * 54, '|', sep='')
        print('|', '　8)  年龄高低排序', ' ' * 54, '|', sep='')
        print('|', '　9)  年龄低高排序', ' ' * 54, '|', sep='')
        print('|', '　q)  退出', ' ' * 62, '|', sep='')
        print('+', '-' * 30, '-', '-' * 20, '-', '-' * 20, '+', sep='')

    def get_chinese_char_count(self, s):
        l = ''

        for i in s:
            if ord(i) > 127:
                l += i
        return len(l)

    def score_hl(self, l):
        def get_score(d):
            return d.score
        l1 = sorted(l, key=get_score, reverse=True)
        self.output_student(l1)

    def score_lh(self, l):
        def get_score(d):
            return d.score
        l2 = sorted(l, key=get_score)
        self.output_student(l2)

    def age_hl(self, l):
        def get_age(d):
            return d.age
        l3 = sorted(l, key=get_age, reverse=True)
        self.output_student(l3)

    def age_lh(self, l):
        def get_age(d):
            return d.age
        l4 = sorted(l, key=get_age)
        self.output_student(l4)
