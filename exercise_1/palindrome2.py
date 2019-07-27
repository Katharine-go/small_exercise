str = input("Please input the string: ")
while not str:
    str = input("Please reinput the string: ")

str2 = reversed(list(str))
if list(str) == list(str2):
    print("字符串是回文")
else:
    print("字符串不是回文")