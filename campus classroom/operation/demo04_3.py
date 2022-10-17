# // 向下取整 向小的方向取整
x = 10//4
print(x) # 2

# 求余 去两个数的余数
c = 8%3
print(c)

# 乘方
b = 3**2
print(b)

a = (9//2)*(9/2)
b = (100%13//3)**2
print(a)
print(b)

# 复合赋值运算符 += -= *= /= //= %= *=
a = 8
b = 3
a%=b
print(a)

# 比较运算符--》结果是bool类型
print(3!=4)
print(4==5)
print(5>7)
print(6<9)
print(5>=4)

# 逻辑运算符
# or 做操作数是非0的 则取左边的值 ；左操作数是0 则取右边的数
print(0 or 3) # 3
print(5 or 4) # 5
print(6 or 0) # 6
print( None or 8)
# and 做操作数是0，则取左边的值；做操作数是非0，则取右边的0
print(3-3 and 4)
print(4-5 and 8)
print(None and 9)
# not 一元运算符 只需要一个操作数
# 结果True False
print(not 5)
print(not None)
print(not 9-8)
#总结：算术运算符>成员测试运算符(in 、not in 、is 、not is)>关系运算符>逻辑运算符
