import os
def data_search(file="operation.txt"):	
	lead_tar=input("Please input the searching product SN or MAC:")
	with open(file,"r") as f:
		for each_line in f:
			if lead_tar in each_line:
				print(each_line)
data_search()