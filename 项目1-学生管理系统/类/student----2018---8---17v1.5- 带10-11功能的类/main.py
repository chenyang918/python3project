# -*- coding: utf-8 -*-
from student_info import Student
def main():
    l2=[]
    l=Student()
    while True:
        l.cao_jiemian()
        x = input('请选择　')
        if x == 'q':
            break
        elif x == '1':
            l2 +=l.input_student()
            print(l2)
        elif x == '2':
            l.output_student(l2)
        elif x == '3':
            l2=l.del_student(l2)
        elif x == '4':
            l2 =l.change_student(l2)
        elif x == '5':
            pass
        elif x == '6':
            l.score_hl(l2)
        elif x == '7':
            l.score_lh(l2)
        elif x == '8':
            l.age_hl(l2)
        elif x == '9':
            l.age_lh(l2)
        elif x == '10':
            l.save_data(l2)
        elif x == '11':
            l2 = l.read_data()

main()
