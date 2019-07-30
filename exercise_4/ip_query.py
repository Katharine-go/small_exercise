import sys
import requests
#找不到requests库时，查看是否安装requests，若以安装，查看是否为有多个版本的python（查询可知，在python下找到该库，在python下运行即可）

def query(ip):
    url = 'http://ip-api.com/json/' + ip
    response = requests.get(url)

    inf = {} #定义一个字典inf
    inf = response.json() #把api网站json接口返回值传给字典inf
    #下面为从字典中取值，显示
    print("**********************************")
    print("您查询的IP地址%s来源地信息为： "%(inf.get('query')))
    print("国家： %s"%(inf.get('country')))
    print("城市： %s"%(inf.get('city')))
    print("经纬度坐标: %s,%s"%(inf.get('lat'),inf.get('lon')))
    print("运营商编号: %s"%(inf.get('as')))
    print("ISP服务商: %s"%(inf.get('isp')))
    print("**********************************")

ip = '180.97.33.108'
query(ip)