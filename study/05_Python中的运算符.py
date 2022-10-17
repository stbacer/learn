"""
演示Python中的各类运算符
"""
# 算术运算符
print("1 + 1 =",1 + 1)
print("2 - 1 =",2 - 1)
print("13 * 2 =",13 * 2)
print("10 / 5 =",10 / 5)
print("11 // 4 =",11 // 4)
print("11 % 4 =",11 % 4)
print("10 ** 5 =",10 ** 5)


# 赋值运算符
num = 1 + 2 * 3

# 复合赋值运算符
num = 1
num += 1
print("num += 1:",num)
num -= 1
print("num -= 1:",num)
num *= 4
print("num *= 4:",num)
num /= 2
print("num /= 2:",num)

num = 3
num %=2
print("num %= 2:",num)

num **= 2
print("num **= 2:",num)

num = 9
num //= 2
print("num //= 2:",num)

