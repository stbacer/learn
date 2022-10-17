a = eval(input("请输入第一个数："))
b = eval(input("请输入第二个数："))

# 输出数据类型
print(type(a))
print(type(b))
# 存储位置
print("a的存储位置",id(a),sep="")
# 和
sum = a + b
sub = a - b
mul = a * b
print("a和b的和：",sum)
# 差
print("a和b的差：",sub)
# 乘积
print("a和b的乘积：",mul)