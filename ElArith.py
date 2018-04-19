# -*- coding:utf-8 -*-
#author:jinwei
#date:2018/04/19
#what:Elementary arithmetic

import random
from fractions import Fraction


#四则运算类
class ElArith():
    def __init__(self,):#初始化
        self.op = ['+', '-', '×', '÷', '/']
        self.question = ''


    #随机生成四则运算问题
    def getQustion(self):
        self.lens = random.randint(2, 9)
        self.teop = ''
        self.tstr = []
        for i in range(self.lens):
            if self.teop == '÷':
                self.tint = random.randint(1, 8)
                self.teop = random.choice(self.op)
            elif self.teop == '/':
                self.tint = random.randint(self.tint+1, 9)
                self.teop = random.choice(self.op[:-1])
            else:
                self.tint = random.randint(0, 8)
                self.teop = random.choice(self.op)
            self.tstr.append(str(self.tint))
            self.tstr.append(self.teop)
        self.tstr[-1] = '='
        self.tstr = ''.join(self.tstr)
        self.question = self.tstr
        return self.tstr

    #求解算式答案
    def getAnswer(self, question):
        rpn = self.toRpn(question[:-1])
        the_ans = self.sloveRpn(rpn)
        print('question is :{0}'.format(self.question))
        my_ans = input()

        if str(the_ans) == my_ans :
            print('Your answer is right !')
            return True
        else:
            print('Your answer is wrong !',end='')
            print('The right answer is :{0}'.format(str(the_ans)) )
            return False

    #算式转换形式
    def toRpn(self, question):
        self.stack = []
        s = ''
        for x in question:
            if x != '+' and x != '-' and x != '×' and x != '÷' and x != '/':
                s += x  #若为数字，直接输出
            else:  # 若为运算符，进栈
                if not self.stack:  #栈空
                    self.stack.append(x)
                else:
                    if self.this_bigger(x, self.stack[-1]):  #运算级高于栈顶元素
                        self.stack.append(x)  #直接进栈
                    else:
                        while self.stack:
                            if self.this_bigger(x, self.stack[-1]):
                                break
                            s += self.stack.pop()
                        self.stack.append(x)
        while self.stack:
            s += self.stack.pop()
        return s


    def this_bigger(self, this, last):
        #当前优先级更高
        if (this == '×' or this == '÷' or this == '/') and (last == '+' or last == '-'):
            return True
        else:
            return False

    #返回算式计算结果
    def sloveRpn(self, rpn):
        self.stack1 = []  #用于保存运算数
        for x in rpn:
            if x != '+' and x != '-' and x != '×' and x != '÷' and x != '/':
                self.stack1.append(int(x))
            elif x == '+':
                second = self.stack1.pop()
                first = self.stack1.pop()
                self.stack1.append(first + second)
            elif x == '-':
                second = self.stack1.pop()
                first = self.stack1.pop()
                self.stack1.append(first - second)
            elif x == '×':
                second = self.stack1.pop()
                first = self.stack1.pop()
                self.stack1.append(first * second)
            elif x == '÷':
                second = self.stack1.pop()
                first = self.stack1.pop()
                self.stack1.append(Fraction(first, second))
            elif x == '/':
                second = self.stack1.pop()
                first = self.stack1.pop()
                self.stack1.append(Fraction(first, second))
        resault = self.stack1[0]
        if resault >= 0:
            return resault
        elif resault < 0:
            s = self.getQustion()
            rpn = self.toRpn(s[:-1])
            return self.sloveRpn(rpn)

#开始运行
if __name__ == '__main__':
    n = int(input('please input the num of question：'))
    o = ElArith()
    num_pass = 0
    print('----------the total of question is:{0}----------' .format(n) )
    for i in range(n):
        print('the {0}/{1} '.format(i+1,n), end='')
        question = o.getQustion()
        if o.getAnswer(question):
            num_pass += 1
    print('-------------------------------------')
    print('----------you have pass {0} question----------'.format(num_pass))
