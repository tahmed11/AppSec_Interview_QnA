#!/usr/bin/env python3
import generate_list
from random import randint
#index: 0,1,2,3,4, 5, 6
#list:  1,2,5,6,8,10,12
#search = 2, l=0,h=5, mid=2,list[mid/2]=5
def binary_search(search,list):
	
	low = 0
	high = len(list)-1	
	found = False
	while (low <= high and found is False):
		mid=int((low+high)/2)
		if(search== list[mid]):
			found = True
		#shift left 
		elif(search < list[mid]):
			high=mid-1
		else:
			low=mid+1
	return found	

def check_if_exists(search,list):
	if search in list:
		return True
	else:
		return False
		
		
def regression_test():
	for i in range(100):
		list=generate_list.generate(100)
		list.sort()
		x=randint(0,200)
		if(binary_search(x,list)==check_if_exists(x,list)):
			print("Pass")
		else:
			print("Fail")

def main():
	regression_test()
	

if __name__ == '__main__':
	main()