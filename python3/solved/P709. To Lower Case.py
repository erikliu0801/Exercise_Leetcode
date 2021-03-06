# ToDo:

"""
709. To Lower Case
Easy

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"

Example 2:

Input: "here"
Output: "here"

Example 3:

Input: "LOVELY"
Output: "lovely"



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def toLowerCase(self, str: str) -> str:
        
## test part

## code here
#1
"""
Success
Runtime: 24 ms, faster than 83.13% of Python3 online submissions for To Lower Case.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for To Lower Case.
"""
def toLowerCase(str):
	return str.lower()

#2 mapping
"""
Success
Runtime: 28 ms, faster than 55.40% of Python3 online submissions for To Lower Case.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for To Lower Case.
"""
def toLowerCase(str):
	up = [chr(x) for x in range(65,91)]
	low = [chr(x) for x in range(97,123)]
	s = ''
	for alph in str:
		if alph in up:
			s += low[up.index(alph)]
		else:
			s += alph
	return s

#3 hash table
"""
Success
Runtime: 28 ms, faster than 55.40% of Python3 online submissions for To Lower Case.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for To Lower Case.
"""
def toLowerCase(str):
	up = [chr(x) for x in range(65,91)]
	low = [chr(x) for x in range(97,123)]
	up_low = {up[i]:low[i] for i in range(26)}
	s = ''
	for alph in str:
		if alph in up_low:
			s += up_low[alph]
		else:
			s += alph
	return s



# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = []
	expected_output = []
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!")
			print(func(input1[i]))
		else:
			print("Right")		
	# print(func(input1[-1]))
	

## Performance Test
import cProfile
cProfile.run('')


## Unit Test
import unittest
class Test(unittest.TestCase):
	def test(self):
		pass

if __name__ == '__main__':
    unittest.main()