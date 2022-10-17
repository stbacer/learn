"""
while循环
"""
# 结构
# while 条件:
#     满足条件时，做的事情1
#     满足条件时，做的事情2
#     满足条件时，做的事情3（只要条件满足，会无限循环执行）
# while 的条件需得到布尔类型的值，true表示继续循环，false表示结束循环

i = 0
while i < 100:
    print("Python")
    i += 1 # 设置循环终止条件 如果没有这行命令，循环将会永远执行

# 案例：猜数字
# 设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
# 1.无限次机会，直到猜中为止
# 2.每猜一次不中会提示大了或小了
# 3.猜完数字后提示猜了几次

# 获取范围在1-100的随机数字
import random
num = random.randint(1,100)

# 定义一个变量，记录总共测了多少次
count = 0

flag = True
while flag:
    guess_num =int(input("请输入你猜的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("你猜大了")
        else:
            print("你猜小了")
print(f"你总共猜测了{count}次")
