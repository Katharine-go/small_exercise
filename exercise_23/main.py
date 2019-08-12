"""
Python翻转字符串(reverse string), 包含5种方法.

方法如下

5种方法的比较:

1. 简单的步长为-1, 即字符串的翻转(常用);

2. 交换前后字母的位置;

3. 递归的方式, 每次输出一个字符;

4. 双端队列, 使用extendleft()函数;

5. 使用for循环, 从左至右输出;

"""
string = 'abcdef'


def string_reverse1(string):
    return string[::-1]


def string_reverse2(string):
    t = list(string)
    l = len(t)
    for i, j in zip(range(l - 1, 0, -1), range(l // 2)):
        t[i], t[j] = t[j], t[i]
    return "".join(t)


def string_reverse3(string):
    if len(string) <= 1:
        return string
    return string_reverse3(string[1:]) + string[0]


from collections import deque


def string_reverse4(string):
    d = deque()
    d.extendleft(string)
    return ''.join(d)


def string_reverse5(string):
    # return ''.join(string[len(string) - i] for i in range(1, len(string)+1))
    return ''.join(string[i] for i in range(len(string) - 1, -1, -1))


print(string_reverse1(string))
print(string_reverse2(string))
print(string_reverse3(string))
print(string_reverse4(string))
print(string_reverse5(string))
