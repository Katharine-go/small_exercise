# 初始化，处理输入的数据
inputstr = input("Please input the string: ")
inputstr = inputstr.lower()
lst = (inputstr).split(' ')

# 使用字典存储，出现不同的单次的次数
dit = {}
max = 0
maxkey = ""

for item in lst:
    if(dit.get(item,0)):
        dit[item] = dit[item] + 1
    else:
        dit[item] = 1

for i in dit:
    print(i , ":", dit.get(i), )