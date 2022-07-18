#!/usr/bin/python3
#-*-coding:UTF-8-*-
#try:
#    statement(s)
#except exception:
#    deal_exception_code
#except exception2:
#    deal_exception2_code
#else:
#    no_exception_happend_code

#不带异常类型的except
#try:
#    raise BException()
#except DException:
#    print("D")
#except:
#    print("处理全部其他异常")

#except捕获多种异常类
#try:
#    raise BException()
#except (BException,DException):
#    print("D")
#except:
#    print("处理其他全部异常")
#else:
#    print("没有异常")

#try-finally语句
#try:
#    raise BException()
#except (BException,DException):
#    print("D")
#except:
#    print("处理全部其他异常")
#else:
#    print("没有异常")
#finally:
#    print("必须执行")

#def diyExeption(level):
#    if level > 0:
#        raise Exception('raise exception', level)
#        print("不执行")
#try:
#    diyException(3)
#except Exception as err:
#    print(err)

#自定义异常
#class   DiyError(RuntimeError):
#    def __init__(self, arg):
#            self.args = arg
#try:
#    raise DiyError("my diy exception")
#except DiyError as e:
#    print(e)
######################################################################################################################
#完成两个变量的交换
#a = 20
#b = 30
#print("变量交换前a的值为{},b的值为{}" .format(a,b))
#
#使用第三方临时变量
#c = a
#a = b
#b = c
#print("变量交换后a的值{},b的值{}" .format(a,b))

#使用python特有的方式
#a,b = b,a
#print("变量交换后a的值{},b的值{}" .format(a,b))

#使用运算符
#a = a + b
#b = a - b
#a = a - b
#print("变量交换后a的值{},b的值{}" .format(a,b))

#使用位运算符
#a = a ^ b
#b = a ^ b
#a = a ^ b

#print("变量交换后a的值{},b的值{}" .format(a,b))



#有4个数字1，2，3，4,能组成多少个不互相同且无重复数字的三位数，各有多少
#count  = 0
#for a in range(1,5):
#    for b in range(1,5):
#        for c in range(1,5):
#            if a != b and a != c and b != c:
#                print(a*100+b*10+c)

#求应发的奖金
#企业发放的奖金根据利润提成，从键盘输入当月的利润I，求对应发放奖金的总数
#利润(I)低于或等于10万的时候，奖金提成10%
#高于10万低于20万，低于10万的部分按10%提成，高于10万的部分按7.5%提成
#20万到40万之间，高于20万的部分提成5%
#40万到60万之间，高于40万的部分提成3%
#60万到100万之间，高于60万的部分提成1.5%
#高于100万，超过100万的部分按1%提成

#profit = [1000000,600000,400000,200000,100000,0]
#rate = [0.01,0.015,0.03,0.05,0.075,0.1]
#bonus = 0   #奖金 
#键盘输入当月的利润
#i = int(input("当月的利润:"))
#
#for j in range(6):
#    if i > profit[j]:
#        bonus += (i - profit[j])*rate[j]
#        i = profit[j]
#print(bonus)



#输入某年某日，判断这一天是这一年的第几天

#year = int(input("年:"))
#month = int(input("月:"))
#day = int(input("天"))
#sum_day = 0
#leap_year = 0
#months = (0,31,59,90,120,151,181,212,243,273,304,334)
#if 0 < month <=12:
#    sum_day = months[month - 1]
#else:
#    print("输入的月份有误")
#
#判断是否为闰年，能被400整除或被4整除且不能被100整除
#if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#    leap_year == 1
#
#判断如果是闰年且月份大于2则在总天数上加1
#if leap_year == 1 and month > 2:
#    sum_day += day + 1
#else:
#    sum_day += day
#print(f"it is the {sum_day}th day")




#输入三个整数x,y,z，并把这三个数由小到大输出
#x = int(input("x值:"))
#y = int(input("y值:"))
#z = int(input("z值:"))

#num_list = [x,y,z]
#num_list.sort()
#print(num_list)

#斐波那契数列
#函数创建
#def fibonaccil(n):
#    a = 0
#    b = 1
#    for i in range(n):
#        a,b = b,a+b
#    print(f"斐波那契数列第{n}项值为:{a}")
#fibonaccil(100)
#递归创建
#def fibonacci2(n):
#    if n == 1 or n == 2:
#        return 1
#    else:
#        return fibonacci2(n-1) + fibonacci2(n-2)
#
#print(fibonacci2(10))

#将一个列表的数据复制到另一个列表中
#list1 = [1,2,3,4,5]
#print(list1)
#使用copy
#new_copy = list1.copy()
#print(new_copy)

#使用切片
#new_copy2 = list1[:]
#print(new_copy2)


#输出九九乘法表
#第一个数字从1变化到9，第二个数字最多变化到和第一个数字相等，最后的数字是前两个数字的乘积
#for i in range (1,10):
#    for j in range(1,i+1):
#        print(f"{i} * {j} = {i * j}", end='\t')
#    print()


#判断100~200之间有多少素数，并输出所有素数
#素数：只有被1和自身整除的数
#范围是100~200,需要使用循环
#如果有一个非1和本身的数被整除，则跳出循环，判断下一个数字
#如果循环完成，都只有1和本身被整除，符合条件，计数器+1

#while循环
#计数器

#count = 0

#i = 101
#while i < 200:
#    j = 2
#    while j < i / 2:
#        if i % j ==0:
#            break
#        j += 1
#    else:
#        count += 1
#        print(i)
#    i += 1
#print(f"the total is {count}")
#count = 0
#
##for循环
#for i in range(101,201):
#    for j in range(2,int(i/2)):
#        if i % j ==0:
#            break
#    else:
#        count += 1
#        print(i)
#print(f"the total is {count}")




#打印水仙花数
#水仙花数：指一个三位数，其各位数字的立方和等于该数本身
#for i in range(100,1000):
#    ge_wei = i % 10
#    shi_wei = i // 10 % 10
#    bai_wei  = i // 100
#    if i ==(ge_wei ** 3 + shi_wei ** 3 + bai_wei ** 3):
#        print(i)

#for x in range(100,1000):
#    s = str(x)
#    a = int(s[0])
#    b = int(s[1])
#    c = int(s[2])
#    if x == a**3 + b**3 + c**3:
#        print(x)


#条件运算符
#成绩>=90用A，60~89用B，60以下用C
#while True:
#    score =int(input("输入成绩:"))
#    score_grade = 'A' if score >=90 else 'B' if 60 <= score <=89 else 'C'
#    print(score_grade)
#    break

#输入一行字符，分别统计出其中的英文字母，空格数字和其他字符的个数

import re

s = input("输入一个字符串:").strip()
letters = 0
space = 0
digit = 0
other = 0

for i in s:
    if i.isalpha():
        letters +=1
    elif i.isspace():
        space +=1
    elif i.isdigit():
        digit +=1
    else:
        other +=1
print(f'char = {letters}, space = {space}, digit = {digit}, others = {other}')






































