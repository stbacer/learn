#输出50-100所有奇数
# number=50
# while number<101:
#     if number % 2 == 1:
#         print(number)
#
#     number +=1

#输入若干非负整数，当输入-1程序终止，计算输入数据的最大值，最小值，平均值
# a = int(input("请输入整数："))
a = int(input("请输入整数："))
b = 0
sum = 0
max = min = a
while a >=0:
    a = int(input("请输入整数："))
    sum = sum + a
    if max < a:
        max = a
    elif min > a:
        min = a
    else:
        min = min
    # a = int(input("请输入整数："))
    b = b + 1
    print("最大数max=",max,sep="")
    print("最小数min=",min,sep="")
print("平均值：",sum/b)
print(b)
