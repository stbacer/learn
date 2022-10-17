"""
演示Python中的input语句
获取键盘的输入信息
"""
# print("请告诉我你的名字")
# name = input()
# print("你叫：%s" % name)

name = input("请告诉我你的名字")
print("你好！%s" % name)
print(f"您好！{name}")


# 输入数字类型
num = input("请输入你的年龄：")
# 数据类型转换
num = int(num)
print("你输入年龄的类型是",type(num))
print(f"你今年{num}了")