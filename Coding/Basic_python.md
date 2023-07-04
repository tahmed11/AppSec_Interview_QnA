#!/usr/bin/env python3 

If __name__=='__main__'
	main()

def main():

Write a function: def function():

One line if else:
product = "iphone" if var == 'iphone X' else False
		
For loop: for i in range (1,len(list),1):
For each loop: for item in dict/list/set/etc

one line for loop: for line in lines: adding_list.append(line)
	
From random import randint
Int x = randint(1,100)

Strings: 
Str = * I am a string " 
print(Str[2:5])
am
Print(Str.strip())
I am a string

Reverse a string array:

Str_array=Str_array[::-1]

String to char list:
List_of_chars=list("I am a string")

Convert str to int:
Int(string)

List

Lists and tuples are standard Python data types that store values in a sequence.

List = ["a","b","c","d"]
List.sort()
List.sort(reverse=True)
List.append("e") -> append add element end of array
List.remove("e")
Insert at position 0 
list.insert(0/1/len(list),element)

Delete item at index 0
Del list[0]

List.count("e") --> Return if item exists
If "e" in list: 
    print e
List.index('element') -- returns index of the element TBC
Max(list)
Min(list)


Convert a list to string 
Join:
test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))
Python->->Ruby->->Java

1. string = "".join(test)
2. string = "".join(str(element) for element in test) 
3. string = "".join(str(element) for element in test if str(element)='a')


Arrays
Numbers_array=[1,2,3,4,5,6,7]
print(numbers_array[2:5]) # 3rd to 5th
[3, 4, 5]
print(numbers_array[:5]) # beginning to 4th [until 5 element doesn’t include 5th element]
[1, 2, 3, 4, 5]
print(numbers_array[5:]) # 6th to end (including 5th element) 
[6, 7]
print(numbers_array[:]) # beginning to end

Dictionary:
Dict ={'a':1,'b':2,'c':3,'d':4}

If a in Dict:
	Print(True)
	
Add element: dict['key']=value
Remove element: dict.pop('key')

Return keys: keys=dict.keys()
Return values: values=dict.values()


Copy by value dict1 = dict.copy()
Sets
Sets, unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values. Because sets cannot have multiple occurrences of the same element, it makes sets highly useful to efficiently remove duplicate values from a list or tuple and to perform common math operations like unions and intersections.

Set = set()
Set = {'InDesign', 'Photoshop', 'Acrobat', 'Premiere', 'Bridge'}
Set.add('Illustrator')
Set.remove('Illustrator')

Set = set(list)  ->> converting list to set


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

Union operation: A | B	Intersection: A & B	Set difference: A - B	Difference between A and B: A ^B
# Output: {1, 2, 3, 4, 5, 6, 7, 8}	print(A & B)	print(A - B)	print(A ^ B)
print(A | B)	# Output: {4, 5}	# Output: {1, 2, 3} 	# Output: {1, 2, 3, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8}	


Map
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.) 

# Return double of n 
def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 

Collections counter:
collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

from collections import Counter

>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]

>>> print Counter(myList).values()
[3, 4, 4, 2, 1]


Sorted function:
The sorted() function returns a sorted list of the specified iterable object.
You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

Def func(num):
	Return num*2

sorted(list/arr/dict.items(), key=func, reverse=False) 

To sort a dictionary using it's value:
dict = {'a':68, 'b': 67, 'c': 66, 'd': 65}]
Here x -> is the tuple ('a':68)
sorted_dict=sorted(dict.items(),key=lambda x:x[1])

print(sorted_dict)
	[('d', 65), ('c', 66), ('b', 67), ('a', 68)]
Check if we can filter like
string="".join(str(element)>b for 


Python lambda:
lambda arguments : expression

lambda a, b : a * b

Convert a list to dictionary: res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 

Object comparison:
object.__lt__(self, other) # For x < y
object.__le__(self, other) # For x <= y
object.__eq__(self, other) # For x == y
object.__ne__(self, other) # For x != y OR x <> y
object.__gt__(self, other) # For x > y
object.__ge__(self, other) # For x >= y

From <https://devinpractice.com/2016/11/29/python-objects-comparison/> 
Class xxxx:

    def __init__(self, color, size):
        self.color = color
        self.size = size

 def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.color == other.color and self.size == other.size

swap an element in list
 i[b], i[a] = i[a], i[b]

Big(O) n: 

Algorithm	Time	Space
Binary search	O(log n)	O(1)
Insert/Bubble sort	O(n^2)	O(1)
Merge/Heap sort	O(nlog n)	O(1)
Quick sort	O(nlog n)	O(1)


To determine a type: type(a_string)
Read a file:lines = open(file_path,'r').readlines()
For line in lines:
	Print(line)
	
Write a file
Writer=open(file_path,'w'):
Writer.write("Hello world")
Writer.close()

Regex:import re
Words = re.split(r'-',string_to_be_evaluated)
Word=word[0]


File system operation:
Os.remove(file)
Os.listdir(path)
os.path.exists('output.txt')

Dump a dict to json: json_dump = json.dump(dict)

Convert json to dict: json_dump = json.loads(json_text)

removed_new_lines_set = set([line.rstrip() for line in open('input.txt')])
	       
Set Environment variable in python:
os.environ['variable']="anything"

Get Environment variable in python:
print(os.environ['variable'])

Timestamp in: 2022_Jan_05_07_09_00_output.csv
import datetime
timestamp = datetime.datetime.now().strftime("%Y_%b_%d_%H_%M_%S_")	       
	       
Requests:
import requests

r = requests.get('https://api.github.com/events')
	       
r = requests.post('https://httpbin.org/post', data = {'key':'value'})	       
	       
headers = {'user-agent': 'my-app/0.0.1'}	       
	       
r = requests.get(url, headers=headers)	 	       
	       
	      
