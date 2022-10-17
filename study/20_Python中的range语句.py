"""
range语句
"""
# 语法1：
# range(num)(获取一个从0开始到num结束的数字序列  注意：不含num本身)
for x in range(10):
    print(x)

print("--------")

# 语法2：
# range(num1, num2) (获得一个从num1开始到num2结束的数字序列 注意：不含num2本身)
for x in range(5, 10):
    # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间的间隔是1
    print(x)

print("--------")

# 语法3：
# range(num1, num2, step) (获得一个从num1开始到num2结束的数字序列 注意：不含num2本身)
# 数字之间的步长，以step为准（step默认为1）
# 如：range(5, 10, 2)取得的数据是[5, 7, 9]
for x in range(5, 10, 2):
    # 从5开始，到10结束（不包含10本身）的一个数字序列,数字之间的间隔是2
    print(x)

