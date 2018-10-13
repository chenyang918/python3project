def output_student(l):

    print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
    print('|', 'name'.center(30), '|', 'age'.center(
        20), '|', 'score'.center(20), '|', sep='')
    print('+', '-' * 30, '+', '-' * 20, '+', '-' * 20, '+', sep='')
    for i in l:
        g = get_chinese_char_count(i.get_name())
        print('|', (i.get_name()).center(30 - g), '|', str(i.get_age()).center(
            20), '|', str(i.get_score()).center(20), '|', sep='')
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
def get_chinese_char_count(s):
    l = ''

    for i in s:
        if ord(i) > 127:
            l += i
    return len(l)

def score_hl(l):
    def get_score(d):
        return d.get_score()
    l1 = sorted(l, key=get_score, reverse=True)
    output_student(l1)


def score_lh(l):
    def get_score(d):
        return d.get_score()
    l2 = sorted(l, key=get_score)
    output_student(l2)


def age_hl(l):
    def get_age(d):
        return d.get_score()
    l3 = sorted(l, key=get_age, reverse=True)
    output_student(l3)


def age_lh(l):
    def get_age(d):
        return d.get_score()
    l4 = sorted(l, key=get_age)
    output_student(l4)

