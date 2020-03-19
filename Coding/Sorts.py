#!/usr/bin/env python3
import sys
from random import randint

def ran_gen_list():
	list = []
	for i in range(0,10,1):
		list.append(randint(1,1000))
	return list
	
def bubblesort(list):
	sort=True
	## ...,5,3... => ...,3,5....
	## ...,6,7.... => ....6,7..... (index)
	## swap(6,7) => list[6]=5, list[7]=3 => list[6]=3, list[7]=5
	##  index_small = 6, index_large = 7
	def swap(index_small,index_large):
		temp = list[index_small] #temp=5
		list[index_small] = list[index_large] #list[6]= list[7]/3
		list[index_large] = temp		#list[7] = 5		
	while(sort):
		#start of the function define a sort to be false so we dont keep looping in infinity loop until no more sort is required. Assume this is the last sort. 
		sort=False
		#iterate from 1st element until the end at each sort call. 
		for i in range(0,len(list)-1,1):
			if(list[i]>list[i+1]):
				swap(i,i+1)
				#print(list)
				sort=True
	return list
	
def insertion_sort(list):
    for i in range(len(list)):
        cursor = list[i]
        pos = i
      
        while pos > 0 and list[pos - 1] > cursor:
            # Swap the number down the list
            list[pos] = list[pos - 1]
            pos = pos - 1
		# Break and do the final swap
        list[pos] = cursor
        print(str(i)+":"+ str(list))
		
    return list

	
list = ran_gen_list()
print("Unsorted list:")
print(list)
#print("Bubble Sorting...")
#list=bubblesort(list)
#print("Bubble sorted list:")
#print(list)
list=insertion_sort(list)
print("Insertion sorted list:")
print(list)