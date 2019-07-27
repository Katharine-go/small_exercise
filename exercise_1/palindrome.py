str = input("Please input the string: ");
while not str:
    str = input("Please reinput the string: ");

length = len(str);
i = 0;
judge = 1;'1代表字符串是回文'

while i <= (length/2):
    if(str[i] == str[length-i-1]):
        i +=1;
    else:
        judge = 0;
        break;

if judge == 1:
    print("字符串是回文")
else:
    print("字符串不是回文")


