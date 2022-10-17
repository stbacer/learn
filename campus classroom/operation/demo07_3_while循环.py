# 计算s=1+2+3+...+n的和，其中n由键盘输入
# n = int(input("n="))
# x = 0
# s = 0
# while x <= n :
#     s = s + x
#     x = x + 1
#     print(s)
# print("1+2+3+...+",n,"=",s,sep="")
# print("最后的结果 s =",s,)


# 输入5个同学的成绩，计算平均成绩
# a = int(input("请输入第一个同学的成绩："))
# b = int(input("请输入第二个同学的成绩："))
# c = int(input("请输入第三个同学的成绩："))
# d = int(input("请输入第四个同学的成绩："))
# e = int(input("请输入第五个同学的成绩："))
a = 1
s = 0
x = 0
while a<=5 :
    b = int(input("请输入前五名同学的成绩"))
    s = s + b
    x = s / a
    # print("前",a,"名同学的平均成绩",x,sep="")
    a = a + 1
print("五名同学的平均成绩x=",x,sep="")