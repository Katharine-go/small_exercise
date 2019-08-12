from socket import *
import threading, sys, json, re
# 引入json模块主要为了数据的封装传输，re为了一些合法性的验证

HOST = '192.168.1.7'
PORT = 8022
BUFSIZE = 1024  # 缓冲区大小：1K
ADDR = (HOST, PORT)
myre = r"^[_a-zA-Z]\w{0,}"
tcpCliSock = socket(AF_INET, SOCK_STREAM)
# 创建一个socket连接
userAccount = None
# 用户登录标志，也用来记录用户的登录名

def register():
    print("Glad to have you a member of us!")
    account = input("Please input your account: ")
    if not re.findall(myre, account):
        print('Account illegal!')
        return None
    password1 = input('Please input your password: ')
    password2 = input('Please confirm your password: ')
    if not (password1 and password1 == password2):
        print("Password not illegal!")
        return None
    global userAccount
    userAccount = account
    regInfo = [account, password1, 'register']
    datastr = json.dumps(regInfo)
    tcpCliSock.send(datastr.encode('utf-8'))
    data = tcpCliSock.rev(BUFSIZE)
    data = data.decode('utf-8')
    if data == '0':
        print('Success to register!')
        return True
    elif data == '1':
        print('Failed to register,account existed')
        return False
    else:
        print('Failed for exceptions!')
        return False

def login():
    print("Welcome to login in!")
    account = input("Account: ")
    if not re.findall(myre, account):
        print('Account illegal!')
        return None
    password = input('Password: ')
    if not password:
        print('Password illegal!')
        return None
    global userAccount
    userAccount = account
    loginInfo = [account, password,'login']
    datastr = json.dumps(loginInfo)
    tcpCliSock.send(datastr.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if data == '0':
        print('Success to login!')
        return True
    else:
        print('Failed to login in(user not exist or username not match the password)!')
        return False

def addGroup():
#群组添加
    groupname = input('Please input group name: ')
    if not re.findall(myre, groupname):
        print('group name illegal!')
        return None
    return groupname

def chat(target):
# 可以选择群聊和点对点聊天
    while True:
        print('{} -> {}: '.format(userAccount,target))
        msg = input()
        if len(msg) > 0 and not msg in 'qQ':
            if 'group' in target:
                optype = 'cg'
            else:
                optype = 'cp'

            dataObj = {'type': optype, 'to': target, 'msg': msg, 'froms': userAccount}
            datastr = json.dumps(dataObj)
            tcpCliSock.send(datastr.encode('utf-8'))
            continue
        elif msg in 'qQ':
            break
        else:
            print('Send data illegal!')

class inputdata(threading.Thread):
# 根据用户选择执行不同的功能程序
    def run(self):
        menu = """
                        (CP): Chat with individual
                        (CG): Chat with group member
                        (AG): Add a group
                        (EG): Enter a group
                        (H):  For help menu
                        (Q):  Quit the system
             
        """
        print(menu)
        while True:
            operation = input("Please input your operation('h' for help): ")
            if operation in 'cPCPCpcp':
                # 进入个人聊天
                target = input('Who would you like to chat with: ')
                chat(target)
                continue

            if operation in 'cgCGCgcG':
                # 进入群聊
                target = input('Which group would you like to chat with: ')
                chat('group' + target)
                continue
            if operation in 'agAGAgaG':
                # 添加群组
                groupName = addGroup()
                if groupName:
                    dataObj = {'type': 'ag', 'groupName': groupName}
                    dataObj = json.dumps(dataObj)
                    tcpCliSock.send(dataObj.encode('utf-8'))
                continue
            if operation in 'egEGEgeG':
            #入群
                groupname = input('Please input group name fro entering: ')
                if not re.findall(myre, groupname):
                    print('group name illegal!')
                    return None
                dataObj = {'type': 'eg', 'groupName': 'group'+groupname}
                dataObj = json.dumps(dataObj)
                tcpCliSock.send(dataObj.encode('utf-8'))
                continue
            if operation in 'hH':
                print(menu)
                continue

            if operation in 'qQ':
                sys.exit(1)
            else:
                print('No such operation!')

class getdata(threading.Thread):
    # 接收数据线程
    def run(self):
        while True:
            data = tcpCliSock.recv(BUFSIZE).decode('utf-8')
            if data == '-1':
                print('can not connect to target!')
                continue
            if data == 'ag0':
                print('Group added!')
                continue

            if data == 'eg0':
                print('Entered group!')
                continue

            if data == 'eg1':
                print('Failed to enter group!')
                continue

            dataObj = json.loads(data)
            if dataObj['type'] == 'cg':
                # 群组消息的格式定义
                print('{}(from {})-> : {}'.format(dataObj['froms'], dataObj['to'], dataObj['msg']))
            else:
                # 个人消息的格式定义
                print('{} ->{} : {}'.format(dataObj['froms'], userAccount, dataObj['msg']))

def main():
    try:
        tcpCliSock.connect(ADDR)
        print('Connected with server')
        while True:
            loginorReg = input('(l)ogin or (r)egister a new account: ')
            if loginorReg in 'lL':
                log = login()
                if log:
                    break
            if loginorReg in 'rR':
                reg = register()
                if reg:
                    break

        myinputd = inputdata()
        mygetdata = getdata()
        myinputd.start()
        mygetdata.start()
        myinputd.join()
        mygetdata.join()

    except Exception:
        print('error')
        tcpCliSock.close()
        sys.exit()

if __name__ == '__main__':
    main()











