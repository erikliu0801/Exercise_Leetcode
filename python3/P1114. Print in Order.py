# ToDo:

"""
1114. Print in Order
Easy

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}

The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

 

Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.

 

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Foo:
	def __init__(self):
		pass


	def first(self, printFirst: 'Callable[[], None]') -> None:
		
		# printFirst() outputs "first". Do not change or remove this line.
		printFirst()


	def second(self, printSecond: 'Callable[[], None]') -> None:
		
		# printSecond() outputs "second". Do not change or remove this line.
		printSecond()


	def third(self, printThird: 'Callable[[], None]') -> None:
		
		# printThird() outputs "third". Do not change or remove this line.
		printThird()
## test part

## code here
#1
import threading
class Foo:
	def __init__(self):



	def first(self, printFirst: 'Callable[[], None]') -> None:
		
		# printFirst() outputs "first". Do not change or remove this line.
		printFirst()


	def second(self, printSecond: 'Callable[[], None]') -> None:
		
		# printSecond() outputs "second". Do not change or remove this line.
		printSecond()


	def third(self, printThird: 'Callable[[], None]') -> None:
		
		# printThird() outputs "third". Do not change or remove this line.
		printThird()

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