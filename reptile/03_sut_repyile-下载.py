import urllib.request

#下载网页
# url_page = 'https://www.linuxcool.com/'

#url代表下载的路径  filename文件的名子
# 在Python中 可以写变量的名字  也可以直接写值
# urllib.request.urlretrieve(url_page,'linux.html')
#下载图片
# url_img = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2Ftp03%2F1Z9202245031462-0-lp.jpg&refer=http%3A%2F%2Fimg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662991922&t=35356aa085e33833d8726c416115f529'
# urllib.request.urlretrieve(url = url_img,filename='bizi.jpeg')

#下载视频
url_video = ''
urllib.request.urlretrieve(url_video,'01.mp4')