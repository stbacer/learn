"""
判断语句的嵌套
格式：
if 条件1:
    满足条件1 做的事情1
    满足条件1 做的事情2

    if 条件2:
        满足条件2 做的事情1
        满足条件2 做的事情2
第二个if属于第一个if内，只有第一个if满足条件，才会执行第二个if
通过空格缩进来决定语句之间的层次关系
"""
# if int(input("请输入身高：")) > 120:
#     print("身高超出限制，请输入会员等级")
#
#     if int(input("请输入会员等级：")) > 3:
#         print("欢迎！高级会员")
#     else:
#         print("请前往购票厅购票")
# else:
#     print("小朋友免票")


# 综合案例：
# 案例要求：
# 1.数字随机产生，范围1~10
# 2.有3次机会猜测数字，通过3层嵌套判断来实现
# 3.每次猜不中，会提示大了或小了
import random
num = random.randint(1,10)
# 定义一个变量num，变量内存储随机数字。
# print(num)

guess_num = int(input("请输入你要猜测的数字："))

if guess_num == num:
    print("恭喜你第一次就猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    guess_num = int(input("请输入你要猜测的数字："))
    if guess_num == num:
        print("恭喜你第二次就猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

        guess_num = int(input("请输入你要猜测的数字："))
        if guess_num == num:
            print("恭喜你第三次就猜中了")
        else:
            print("三次机会用完了，没有猜中")
            print("数字是：",num)