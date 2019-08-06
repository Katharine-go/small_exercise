import os
import shutil
import zipfile
from os.path import join, getsize

def zip_file(src_dir):
    # 压缩指定文件夹
    zip_name = src_dir + '.zip'
    # src_dir: 压缩的文件夹路径；zip_name: 压缩后zip文件的路径及名称
    z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
            print ('==压缩成功==')
    z.close()

def unzip_file(zip_src, dst_dir):
    #zip_src: zip文件的全路径，dst_dir: 要解压到的目的文件夹
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file,dst_dir)
    else:
        print("This is not zip")

"""
  python其他操作文件方法：
    1.剪切（移动）文件到指定目录
      shutil.move(filename, dst_dir)
    2.删除文件夹
      shutil.rmtree(src_dir)
    3.删除指定文件
      os.remove(file_src)
    4.新建文件夹
      os.mkdir(dst_dir)
    5.遍历文件夹
      for filename in os.listdir(src_dir)
    6.复制文件
      shutil.copyfile(src_file,dst_file)
    7.获取文件夹大小
      def get_dir_size(dir_path):
        size = 0L
        for root, dirs, files in os.walk(dir_path):
          size += sum([getsize(join(root, name)) for name in files])
        return size
      可以根据文件大小做出不同的判断：
        file_size = get_dir_size(DATA_PATH)
        max_size = file_size /1024/ 1024 #获取以MB为单位的值
        if max_size < 100:
          pass
      
"""