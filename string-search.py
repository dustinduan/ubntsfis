import os
import platform as pl
def screen_clean():
    if 'window' in pl.platform():
        os.system("cls")
    else:
        os.system("clear screen")
def str_search(path=''):
    str_tar=input("请输入需要搜索的特征信息:")
    screen_clean()
    for x in os.listdir(path):
        with open(x,"r") as f:
            i=0
            for each_line in f and i==0:
                if str_tar in each_line:
                    print(x)
                    i=1
str_search()