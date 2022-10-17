"""
关键字continue（跳过循环）和break（结束循环）
"""

# 循环中断语句 continue
for i in range(1, 6):
    print("语句 1")
    continue
    print("语句2")

# continue的嵌套应用
for i in range(1, 6):
    print("语句1")
    for j in range(1, 6):
        print("语句2")
        continue
        print("语句3")

    print("yuju4")

# 循环中断语句break
for i in range(1, 101):
    print("语句  1")
    break
    print("语句  2")

print("语句  3")

print("-----------")

# break的嵌套应用
for i in range(1, 10):
    print("1")
    for j in range(1, 10):
        print("2")
        break
        print("3")
    print("4")