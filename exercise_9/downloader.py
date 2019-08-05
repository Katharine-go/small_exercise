import requests
from concurrent.futures import ThreadPoolExecutor
import threading

class downloader():
    def __init__(self,url,num,name):
        self.url = url
        self.num = num  #线程数
        self.name = name
        r = requests.head(self.url)
        self.size = int(r.headers['Content-Length']) #下载文件总大小
        # 用head方法获取到http首部信息，在从获取的信息中提取到Content-Length字段，得知数据块大小

    def down(self, start, end):
        headers = {'Range': 'bytes={}-{}'.format(start, end)} #得到部分文件
        r = requests.get(self.url, headers = headers, stream = True)

        # 写入文件相应位置
        with open(self.name,"rb+") as f:
            f.seek(start) #调节文件指针
            f.write(r.content)

    def run(self):
        f = open(self.name,"wb")
        f.truncate(self.size) #截取大小为size的文件
        f.close()

        # 多线程并发执行下载各自的部分，然后再汇总
        futures = []
        part = self.size //self.num
        pool = ThreadPoolExecutor(max_workers = self.num)
        for i in range(self.num):
            start = part * i
            if i == self.num -1:  #最后的文件块
                end = self.size
            else:
                end = start + part -1
            # 扔进线程池
            futures.append(pool.submit(self.down, start, end))
        threading.wait(futures)
