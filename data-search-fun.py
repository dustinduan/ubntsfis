import os
import time
import platform as pl
def clean_screen():
	if 'Windows' in pl.platform():
		os.system("cls")
	else:
		os.system("clear screen")
def delay():
	time.sleep(3)
	clean_screen()
def data_search(file="operation.txt"):	
	lead_tar=input("Please input the searching product SN or MAC:")
	with open(file,"r") as f:
		for each_line in f:
			if lead_tar in each_line:
				print(each_line)
while True:
	data_search()
	delay()