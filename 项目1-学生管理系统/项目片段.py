# # -*- coding: utf-8 -*-
# '''from __future__ import unicode_literals'''
# 2. 学生信息管理项目
#     输入任意个学生的姓名, 年龄, 成绩.每个学生的信息存入一个字典内, 然后放入到列表中
#         (每个学生需要手动输入)
#     如:
#         请输入姓名:
#             tarena
#         请输入年龄:
#             20
#         请输入成绩:
#             99
#         请输入姓名:
#             name2
#         请输入年龄:
#             30
#         请输入成绩:
#             88
#         请输入姓名:
#             < 回车 > 结束输入
#     形成内部存储格式如下:
#         [{'name': 'tarena', 'age': 20, 'score': 99},
#             {'name': name2, 'age': 30, 'score': 88}]
#     1 打印出存有学生信息的字典的列表
# l = []
# while True:

#     d = {}

#     x = input('name')
#     if x == '':
#         break
#     y = int(input('age'))
#     z = int(input('score'))
#     d['name'] = x
#     d['age'] = y
#     d['score'] = z
#     l.append(d)
# print(l)
# print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
# print('|', 'name'.center(30), '|', 'age'.center(
#     20), '|', 'score'.center(20), '|', sep='')
# print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
# for i in range(len(l)):
#     print('|', (l[i]['name']).center(30), '|', str(l[i]['age']).center(
#         20), '|', str(l[i]['score']).center(20), '|', sep='')
# print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')


# 用函数封装后：


# def input_student():
#     l = []
#     while True:

#         d = {}

#         x = input('name')
#         if x == '':
#             break
#         y = int(input('age'))
#         z = int(input('score'))
#         d['name'] = x
#         d['age'] = y
#         d['score'] = z
#         l.append(d)
#     return l


