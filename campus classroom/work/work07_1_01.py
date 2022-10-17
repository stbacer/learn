# 任务一
# 1.在显示器上显示一个菜单模型，当输入数字时输出其对应的文字
'''
print("1 存款")
print("2 取款")
print("3 转账")
print("4 查询")
print("5 退出")
a = int(input("请输入你所需要的操作编号："))
if a==1:
    print("存款")
elif a==2:
    print("取款")
elif a==3:
    print("转账")
elif a==4:
    print("查询")
elif a==5:
    print("退出")
else:
    print("你输入的编号有误")


# 2.根据某人的BMI值，判定身高体重指数等级
a = int(input("请输入身高体重指数："))
if a<18.5:
    print("偏瘦")
elif a<24:
    print("正常")
elif a<27:
    print("偏胖")
elif a<30:
    print("肥胖")
else:
    print("重度肥胖")






# 任务二：
# 1.输出50~100范围内所有的奇数
a=50
while a<=100:
    if a%2==1:
        print(a)
    a=a+1


'''






#输入若干非负整数，当输入-1程序终止，计算输入数据的最大值，最小值，平均值
a=[]
b = int(input("请输入整数:"))
while True:
    if b == -1:
        break
    a.append(b)
    b=int(input("请输入整数："))
    if b==-1:
        break
    print(f'最大值是{max(a)}')
    print(f'最小值是{min(a)}')
    print('平均值是' + str(sum(a) / len(a)))