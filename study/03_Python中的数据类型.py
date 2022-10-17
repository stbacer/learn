# 方式1：使用print直接输出类型信息
print(type("学习Python"))
print(type(123))
print(type(1.2))
# 方式2：使用变量存储type()语句的结果
string_type = type("学习Python")
int_type = type(123)
float_type = type(1.2)
print(string_type)
print(int_type)
print(float_type)
# 方式3：使用type()语句，查看变量中存储的数据类型信息
name = "Python"
name_type = type(name)
print(name_type)