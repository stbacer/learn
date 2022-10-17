# 引入模块   math库 数学库
# import math
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
# if a != 0 :
#     z = b * b - 4 * a * c
#     if z>0:
#         x1 = (-b+math.sqrt(z))/(2*a)
#         x2 = (-b-math.sqrt(z))/(2*a)
#         print("x1=",x1,sep="")
#         print("x2=",x2,sep="")
#     elif z==0:
#         x1 = x2 = (-b)/(2*a)
#         print("x1=x2=",x1,sep="")
#     else:
#         print("无根!")
#     print("是一个一元二次方程")
#
# else:
#     print("不是一个一元二次方程")




# 引入模块的第一种方式
# 球圆的面积
import math
r = 2
s = math.pi*math.pow(r,2)
print(s)
print(math.log2(2))
print(math.log10(100))
print(math.fabs(-99))
print("----------")
# 引入模块的第二种方式
from math import pi,fabs,log2
print(pi)
print(fabs(-99))
print(log2(8))
print("----------")
# 引入模块的第三种方式
from math import *
print(pi)
print(fabs(-99))
print(log2(8))