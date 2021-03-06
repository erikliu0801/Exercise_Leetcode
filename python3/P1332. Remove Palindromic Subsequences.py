# ToDo:

"""
1332. Remove Palindromic Subsequences
Easy

Given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string, if it is generated by deleting some characters of a given string without changing its order.

A string is called palindrome if is one that reads the same backward as well as forward.

Constraints:

    0 <= s.length <= 1000
    s only consists of letters 'a' and 'b'
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def removePalindromeSub(self, s: str) -> int:
## test part
def removePalindromeSub(s):
	"""
	s: str
	rtype: int
	"""
## code here
#1
def removePalindromeSub(s):
	if s == '': return 0
	reversed_s = s[::-1]
	if s == reversed_s : return 1	

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_s = ["ababa", "abb", "baabb", ""]
	expected_output = [1, 2, 2, 0]
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', func(input1[i]), '; Expected Output:', expected_output[i])
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