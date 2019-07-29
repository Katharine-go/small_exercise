import urllib.request
import json
import gzip

cityname = input('请输入你想查询的城市？\n')
#访问的url，其中的urllib.parse.quote是将城市名转换为url组件
url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(cityname)
#发送请求并读取到weather_data
weather_data = urllib.request.urlopen(url).read()
#以utf-8的编码方式解压数据
weather_data = gzip.decompress(weather_data).decode('utf-8')
#将json数据转换为dict数据
weather_dict = json.loads(weather_data)
print(weather_dict)

if weather_dict.get('desc') == 'invilad-citykey':
    print("输入的城市名有误")
elif weather_dict.get('desc') == 'OK':
    print('OK')
    forecast = weather_dict.get('data').get('forecast')

    startoday = '城市' + weather_dict.get('data').get('city') + '\n' \
              + '日期: ' + forecast[0].get('date') + '\n'\
              + '温度: ' + weather_dict.get('data').get('wendu') + '℃\n' \
              + '高温：' + forecast[0].get('high') + '℃\n' \
              + '高温：' + forecast[0].get('high') + '℃\n' \
              + '风向：' + forecast[0].get('fengxiang') + '\n'\
              + '风力：' + forecast[0].get('fengli') + '\n'\
              + '天气：' + forecast[0].get('type') + '\n'\
              + '感冒：' + weather_dict.get('data').get('ganmao') + '\n'

    one_day   ='日期：'+forecast[1].get('date')+'\n' \
              +'天气：'+forecast[1].get('type')+'\n'\
              +'高温：'+forecast[1].get('high')+'\n'\
              +'低温：'+forecast[1].get('low')+'\n'\
              +'风向：'+forecast[1].get('fengxiang')+'\n'\
              +'风力：'+forecast[1].get('fengli')+'\n'

    two_day   = '日期：' + forecast[2].get('date') + '\n' \
              + '天气：' + forecast[2].get('type') + '\n' \
              + '高温：' + forecast[2].get('high') + '\n' \
              + '低温：' + forecast[2].get('low') + '\n' \
              + '风向：' + forecast[2].get('fengxiang') + '\n' \
              + '风力：' + forecast[2].get('fengli') + '\n'

    three_day = '日期：' + forecast[3].get('date') + '\n' \
              + '天气：' + forecast[3].get('type') + '\n' \
              + '高温：' + forecast[3].get('high') + '\n' \
              + '低温：' + forecast[3].get('low') + '\n' \
              + '风向：' + forecast[3].get('fengxiang') + '\n' \
              + '风力：' + forecast[3].get('fengli') + '\n'

    four_day  = '日期：' + forecast[4].get('date') + '\n' \
              + '天气：' + forecast[4].get('type') + '\n' \
              + '高温：' + forecast[4].get('high') + '\n' \
              + '低温：' + forecast[4].get('low') + '\n' \
              + '风向：' + forecast[4].get('fengxiang') + '\n' \
              + '风力：' + forecast[4].get('fengli') + '\n'

    print(one_day)
    print(two_day)
    print(three_day)
    print(four_day)


