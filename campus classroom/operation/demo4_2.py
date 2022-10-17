# 强制类型转换
# x = eval(input("请输入一个十进制数："))
# print("17的二进制数=",bin(x),sep="")
# print("17的八进制数=",oct(x),sep="")
# print("17的十六进制数=",hex(x),sep="")
# print("17的十进制数=",int(x),sep="")

# 强制转换成整型数据，只丢弃小数点后面的数据
y = 12.2
y1 = int(y)
print(y1)

# float 强制转换成浮点型数据

# str 字符串类型

# complex 复数类型
z = 123
a = 3+5j
z2 = complex(z) # 强制转换成复数类型
print(type(a),type(z2))
print(a+z2)

# 布尔类型（bool） 逻辑型：True Flase
#一切非零的数据都是True
# 一切非零（空）的数据都是Flase
b = True
c = 19
d = 0
print(type(b))
print(bool(c))
print(bool(d))

# 赋值号：=
# 1.直接赋值 x = 100
# 2.链式赋值
x=y=z=20
print(x,y,z)
# 3.解包赋值  赋值号左右两边的数目要相等，否则会报错
a,b = 10,45 #错误案例：x,y,z=12,45
print(a,b)