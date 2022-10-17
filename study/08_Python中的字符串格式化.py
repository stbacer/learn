# 通过占位的方式完成拼接
name = "Python"
message = "学习 %s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 2021
avg_salary = 123456
message = "Python大数据技术学科，重庆%s级，学习共%s人" %(class_num,avg_salary)
print(message)



#
name = "大数据技术"
enrollment_year = 2021
tuition_fee = 8000.00
message = "从%d年开始，我学习%s，一年学费%f元" % (enrollment_year,name,tuition_fee)
print(message)

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1) # 宽度的限制比数字本身宽度还小 宽度限制无效
print("数字11.345宽度限制7，小数精度限制2，结果是：%7.2f" % num2) # 小数部分的精度控制会进行四舍五入
print("数字11.345宽度不限制，小数精度限制2，结果是：%.2f" % num2)