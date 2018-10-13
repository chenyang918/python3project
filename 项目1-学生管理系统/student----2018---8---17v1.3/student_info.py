# -*- coding: utf-8 -*-


def input_student():
    l = []
    while True:

        d = {}

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

        d['name'] = x
        d['age'] = y
        d['score'] = z
        l.append(d)

    return l


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

def read_data():
    try:

        l1=[]
        f=open('info.txt','r')
        l=f.readlines()
        f.close()
        for line in l:
            s=line.strip()
            name,age,score=s.split(' ')
            age=int(age)
            score=int(score)
            l1.append({'name':name,'age':age,'score':score})
    except OSError:
        print('读取文件失败')
    return l1
def save_data(l):
    try:
        f=open('info.txt','w')
        for i in l :
            f.write(i['name'])
            f.write(' '+str(i['age']))
            f.write(' '+str(i['score'])+'\n')
        f.close()
    except OSError:
        print('打开失败')



# 待完善


# def find_student(l):
#     while True:
#         x = input('请输入要查找学生的名字')
#         for i in l:
#             if i[x] in i:
#                 output_student(i)
#             else:
#                 print('不存在')
#                 break
