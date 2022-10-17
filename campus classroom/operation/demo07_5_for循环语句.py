# range()函数
l1 = range(0,6,1)
print(l1) # 0 1 2 3 4 5
print(type(l1))
l2 = list(l1) # 列表
print(l2) # [0,1,2,3,4,5] 数组：一组数据

# for 循环
# 格式：
# for 循环变量 in 序列或迭代对象 :
#     循环体
'''
for 循环变量 in range(stop)
    循环体
'''


# 1+2+3+4+5

#while循环:
s=0
i = 1
while i<= 5:
    s = s+1
    i = i+1
print("1+2+3+4+5=",s)

# for 循环
s = 0
for i in range(1,101):
    s = s+i
print("1+2+3+...+100=",s)
