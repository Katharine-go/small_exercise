import time

import numpy as np
from PIL import ImageGrab

# 每抓取一次屏幕需要的时间约为1s,如果图像尺寸小一些效率就会高一些
beg = time.time()
debug = False
for i in range(10):
    img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
end = time.time()
print(end - beg)