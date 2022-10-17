a = eval(input("您总共消费："))
b = eval(input("付款："))
change = b - a
print("找零：",change)
c = change //50
# print(c)
d = change%50//5
# print(d)
e = change%50%5//1
# print(e)
print("找钱方案：50元：",c,"张   5元：",d,"张   1元：",e,"张")