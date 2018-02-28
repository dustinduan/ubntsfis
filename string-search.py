import os
def str_search():
	filelist=os.listdir()
	str_tar=input("请输入需要搜索的特征字符:")
	for x in filelist:
		if "search" not in x:
			with open(x,"r") as f:
				for each_line in f:
					if str_tar in each_line:
						print(x)
						break
str_search()
