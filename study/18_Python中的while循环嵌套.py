"""
while循环的嵌套使用
"""
# 外层循环
# 内层循环
i = 1
while i <= 100:
    print(f"第{i}天")

    # 内层循环的控制变量
    j = 0
    while j < 10:
        print(j)
        j += 1

    print("Python")
    i += 1

print(f"输出{i - 1}次")

print("-------------")

# 案例：
# print输出不换行：
print("Hello",end='')
print("Woeld",end='')
print("-------------")
# 制表符：\t 效果等同于键盘上的tab键，它可以让我们的多行字符串进行对齐。
print("Hello World")
print("Python Reptile")
print("Hello\tWorld")
print("Python\tReptile")

print("-------------")

# 案例 打印九九乘法表
i = 1
while i <= 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t",end='')
        j += 1
    i += 1
    print() # print空内容就是输出一个换行