"""
for循环嵌套
while循环和for循环可以相互嵌套校园课堂
"""
# 坚持100天，每天10圈
i = 0
for i in range(1, 101):
    print(f"今天是跑步的第{i}天，加油")
    for j in range(1, 11):
        print(f"今天跑步的第{j}圈")

    print("今天跑完了")

print(f"我坚持了{i}天")

print("------------")

# 案例：九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}\t",end='')
    print()