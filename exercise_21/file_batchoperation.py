import os, shutil


"""
下面的代码实现了按照文件的创建顺序对文件进行移动（复制）和统一命名。 
（需要先用 ls -trl 命令按照子文件夹的创建时间递增查看子文件夹，并按照该顺序用自然数对子文件夹重新递增命名。）
"""

def batchRenameFile(srcDirName, destDirName): #srcDirName为源文件夹的绝对路径；destDirName为目标文件夹的绝对路径
    i = 1;
    subDirNameList = os.listDir(srcDirName)
    subDirNameList.sort(key= lambda x:int(x[0:]))   # 按照子文件夹名称递增排序
    # print(subDirNAmeList) 查看排序结果
    for subDirName in subDirNameList:
        fileList = os.listdir(srcDirName+'/'+subDirName)   # 此处给出绝对路径
        fileList.sort(key = lambda x:int(x[3:-4]))  # 按照文件名字符串中的数字部分（下标由3开始，至倒数第4个字符结束，不含倒数第四个字符）递增排序（这也是同一子文件夹中所有文件的创建顺序）
        # print(fileList) 查看排序结果
        for file in fileList[10::]:   #由于每次采集信号是最初采集到的信号不稳定，因此将每次采集到的前10个文件忽略
            shutil.copy(srcDirName+'/'+subDirName+'/'+file,destDirName+'/csi'+str(i)+'.dat')  #此处给出绝对路径
            i=i+1

srcDirName = ' '
destDirName = ' '
batchRenameFile(srcDirName, destDirName)
