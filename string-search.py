import os
import platform as pl
import time
def clean_screen():
	if 'Windows' in pl.platform():
		os.system("cls")
	else:
		os.system("clear screen")
def delay():
	time.sleep(3)
	clean_screen()
def str_search():
	filelist=os.listdir()
	str_tar=input("Please input the searching string:")
	for x in filelist:
		if "search" and ".git" not in x:
			with open(x,"r") as f:
				for each_line in f:
					if str_tar in each_line:
						print(x)
						break
while True:
	str_search()
	delay()
