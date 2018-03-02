import time
import platform as pl
import os
def clean_screen():
    if 'Windows' in pl.platform():
        os.system("cls")
    else:
        os.system("clear screen")
def TPI_info(file="//10.6.1.14/公用Public/public/TPI.txt"):
    sn=input("请输入需要记录的产品工单:").upper()
    with open(file,"r") as f:
        for each_line in f:
            if sn in each_line:
                print(each_line)
while True:
    TPI_info()
    n=input("Press Any Key To Continue......")
    clean_screen()