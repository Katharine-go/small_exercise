import requests
import json

print('************欢迎使用旅游景点查询系统**************')
while 1:
    city = input('输入旅游城市名（输入0退出）：')
    if city =='0':
        print('已退出旅游查询系统')
        break
    else:
        url = 'http://api.map.baidu.com/telematics/v3/travel_city?location=%s&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json' % city
        rs = requests.get(url)
        rs_dict = json.load(rs.text)
        error_code = rs_dict['error']
        if error_code == 0:
            date = rs_dict['date']
            result = rs_dict['result']
            cityid = result['cityid']
            cityname = result['cityname']
            star = result['star']
            abstract = result['abstract']
            description = result['description']
            print('日期：%s\n城市编号：%s\n城市名：%s\n城市等级：%s\n摘要：%s\n简介：%s\n' % (
            date, cityid, cityname, star, abstract, description))
            print('********************************旅游方式*********************************************')
            itineraries = result['itineraries']
            for detail_dict in itineraries:
                name = detail_dict['name']
                description = detail_dict['description']
                print('旅游方式：%s\n简介：%s\n' % (name, description))
                print('**********************************具体景点介绍************************************')
                itineraries = detail_dict['itineraries']
                for detail1_dict in itineraries:
                    description = detail1_dict.get('description', '未知')
                    dinning = detail1_dict.get('dinning', '未知')
                    accommodation = detail1_dict.get('accommodation', '未知')
                    print('景点简介：%s\n就餐：%s\n住宿：%s\n' % (description, dinning, accommodation))
                    print('************************观光路线***********************************')
                    path = detail1_dict['path']
                    for path_dict in path:
                        name = path_dict['name']
                        detail = path_dict['detail']
                        print('景点：%s\n链接：%s' % (name, detail))
                    print('***********************************************************')

        else:
            print('没有查询到任何信息')
