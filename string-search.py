import os
import platform as pl
def str_search():
    str_tar=input("请输入需要搜索的特征信息:")
    os.system("cls")
    for x in os.listdir():
        with open(x,"r") as f:
            i=0
            for each_line in f and i==0:
                if str_tar in each_line:
                    print(x)
                    i=1
str_search()