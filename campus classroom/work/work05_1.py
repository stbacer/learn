# 输入一个整数，判断它是奇数还是偶数。
x = eval(input("请输入一个整数："))
print(x)
if x % 2 == 0:
    print("x =",x,"是偶数")
else:
    print("x =",x,"是奇数")