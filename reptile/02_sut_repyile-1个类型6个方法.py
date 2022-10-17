import  urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
# print(type(response))

#按照一个字节一个字节去读
# content = response.read()
# print(content)

#返回多少个字节
# content = response.read(5)
# print(content)

#读取一行
# content = response.readline()
# print(content)

#一行一行的读取直到读完
# content = response.readlines()
# print(content)

# 返回状态码  可以通过状态码去判断代码有没有问题  如果是200了，就证明我们的逻辑没有错
# print(response.getcode())

# 返回url地址
# print(response.geturl())

#获取一些状态信息
print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法 read  readline  readlines  getcode  geturl  getheaders