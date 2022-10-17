
# continue 用法
"""
sum = 0
for i in range(1,101):
    if i%2==0:
        continue # 提前结束“本次”循环，不会减少循环的次数
    sum = sum + i
print("100以内的奇数和：",sum)
"""




# 循环嵌套使用   循环嵌套一般不超过三层
for n in range(3,101):
    for i in range(2,n):
        if n%i==0:
            print(n,"不是素数")
            break
    if i==n-1:
        print(n,"是素数")
# 嵌套循环：外循环+内循环
# 内层：
# 外层：



# 异常处理   如果没有使用异常处理，后面语句将不会执行
try: # 试试 将担心容易出错的代码，放到try，如果有误，，抛出错误
    x = eval(input("x="))
    sum = x+100
    print(sum)
except: # 捕捉错误，执行except管着的语句
    print("输入有误")

