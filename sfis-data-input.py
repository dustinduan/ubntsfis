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
def config_update(file="wo-config.cfg"):
    if os.path.exists(file):
        choice=input("请确认是否需要设置新的工单信息:(Y/N)").upper()
        if choice=="Y":
            info="Info:"+input("请输入需要会记录的信息:")
            with open(file,"w") as f:
                f.write(info)
        else:
            with open(file) as f:
                info=f.readline().strip('\n')
    else:
        info="Info:"+input("请输入需要会记录的信息:")
        with open(file,"w") as f:
            f.write(info)
    clean_screen()
    return (info)
def sfis_write(inf,file="sfis.txt"):
    sn="MAC:"+input("请输入需要记录的产品条码:").upper()+' '
    try:
        with open(file,"a") as f:
            f.write(info+' '+sn+sfis_time())
        clean_screen()
        print("sfis记录OK")
        time.sleep(1.5)
        clean_screen()
info_str=config_update()
while True:
    sfis_write(info)