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
            except ValueError:
                print('输入类型错误，请重新输入')
                y = int(input('age'))
                break
            else:
                break
        while True:   
            try:
                z = int(input('score'))
            except ValueError:
                print('输入类型错误，请重新输入')
                z = int(input('score'))
                break
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
