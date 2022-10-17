# id(x) 获得变量x的存储位置

# x = 5
# print(id(x))

# 输出函数
x = 3
y = 5
print(x,y) # 输出时，多个参数默认空格隔开
# 自己定义多个函数之间的间隔符：sep=','   逗号隔开
print(x,y,sep="********")
# 自己定义输出完了之后的字符，不想换行，end='---'
print(x,y,end="----->不想换行")
print(x,y,sep="*******")
a = 100
b = 200
print("a=",a) #默认，空格隔开，换行 a= 100
print("a=",a,sep="") #
# print(a,b,sep="",end="") # 不换行不空格


print("李老师","你好")
print("张同学","你也好",sep="***",end="\t\t\t")
print("李老师","你好",sep=",")