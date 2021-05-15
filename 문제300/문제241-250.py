#241
from datetime import datetime
print(datetime.now())
#242
print(type(datetime.now()))
#243
from datetime import timedelta
for i in range(5,0,-1):
    print(datetime.now()-timedelta(i))
#244
import time
print(time.strftime('%I:%M:%S', time.localtime(time.time())))

#245
print(datetime.strptime("2020-05-04","%Y-%m-%d"))

#246
#while True:
#    print(datetime.now())
#    time.sleep(1)


#247
#import 모듈
#from 모듈 import 이름
#from 모듈 as 이름
#from 모듈 import *

#248
from os import getcwd
print(getcwd())

#249
os.rename("C:\Users\User\Desktop\h.txt","a.txt")
#250
import numpy
print(numpy.arange(0,5,0.1))