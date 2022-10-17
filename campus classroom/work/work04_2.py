a = eval(input("请输入一个四位数的正整数："))
b = a // 1000
# print(b)
c = a % 1000 // 100
# print(c)
d = a % 100 //10
# print(d)
e = a % 10 // 1
# print(e)
print("千位数是：",b)
print("百位数是：",c)
print("十位数是：",d)
print("个位数是：",e)