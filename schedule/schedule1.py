import requests  # 引入requests库
import time  # 引入time，计算下载时间

start = time.time()
size = 0
path = "/Users/edz/Downloads/Test.exe"  # 路径
url = "https://dldir1.qq.com/qqtv/TencentVideo10.14.3360.0.exe"
response = requests.get(url, stream=True)  # stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载
chunk_size = 1024  # 每次块大小为1024
content_size = int(response.headers['content-length'])  # 返回的response的headers中获取文件大小信息
print("文件大小：" + str(round(float(content_size / chunk_size / 1024), 4)) + "[MB]")
with open(path, 'wb') as file:
    for data in response.iter_content(chunk_size=chunk_size):  # 每次只获取一个chunk_size大小
        file.write(data)  # 每次只写入data大小
        size = len(data) + size
        # 'r'每次重新从开始输出，end = ""是不换行
        print('\r' + "已经下载：" + int(size / content_size * 100) * "█" + " 【" + str(
            round(size / chunk_size / 1024, 2)) + "MB】" + "【" + str(
            round(float(size / content_size) * 100, 2)) + "%" + "】", end="")
end = time.time()
print("总耗时:" + str(end - start) + "秒")
