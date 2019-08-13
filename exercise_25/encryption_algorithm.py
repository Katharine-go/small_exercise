"""
1.
  将字符串和Bytes互相转换可以使用encode()和decode()方法
  利用binascii模块可以将十六进制显示的字节转换成我们在加解密中更常用的显示方式：
"""
'南北'.encode()
b'\xe5\x8d\x97\xe5\x8c\x97'.decode()

import binascii
'南北'.encode()
binascii.b2a_hex('南北'.encode())
binascii.a2b_hex(b'e58d97e58c97')
binascii.a2b_hex(b'e58d97e58c97').decode()

"""
2.url编码
  正常的URL中是只能包含ASCII字符的，也就是字符、数字和一些符号。而URL编码就是一种浏览器用来避免url中出现特殊字符（如汉字）的编码方式。
  其实就是将超出ASCII范围的字符转换成带%的十六进制格式。
"""
from urllib import parse
# quote()方法会自动将str转换成bytes，所以这里传入str和bytes都可以
parse.quote('南北')
parse.unquote('%E5%8D%97%E5%8C%97')

"""
3.Base64编码
  Base64是一种用64个字符来表示任意二进制数据的方法。
  Base64编码可以称为密码学的基石。
  可以将任意的二进制数据进行Base64编码。所有的数据都能被编码为并只用65个字符就能表示的文本文件。
  （ 65字符：A~Z a~z 0~9 + / = ）编码后的数据~=编码前数据的4/3，会大1/3左右。  
"""
import base64
# 注意：用于base64编码的，要么是ASCII包含的字符，要么是二进制数据
base64.b64encode(b'hello world')
base64.b64decode(b'aGVsbG8gd29ybGQ=')

"""
4.MD5(信息-摘要算法)
  message-digest algorithm 5（信息-摘要算法）。经常说的“MD5加密”，就是信息摘要算法。
  md5，其实就是一种算法。可以将一个字符串，或文件，或压缩包，执行md5后，就可以生成一个固定长度为128bit的串。这个串，基本上是唯一的。
"""
import hashlib
# 待加密信息
str = '这是一个测试'

# 创建md5对象
hl = hashlib.md5()

# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())

"""
5.Python加密库PyCryptodome
  PyCrypto是 Python 中密码学方面最有名的第三方软件包，提供了许多加密算法的使用，它的开发工作于2012年就已停止。
  该项目的分支PyCrytodome 取代了 PyCrypto 。
"""
# 安装之前需要先安装Microsoft Visual c++ 2015。
# pip install pycryptodome
# import Crypto （Linux） import Cryptodome（Windows）

"""
6.DES
  DES算法为密码体制中的对称密码体制，又被称为美国数据加密标准.
  DES是一个分组加密算法，典型的DES以64位为分组对数据加密，加密和解密用的是同一个算法.
  DES算法的入口参数有三个：Key、Data、Mode。其中Key为7个字节共56位，是DES算法的工作密钥；Data为8个字节64位，是要被加密或被解密的数据；Mode为DES的工作方式,有两种:加密或解密。
  密钥长64位，密钥事实上是56位参与DES运算（第8、16、24、32、40、48、56、64位是校验位，使得每个密钥都有奇数个1），分组后的明文组和56位的密钥按位替代或交换的方法形成密文组。 
"""
# 导入DES模块
from Cryptodome.Cipher import DES
import binascii

# 这是密钥
key = b'abcdefgh'
# 需要去生成一个DES对象
des = DES.new(key, DES.MODE_ECB)
# 需要加密的数据
text = 'python spider!'
text = text + (8 - (len(text) % 8)) * '='

# 加密的过程
encrypto_text = des.encrypt(text.encode())
encrypto_text = binascii.b2a_hex(encrypto_text)
print(encrypto_text)

"""
7.3DES
  3DES（或称为Triple DES）是三重数据加密算法（TDEA，Triple Data Encryption Algorithm）块密码的通称。它相当于是对每个数据块应用三次DES加密算法。
  由于计算机运算能力的增强，原版DES密码的密钥长度变得容易被暴力破解。3DES即是设计用来提供一种相对简单的方法，即通过增加DES的密钥长度来避免类似的攻击，而不是设计一种全新的块密码算法。
"""

"""
8.AES
  高级加密标准（英语：Advanced Encryption Standard，缩写：AES），在密码学中又称Rijndael加密法，是美国联邦政府采用的一种区块加密标准。
  这个标准用来替代原先的DES，已经被多方分析且广为全世界所使用。经过五年的甄选流程，高级加密标准由美国国家标准与技术研究院（NIST）于2001年11月26日发布于FIPS PUB 197，并在2002年5月26日成为有效的标准。
  2006年，高级加密标准已然成为对称密钥加密中最流行的算法之一。
"""
from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex

# 要加密的明文
data = '南来北往'
# 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
# 目前AES-128足够用
key = b'this is a 16 key'
# 生成长度等于AES块大小的不可重复的密钥向量
iv = Random.new().read(AES.block_size)

# 使用key和iv初始化AES对象, 使用MODE_CFB模式
mycipher = AES.new(key, AES.MODE_CFB, iv)
# 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
# 将iv（密钥向量）加到加密的密文开头，一起传输
ciphertext = iv + mycipher.encrypt(data.encode())

# 解密的话要用key和iv生成新的AES对象
mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
# 使用新生成的AES对象，将加密的密文解密
decrypttext = mydecrypt.decrypt(ciphertext[16:])


print('密钥k为：', key)
print('iv为：', b2a_hex(ciphertext)[:16])
print('加密后数据为：', b2a_hex(ciphertext)[16:])
print('解密后数据为：', decrypttext.decode())

"""
9.REA
  RSA加密算法是一种非对称加密算法。在公开密钥加密和电子商业中RSA被广泛使用。
  该算法基于一个十分简单的数论事实：将两个大素数相乘十分容易，但那时想要对其乘积进行因式分解却极其困难，因此可以将乘积公开作为加密密钥，即公钥，而两个大素数组合成私钥。
  公钥是可发布的供任何人使用，私钥则为自己所有，供解密之用。
"""
import rsa
import binascii

# 使用网页中获得的n和e值，将明文加密
def rsa_encrypt(rsa_n, rsa_e, message):
    # 用n值和e值生成公钥
    key = rsa.PublicKey(rsa_n, rsa_e)
    # 用公钥把明文加密
    message = rsa.encrypt(message.encode(), key)
    # 转化成常用的可读性高的十六进制
    message = binascii.b2a_hex(message)
    # 将加密结果转化回字符串并返回
    return message.decode()

# RSA的公钥有两个值n和e，我们在网站中获得的公钥一般就是这样的两个值。
# n常常为长度为256的十六进制字符串
# e常常为十六进制‘10001’
pubkey_n = '8d7e6949d411ce14d7d233d7160f5b2cc753930caba4d5ad24f923a505253b9c39b09a059732250e56c594d735077cfcb0c3508e9f544f101bdf7e97fe1b0d97f273468264b8b24caaa2a90cd9708a417c51cf8ba35444d37c514a0490441a773ccb121034f29748763c6c4f76eb0303559c57071fd89234d140c8bb965f9725'
pubkey_e = '10001'
# 需要将十六进制转换成十进制
rsa_n = int(pubkey_n, 16)
rsa_e = int(pubkey_e, 16)
# 要加密的明文
message = '南北今天很忙'

print("公钥n值长度：", len(pubkey_n))
print(rsa_encrypt(rsa_n, rsa_e, message))
