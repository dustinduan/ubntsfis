import time
import platform as pl
import os
def clean_screen():
    if 'Windows' in pl.platform():
        os.system("cls")
    else:
        os.system("clear screen")
def sfis_time():
    return ("Date:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
def config_update(file="//10.6.1.14/公用Public/public/wo-config.cfg"):
    if os.path.exists(file):
        with open(file,"r") as wo_info:
            print(wo_info.readline())
        choice=input("请确认是否需要设置新的工单信息:(Y/N)").upper()
        if choice=="Y":
            info="Info:"+input("请输入需要会记录的信息:")
            with open(file,"w") as f:
                f.write(info)
        else:
            with open(file) as f:
                info=f.readline().strip('\n')
    else:
        info="Info:"+input("请输入需要记录的工单信息:")
        with open(file,"w") as f:
            f.write(info)
    clean_screen()
    print(info)
    return (info)
def sfis_write(inf,file="//10.6.1.14/公用Public/public/sfis.txt"):
    sn=input("请输入需要记录的产品条码:").upper()+' '
    with open(file,"a") as f:
        f.write(inf+' MAC:'+sn+sfis_time())
        clean_screen()
    with open(file,"r") as f:
        for each_line in f:
            if sn.strip(' ') in each_line:
                print(each_line)
    print("sfis记录ok")
    n=input("Please Press Any Key To Continue......")
    clean_screen()
wo_info=config_update()
while True:
    sfis_write(wo_info)