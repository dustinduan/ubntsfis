import requests as rt
import os
r=rt.get("https://hao.360.cn/?safe")
print (os.getpid())
print (os.getppid())