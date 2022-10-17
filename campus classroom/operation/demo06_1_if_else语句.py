# 三元运算
# 输入两个整数，输出最大的一个。
'''
x = eval(input("请输入第一个数："))
y = eval(input("请输入第二个数："))
value = x if x >= y else y
# 真：取左边的值；假：取右边的值
print("较大值：",value)



# 输入一个整数，判断它是奇数还是偶数。
x = int(input("请输入一个整数："))
t = "这是一个偶数！" if x%2==0 else "这是一个奇数！"
print(t)


# 输入一个整数，输出其绝对值。
x = eval(input("请输入一个数："))
a = x if x>0 else -x
print("x的绝对值：",a)
'''

# 多分支选择结构
# 输入一个学生的整数成绩m
# 按[90,100]、[80,89]、[70,79]、[60,69]、[0,59]
# 的范围分别给出A、B、C、D、E的等级
m = int(input("请输入成绩："))
if m>=90 and m<=100:
    print("A")
elif m>=80 and m<=89:
    print("B")
elif m>=70 and m<=79:
    print("C")
elif m>=60 and m<=69:
    print("D")
else:
    print("E")