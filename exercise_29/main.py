"""
  网上查到一个能用迅雷下载的美剧下载网站【天天美剧】
  抓取该网站上所有美剧链接，并保存在文本文档中，需要哪部剧就直接打开复制链接到迅雷就可以下载了。
"""

"""
实现原理：
   电视剧链接都是在文章里面，文章url后面有数字编号，例如http://cn163.net/archives/24016/，自动生成url，每部剧的都是唯一的，所以改变后面的数字，
   尝试一下大概有多少篇文章，然后用range函数直接连续生成数来构造url。
   但是很多url是不存在的，所以会直接挂掉，因为使用的是requests，其自带的status_code用来判断请求返回的状态的，所以只要是返回的状态码是404就直接跳过，其他的都进去爬取链接，这就解决了url的问题了。
"""

#  -*- coding:utf-8 -*-
import requests
import re
import sys
import threading
import time
reload(sys)
sys.setdefaultencoding('utf-8')
class Archives(object):

    def save_links(self,url):
        try:

            data=requests.get(url,timeout=3)
            content=data.text
            link_pat='"(ed2k://\|file\|[^"]+?\.(S\d+)(E\d+)[^"]+?1024X\d{3}[^"]+?)"'
            name_pat=re.compile(r'<h2 class="entry_title">(.*?)</h2>',re.S)
            links = set(re.findall(link_pat,content))
            name=re.findall(name_pat,content)
            links_dict = {}
            count=len(links)
        except Exception:
            pass
        for i in links:
            links_dict[int(i[1][1:3]) * 100 + int(i[2][1:3])] = i#把剧集按s和e提取编号
        try:
            with open(name[0].replace('/',' ')+'.txt','w') as f:
                print (name[0])
                for i in sorted(list(links_dict.keys())):#按季数+集数排序顺序写入
                    f.write(links_dict[i][0] + '\n')
            print ("Get links ... ", name[0], count)
        except Exception:
            pass

    def get_urls(self):
        try:
            for i in range(2015,25000):
                base_url='http://cn163.net/archives/'
                url=base_url+str(i)+'/'
                if requests.get(url).status_code == 404:
                    continue
                else:
                    self.save_links(url)
        except Exception:
            pass
    def main(self):
        thread1=threading.Thread(target=self.get_urls())
        thread1.start()
        thread1.join()
if __name__ == '__main__':
    start=time.time()
    a=Archives()
    a.main()
    end=time.time()
    print( end-start)
