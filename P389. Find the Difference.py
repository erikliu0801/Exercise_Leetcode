# ToDo:

"""
389. Find the Difference
Easy
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
## test part
def findTheDifference(s,t):
	"""
	s: str
	t: str
	rtype: str
	"""
## code here
#1
"""
Runtime Error
Last executed input
"a"
"aa"

Success
Runtime: 24 ms, faster than 98.45% of Python3 online submissions for Find the Difference.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Find the Difference.
"""
def findTheDifference(s,t):
	return (set(t) - set(s)).pop()

#1.1
def findTheDifference(s,t):
	t_set, s_set = set(t), set(s)
	if len(t_set) != len(s_set):
		return (t_set - s_set).pop()
	for alphabet in t_set:
		if t.count(alphabet) > s. count(alphabet):
			return alphabet

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