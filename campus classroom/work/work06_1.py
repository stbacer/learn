# 输入一个学生的整数成绩
# 按[90,100]、[80,89]、[70,79]、[60,69]、[0,59]
# 的范围分别给出A、B、C、D、E的等级

# x = eval(input("请输入成绩："))
# if x>=90 and x<=100:
#     print("A")
# elif x>=80 and x<=89:
#     print("B")
# elif x>=70 and x<=79:
#     print("C")
# elif x>=60 and x<=69:
#     print("D")
# elif x>=0 and x<=59:
#     print("E")
# else:
#     print("你输入的成绩有误！")


# 输入0-6的整数，把它作为星期，其中0对应星期日，1对应星期一，……，以此类推，要求在屏幕打印输出：
# Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday。
x = int(input("请输入一个0-6的整数："))
if x==0:
    print("Sunday")
elif x==1:
    print("Monday")
elif x==2:
    print("Tuesday")
elif x==3:
    print("Wednesday")
elif x==4:
    print("Thuresday")
elif x==5:
    print("Friday")
elif x==6:
    print("Saturday")
else:
    print("你输入的数字有误！")