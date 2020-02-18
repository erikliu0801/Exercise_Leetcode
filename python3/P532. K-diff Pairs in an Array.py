# ToDo:

"""
532. K-diff Pairs in an Array
Easy

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
## test part
def findPairs(nums, k):
	"""
	nums: List[int]
	k: int
	rtype: int
	"""
## code here
#1
def findPairs(nums, k):

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_nums = [[3, 1, 4, 1, 5], [1, 2, 3, 4, 5], [1, 3, 1, 5, 4]]
	input_k = [2, 1, 0]
	expected_output = [2, 4, 1]
	for i in range(len(input_nums)):
		if findPairs(input_nums[i], input_k[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', findPairs(input_nums[i], input_k[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(findPairs(input_nums[-1], input_k[-1]))
	

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