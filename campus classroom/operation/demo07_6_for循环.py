"""
# 1.计算s=2+4+98+100
s = 0
for i in range(2,101,2):
    s = s+i
print("2+4+98+100=",s)





# 2.判断100~999之间能同时被3、5、7、整除的，并将其输出
for i in range(100,1000):
    if i%3==0 and i%5==0 and i%7==0:
        print(i,"能同时被3、5、7整除",sep="")

import math
print("100~999之间的所有水仙花数如下：")
for i in range(100,1000,1):
    a = i//100
    b = i//10%10
    c = i%10
    if a*a*a+math.pow(b,3)+c**3==i :
        print(i)
"""






# 从键盘输入一个数，判断是否为素数，并将其输出   （素数：只能被1和本身整除）
a = int(input("请输入一个整数："))
flag = 0
for i in range(2,a):
    if a%i==0:
        flag = flag + 1 # 当出现a%i=0，可以得出结论，就提前结束循环让循环的次数减少
        # 如果不提前结束循环，i就会走到最后
if flag == 0:
    print(a,"是素数",sep="")
else:
    print(a,"不是素数",sep="")


n = int(input("n="))
for i in range(2,n):
    if n%i==0:
        print(n,"不是素数")
        break# 当出现a%i=0，可以得出结论，就提前结束循环让循环的次数减少
        # 如果不提前结束循环，i就会走到最后
if i==n-1:
    print(n,"是素数")