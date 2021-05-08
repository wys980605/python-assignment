#2. 计算这3名学生的成绩平均分，并进行显示。
class student:
    def __init__(self,number,name,score):
        self.num=number
        self.name=name
        self.score=score
    def __str__(self):
        return "name:{} student number:{} score:{}".format(self.name,self.num,self.score)

A=student('001','aaa',95)
B=student('002','bbb',98)
C=student('003','ccc',94)

print(A)
print(B)
print(C)

print('The average score is {:.2f}'.format((A.score+B.score+C.score)/3)


