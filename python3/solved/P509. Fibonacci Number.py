# ToDo:

"""
509. Fibonacci Number
Easy
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def fib(self, N: int) -> int:
        
## test part
def fib(N):
	"""
	N: int
	rtype: int:
	"""
## code here
#1
"""
Success
Runtime: 992 ms, faster than 15.12% of Python3 online submissions for Fibonacci Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Fibonacci Number.
"""
def fib(N):
	if N < 1:
		return 0
	elif N ==1:
		return 1
	else:
		return fib(N-1) + fib(N-2)

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