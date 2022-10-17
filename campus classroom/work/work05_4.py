# 输入年份值，输出其是否为闰年。
a = eval(input("请输入年份："))
if((a%4==0) and (a%100!=0))or (a%400==0):
    print(a,"年是闰年")
else:
    print(a,"年不是闰年")