# def output_student(l):
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     print('|', 'name'.center(30), '|', 'age'.center(
#         20), '|', 'score'.center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     for i in range(len(l)):
#         print('|', (l[i]['name']).center(30), '|', str(l[i]['age']).center(
#             20), '|', str(l[i]['score']).center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
# l = input_student()
# print(l)
# output_student(l)


# name可以是中文了


# def input_student():

#     while True:

#         d = {}

#         x = input('name')

#         if x == '':

#             break
#         y = int(input('age'))
#         z = int(input('score'))
#         g = get_chinese_char_count(x)
#         d['name'] = x
#         d['age'] = y
#         d['score'] = z
#         l.append(d)
#     l.append(g)
#     return l


# def output_student(l):

#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     print('|', 'name'.center(30), '|', 'age'.center(
#         20), '|', 'score'.center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     for i in range(len(l) - 1):
#         print('|', (l[i]['name']).center(30 - l[-1]), '|', str(l[i]['age']).center(
#             20), '|', str(l[i]['score']).center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')


# def get_chinese_char_count(s):
#     l = ''

#     for i in s:
#         if ord(i) > 127:
#             l += i
#     return len(l)


# 版本v2


# def input_student(l):
#     while True:

#         d = {}

#         x = input('name')

#         if x == '':

#             break
#         y = int(input('age'))
#         z = int(input('score'))
#         g = get_chinese_char_count(x)
#         d['name'] = x
#         d['age'] = y
#         d['score'] = z
#         l.append(d)
#     l.append(g)
#     return l


# def output_student(l):

#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     print('|', 'name'.center(30), '|', 'age'.center(
#         20), '|', 'score'.center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     for i in range(len(l) - 1):
#         print('|', (l[i]['name']).center(30 - l[-1]), '|', str(l[i]['age']).center(
#             20), '|', str(l[i]['score']).center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')


# def get_chinese_char_count(s):
#     l = ''

#     for i in s:
#         if ord(i) > 127:
#             l += i
#     return len(l)


# def cao_jiemian():
#     print('+', '-' * 30, '-', '-' * 20, '-', '-' * 20, '+', sep='')
#     print('|', '　1)  添加学生信息', ' ' * 54, '|', sep='')
#     print('|', '　2)  显示学生信息', ' ' * 54, '|', sep='')
#     print('|', '　3)  删除学生信息', ' ' * 54, '|', sep='')
#     print('|', '　4)  修改学生信息', ' ' * 54, '|', sep='')
#     print('|', '　5)  查找学生信息', ' ' * 54, '|', sep='')
#     print('|', '　q)  退出', ' ' * 62, '|', sep='')
#     print('+', '-' * 30, '-', '-' * 20, '-', '-' * 20, '+', sep='')


# def del_student(l):
#     a = True
#     if a == True:
#         l.pop()
#         a = False

#     print(l)  # jian
#     a = len(l)
#     q = 0
#     while True:
#         x = input('请输入要删除学生的名字')

#         for i in l:
#             if i['name'] == x:
#                 l.pop(l.index(i))
#                 print('删除成功')
#         else:
#             if len(l) == a:
#                 print('输入错误请重新输入')
#                 q += 1
#                 if q == 3:
#                     break
#             else:
#                 break
#     return l


# def change_student(l):
#     print(l)  # jian
#     a = len(l)
#     q = 0
#     while True:
#         x = input('请输入要修改学生的名字')

#         for i in l:
#             if i['name'] == x:
#                 x1 = input('请输入要修改的项目名')
#                 if x1 == 'age':
#                     x2 = int(input('请输入新的age'))
#                     l[l.index(i)]['age'] = x2
#                     print('修改成功')
#                 elif x1 == 'name':
#                     x3 = int(input('请输入新的name'))
#                     l[l.index(i)]['name'] = x2
#                     print('修改成功')
#                 elif x1 == 'score':
#                     x4 = int(input('请输入新的score'))
#                     l[l.index(i)]['score'] = x2
#                     print('修改成功')
#                 else:
#                     break
#     return l


# def find_student(l):
#     li = []
#     while True:
#         x = input('请输入要查找学生的名字')
#         for i in l:
#             if i[x] in i:
#                 li.append(l.index(i))

#     return l


# def main():
#     l = []

#     while True:
#         cao_jiemian()
#         x = input('请选择　')
#         if x == 'q':
#             break
#         elif x == '1':
#             input_student(l)
#         elif x == '2':
#             output_student(l)
#         elif x == '3':
#             del_student(l)
#         elif x == '4':

#             pass
#         elif x == '5':
#             pass


# main()


# 版本v2 - 1


# def input_student():
#     l = []
#     while True:

#         d = {}

#         x = input('name')

#         if x == '':

#             break
#         y = int(input('age'))
#         z = int(input('score'))

#         d['name'] = x
#         d['age'] = y
#         d['score'] = z
#         l.append(d)

#     return l


# def get_chinese_char_count(s):
#     l = ''

#     for i in s:
#         if ord(i) > 127:
#             l += i
#     return len(l)


# def output_student(l):

#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     print('|', 'name'.center(30), '|', 'age'.center(
#         20), '|', 'score'.center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     for i in range(len(l)):
#         g = get_chinese_char_count(l[i]['name'])
#         print('|', (l[i]['name']).center(30 - g), '|', str(l[i]['age']).center(
#             20), '|', str(l[i]['score']).center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')


# def cao_jiemian():
#     print('+', '-' * 30, '-', '-' * 20, '-', '-' * 20, '+', sep='')
#     print('|', '　1)  添加学生信息', ' ' * 54, '|', sep='')
#     print('|', '　2)  显示学生信息', ' ' * 54, '|', sep='')
#     print('|', '　3)  删除学生信息', ' ' * 54, '|', sep='')
#     print('|', '　4)  修改学生信息', ' ' * 54, '|', sep='')
#     print('|', '　5)  查找学生信息', ' ' * 54, '|', sep='')
#     print('|', '　q)  退出', ' ' * 62, '|', sep='')
#     print('+', '-' * 30, '-', '-' * 20, '-', '-' * 20, '+', sep='')


# def del_student(l):

#     print(l)  # jian
#     a = len(l)
#     q = 0
#     while True:
#         x = input('请输入要删除学生的名字')

#         for i in l:
#             if i['name'] == x:
#                 l.pop(l.index(i))
#                 print('删除成功')
#         else:
#             if len(l) == a:
#                 print('输入错误请重新输入')
#                 q += 1
#                 if q == 3:
#                     break
#             else:
#                 break
#     return l


# def change_student(l):

#     a = len(l)
#     q = 0
#     while True:
#         x = input('请输入要修改学生的名字')
#         if x == '':
#             break

#         for i in l:
#             if i['name'] == x:
#                 x1 = input('请输入要修改的项目名')
#                 if x1 == 'age':
#                     x2 = int(input('请输入新的age'))
#                     l[l.index(i)]['age'] = x2
#                     print('修改成功')
#                 elif x1 == 'name':
#                     x3 = int(input('请输入新的name'))
#                     l[l.index(i)]['name'] = x2
#                     print('修改成功')
#                 elif x1 == 'score':
#                     x4 = int(input('请输入新的score'))
#                     l[l.index(i)]['score'] = x2
#                     print('修改成功')
#                 else:
#                     break
#     return l

# # 待完善


# def find_student(l):
#     while True:
#         x = input('请输入要查找学生的名字')
#         for i in l:
#             if i[x] in i:
#                 output_student(i)
#             else:
#                 print('不存在')
#                 break


# def main():
#     l = []

#     while True:
#         cao_jiemian()
#         x = input('请选择　')
#         if x == 'q':
#             break
#         elif x == '1':
#             l += input_student()
#         elif x == '2':
#             output_student(l)
#         elif x == '3':
#             l = del_student(l)
#         elif x == '4':
#             l = change_student(l)
#         elif x == '5':
#             pass
# main()
# 版本v3
# def input_student():
#     l = []
#     while True:

#         d = {}

#         x = input('name')

#         if x == '':

#             break
#         y = int(input('age'))
#         z = int(input('score'))

#         d['name'] = x
#         d['age'] = y
#         d['score'] = z
#         l.append(d)

#     return l


# def get_chinese_char_count(s):
#     l = ''

#     for i in s:
#         if ord(i) > 127:
#             l += i
#     return len(l)


# def output_student(l):

#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     print('|', 'name'.center(30), '|', 'age'.center(
#         20), '|', 'score'.center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
#     for i in range(len(l)):
#         g = get_chinese_char_count(l[i]['name'])
#         print('|', (l[i]['name']).center(30 - g), '|', str(l[i]['age']).center(
#             20), '|', str(l[i]['score']).center(20), '|', sep='')
#     print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')


# def cao_jiemian():
#     print('+', '-' * 30, '-', '-' * 20, '-', '-' * 20, '+', sep='')
#     print('|', '　1)  添加学生信息', ' ' * 54, '|', sep='')
#     print('|', '　2)  显示学生信息', ' ' * 54, '|', sep='')
#     print('|', '　3)  删除学生信息', ' ' * 54, '|', sep='')
#     print('|', '　4)  修改学生信息', ' ' * 54, '|', sep='')
#     print('|', '　5)  查找学生信息', ' ' * 54, '|', sep='')
#     print('|', '　6)  成绩高低排序', ' ' * 54, '|', sep='')
#     print('|', '　7)  成绩低高排序', ' ' * 54, '|', sep='')
#     print('|', '　8)  年龄高低排序', ' ' * 54, '|', sep='')
#     print('|', '　9)  年龄低高排序', ' ' * 54, '|', sep='')
#     print('|', '　q)  退出', ' ' * 62, '|', sep='')
#     print('+', '-' * 30, '-', '-' * 20, '-', '-' * 20, '+', sep='')


# def del_student(l):

#     print(l)  # jian
#     a = len(l)
#     q = 0
#     while True:
#         x = input('请输入要删除学生的名字')

#         for i in l:
#             if i['name'] == x:
#                 l.pop(l.index(i))
#                 print('删除成功')
#         else:
#             if len(l) == a:
#                 print('输入错误请重新输入')
#                 q += 1
#                 if q == 3:
#                     break
#             else:
#                 break
#     return l


# def change_student(l):

#     a = len(l)
#     q = 0
#     while True:
#         x = input('请输入要修改学生的名字')
#         if x == '':
#             break

#         for i in l:
#             if i['name'] == x:
#                 x1 = input('请输入要修改的项目名')
#                 if x1 == 'age':
#                     x2 = int(input('请输入新的age'))
#                     l[l.index(i)]['age'] = x2
#                     print('修改成功')
#                 elif x1 == 'name':
#                     x3 = int(input('请输入新的name'))
#                     l[l.index(i)]['name'] = x2
#                     print('修改成功')
#                 elif x1 == 'score':
#                     x4 = int(input('请输入新的score'))
#                     l[l.index(i)]['score'] = x2
#                     print('修改成功')
#                 else:
#                     break
#     return l

# # 待完善


# def find_student(l):
#     while True:
#         x = input('请输入要查找学生的名字')
#         for i in l:
#             if i[x] in i:
#                 output_student(i)
#             else:
#                 print('不存在')
#                 break


# def score_hl(d):
#     return d['score']
# def score_lh(d):
#     return d['score']
# def age_hl(d):
#     return d['age']
# def age_lh(d):
#     return d['age']


# def main():
#     l = []

#     while True:
#         cao_jiemian()
#         x = input('请选择　')
#         if x == 'q':
#             break
#         elif x == '1':
#             l += input_student()
#         elif x == '2':
#             output_student(l)
#         elif x == '3':
#             l = del_student(l)
#         elif x == '4':
#             l = change_student(l)
#         elif x == '5':

#             pass
#         elif x=='6':
#             li=sorted(l,key=score_hl,reverse=True)
#             output_student(li)
#         elif x=='7':
#             li=sorted(l,key=score_lh)
#             output_student(li)
#         elif x=='8':
#             li=sorted(l,key=age_hl,reverse=True)
#             output_student(li)
#         elif x=='9':
#             li=sorted(l,key=age_lh)
#             output_student(li)


# main()
版本v4
#   3. 改写之前的学生信息的程序,要求添加四个功能:
#       | 5)  按学生成绩高-低显示学生信息 |
#       | 6)  按学生成绩低-高显示学生信息 |
#       | 7)  按学生年龄高-低显示学生信息 |
#       | 8)  按学生年龄低-高显示学生信息 |


def input_student():
    l = []
    while True:

        d = {}

        x = input('name')

        if x == '':

            break
        y = int(input('age'))
        z = int(input('score'))

        d['name'] = x
        d['age'] = y
        d['score'] = z
        l.append(d)

    return l


def get_chinese_char_count(s):
    l = ''

    for i in s:
        if ord(i) > 127:
            l += i
    return len(l)


def output_student(l):

    print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
    print('|', 'name'.center(30), '|', 'age'.center(
        20), '|', 'score'.center(20), '|', sep='')
    print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
    for i in range(len(l)):
        g = get_chinese_char_count(l[i]['name'])
        print('|', (l[i]['name']).center(30 - g), '|', str(l[i]['age']).center(
            20), '|', str(l[i]['score']).center(20), '|', sep='')
    print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')


def cao_jiemian():
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


def del_student(l):

    print(l)  # jian
    a = len(l)
    q = 0
    while True:
        x = input('请输入要删除学生的名字')

        for i in l:
            if i['name'] == x:
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


def change_student(l):

    a = len(l)
    q = 0
    while True:
        x = input('请输入要修改学生的名字')
        if x == '':
            break

        for i in l:
            if i['name'] == x:
                x1 = input('请输入要修改的项目名')
                if x1 == 'age':
                    x2 = int(input('请输入新的age'))
                    l[l.index(i)]['age'] = x2
                    print('修改成功')
                elif x1 == 'name':
                    x3 = int(input('请输入新的name'))
                    l[l.index(i)]['name'] = x2
                    print('修改成功')
                elif x1 == 'score':
                    x4 = int(input('请输入新的score'))
                    l[l.index(i)]['score'] = x2
                    print('修改成功')
                else:
                    break
    return l

# 待完善


def find_student(l):
    while True:
        x = input('请输入要查找学生的名字')
        for i in l:
            if i[x] in i:
                output_student(i)
            else:
                print('不存在')
                break


def score_hl(l):
    def get_score(d):
        return d['score']
    l1 = sorted(l, key=get_score, reverse=True)
    output_student(l1)


def score_lh(l):
    def get_score(d):
        return d['score']
    l2 = sorted(l, key=get_score)
    output_student(l2)


def age_hl(l):
    def get_age(d):
        return d['age']
    l3 = sorted(l, key=get_age, reverse=True)
    output_student(l3)


def age_lh(l):
    def get_age(d):
        return d['age']
    l4 = sorted(l, key=get_age)
    output_student(l4)


def main():
    l = []

    while True:
        cao_jiemian()
        x = input('请选择　')
        if x == 'q':
            break
        elif x == '1':
            l += input_student()
        elif x == '2':
            output_student(l)
        elif x == '3':
            l = del_student(l)
        elif x == '4':
            l = change_student(l)
        elif x == '5':

            pass
        elif x == '6':
            score_hl(l)
        elif x == '7':
            score_lh(l)
        elif x == '8':
            age_hl(l)
        elif x == '9':
            age_lh(l)


main()
