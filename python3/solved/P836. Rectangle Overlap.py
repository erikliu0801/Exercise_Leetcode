# ToDo:

"""
836. Rectangle Overlap
Easy

A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Notes:
Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
## test part
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        rec1: List[int]
        rec2: List[int]
        rtype: bool:
        """
        
## code here
#1
"""
Success
Runtime: 28 ms, faster than 58.13% of Python3 online submissions for Rectangle Overlap.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rectangle Overlap.
"""
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        def isOverlap(a1, a2, b1, b2):
            if a2 < a1 : a1, a2 = a2, a1
            if b2 < b1 : b1, b2 = b2, b1
            if b1 >= a2 or b2 =< a1: return False
            else: return True
        return isOverlap(rec1[0], rec1[2], rec2[0], rec2[2]) and isOverlap(rec1[1], rec1[3], rec2[1], rec2[3])
        


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [[0,0,2,2], [0,0,1,1]]
    input2 = [[1,1,3,3], [1,0,2,1]]
    expected_output = [True, False]
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