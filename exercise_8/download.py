import requests
from contextlib import closing

"""
  利用requests提供了stream流的方式来获取响应体，这样有利于获取实时的下载进度
"""

if __name__ == 'download':
    url = '' #下载地址 e.g. https://download.jetbrains.com/idea/ideaIU-2018.2.1.exe
    with closing(requests.get(url, stream = True)) as response: #当上语句被执行时，只有响应头被下载并返回，便于获取到我们所需要的数据，比如内容长度content-length
        chunk_size = 1024 #单次请求最大值
        content_size = int(response.headers['content-length']) # 内容体总大小
        data_count = 0
        with open('idea.exe', "wb") as file:
            for data in response.iter_content(chunk_size = chunk_size): #使用response.iter_content来控制工作流，来遍历获取资源数据
                file.write(data)
                data_count = data_count + len(data)
                now_jd = (data_count /content_size) * 100
                print("\r 文件下载进度：%d%%(%d%d) - %s" %(now_jd, data_count, content_size, url), end=" ")
                """
                打印：
                    在打印内容开头加入/r会使光标回到首行，不换行，可以实现进度条的效果。%d 整数
                """