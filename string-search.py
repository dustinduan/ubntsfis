import os
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
str_search()
