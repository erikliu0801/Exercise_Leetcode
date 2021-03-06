#35
def searchInsert(nums, target):	
	if len(nums) == 0:
		return 0
	else:
		if target < nums[0]:
			return 0
		elif target > nums[-1]:
			return len(nums)
		else:
			for i in range(len(nums)):
				if nums[i] == target:
					return i
				elif target < nums[i]:
					return i

#38
def countAndSay(n):
	start = '1'
	if n > 1:
		# answer = ''
		for m in range(n-1):
			count = 1
			answer, repeat = '', ''
			for i in range(len(start)):
				if i == 0:
					repeat = start[i]
				elif start[i] == repeat:
					count += 1
				elif start[i] != repeat:
					answer = answer + str(count) + str(start[i-1])
					repeat = start[i]
					count = 1
			answer = answer + str(count) + str(start[-1])
			start = answer
		return answer
	else:
		return start

#53
def maxSubArray(nums):
	max_sum, process_sum = 0, 0
	max_one = float('-inf')
	for num in nums:
		if process_sum + num > 0 or num > 0:
			process_sum += num
			if process_sum > max_sum:
				max_sum = process_sum	
			if num > max_one:
				max_one = num
		else:
			process_sum = 0
			if num > max_one:
				max_one = num
	if max_one < 0:
		max_sum = max_one
	return max_sum

#58
def lengthOfLastWord(s):
	s = s.lstrip()
	s = s.rstrip()
	len_word = 0
	for i in range(len(s)):
		if s[i] == ' ': #end with ' '?
			len_word = 0
		else:
			len_word += 1
	return len_word

#66
def plusOne(digits):
	digits[-1] = digits[-1] + 1
	if digits[-1] >= 10:
		digits[-1] = digits[-1] -10
		carry = 1
		position = 1
		while carry == 1:
			if position == len(digits):
				digits = [1] + digits
				position += 1
				carry = 0
			else:
				position += 1
				digits[0-position] = digits[0-position] + carry
				if digits[0-position] >= 10:
					digits[0-position] = digits[0-position] -10
				else:
					carry = 0
	return digits

#67
def addBinary(a, b):
	position = 1
	carry = False
	bi_sum = ''
	if len(a) < len(b):
		a, b = b, a
	while position <= len(b):
		if a[0-position] == '1' and b[0-position] == '1':
			if carry == True:
				bi_sum = '1' + bi_sum
			else:
				bi_sum = '0' + bi_sum
			carry = True
			position +=1
		elif a[0-position] == '0' and b[0-position] == '0':
			if carry == True:
				bi_sum = '1' + bi_sum
			else:
				bi_sum = '0' + bi_sum
			carry = False
			position +=1
		else:
			if carry == True:
				bi_sum = '0' + bi_sum
			else:
				bi_sum = '1' + bi_sum
			position +=1
	while carry == True:
		if position <= len(a):
			if a[0-position] == '1':
				bi_sum = '0' + bi_sum
				carry = True
			else:
				bi_sum = '1' + bi_sum
				carry = False			
		else:
			bi_sum = '1' + bi_sum
			carry = False
		position +=1
	if position <= len(a):
		bi_sum = a[:1-position] + bi_sum
	return bi_sum

#69
def mySqrt(x):
	if x < 0: #math.abs(x)
		x = 0 -x
	if x in [0,1]:
		return x
	else:
		try_num = x//2
		high_limit, low_limit = x, 0
		answer = 0
		while answer < 1:
			if try_num**2 > x:
				high_limit = try_num
				if try_num == low_limit +1:
					answer = low_limit
					break
				else:
					try_num = (try_num + low_limit)//2						
			elif try_num**2 < x:
				low_limit = try_num
				if try_num in [high_limit -1, high_limit] :
					answer = try_num
					break
				else:
					try_num = (try_num + high_limit)//2
			else:
				answer = try_num
				break
		return answer

#70
def climbStairs(n):
	def mathCombination(a,b):
		if a in [0] or b in [0]:
			return 1
		if b > a:
			a, b = b, a
		numerator = 1
		denominator = 1
		for i in range(b):
			numerator *= a - i
			denominator *= 1 +i
		return numerator//denominator
	if n in [1,2,3]:
		return n
	elif n > 3:
		two, steps = 0, 0
		while n >= 0:
			steps += mathCombination(n+two, two)
			n += -2
			two += 1
		return steps
	else:
		return 0

if __name__ == "__main__":
    #35
	# input_nums = [
	# [1,3,5,6],
	# [1,3,5,6],
	# [1,3,5,6],
	# [1,3,5,6]
	# ]
	# input_target = [5,2,7,0]
	# expected_output = [2,1,4,0]
	# for i, j in enumerate(input_nums):
	# 	if searchInsert(input_nums[i],input_target[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(searchInsert(input_nums[i],input_target[i]))
	# 	else:
	# 		print("Right")		
	# print(searchInsert(input_nums[-1],input_target[-1]))

    #38
    # input1 = [1, 2, 3, 4, 5, 6, 7, 8]
    # expected_output = ["1", "11", "21", "1211", "111221", "312211", "13112221", "1113213211"]

    # for i, j in enumerate(input1):
    #     if countAndSay(input1[i]) != expected_output[i]:
    #         print("Wrong!!!")
    #         print(countAndSay(input1[i]))
    #     else:            
    #         print("Right")
    # print(countAndSay(input1[1]))

	#53
	# input_nums = [
	# 	[-2,1,-3,4,-1,2,1,-5,4],
	# 	[-5, 3, 7, -3, -5, 3, 2, 4],
	# 	[1],
	# 	[-1],
	# 	[-64,78,56,10,-8,26,-18,47,-31,75,89,13,48,-19,-69,36,-39,55,-5,-4,-15,-37,-27,-8,-5,35,-51,83,21,-47,46,33,-91,-21,-57,0,81,1,-75,-50,-23,-86,39,-98,-29,69,38,32,24,-90,-95,86,-27,-23,-22,44,-88,3,27,9,55,-50,-80,40,5,-61,-82,-14,40,-58,35,93,-68,-26,94,3,-79,9,-88,21,19,-84,7,91,-8,84,12,-19,-13,-83,66,-80,-34,62,59,48,-98,53,-66,18,94,46,11,-73,96,-18,6,-83,91,17,38,10,9,-78,-22,77,83,89,-42,-30,-94,-98,-34,-51,63,-97,96,64,55,-93,-41,27,52,69,53,26,-71,-64,42,-80,52,-43,6,-62,-21,83,-85,-38,49,-50,8,55,-72,74,80,90,53,53,32,-15,36,90,-88,-34,37,41,91,65,76,33,61,5,90,-33,42,-54,-73,34,-16,75,83,91,7,-89,42,-36,77,-5,-83,9,80,53,-23,68,-81,90,10,-90,55,-14,19,-7,91,-14,59,33,31,62,-33,-85,37,-73,83,-78,-86,25,-15,91,97,2,-23,54,-68,53,22,-73,43,-68,-87,-25,18,31,67,-14,94,3,-81,25,-35,-37,17,79,-34,-23,-99,-43,-98,-38,-52,75,63,1,29,71,-68,-71,74,51,-40,86,-73,54,-5,70,-60,-11,-49,-64,90,-8,-25,-16,-52,40,60,-75,96,39,-13,-79,14,-73,22,-79,75,30,-51,49,-19,-15,36,-16,-60,-69,-68,-21,-4,-18,-9,-14,50,65,70,75,-17,30,99,-44,-31,-14,-46,60,-10,52,80,-35,-18,-94,-86,62,-10,49,-53,6,56,-45,62,-48,36,-47,15,-37,-81,-15,-62,-22,91,-85,33,-62,-23,86,97,66,15,54,-69,96,36,-55,36,-97,70,82,9,4,-63,-29,32,49,23,-53,88,18,8,-96,72,-23,-82,6,14,-6,-31,-12,-39,61,-58,-32,57,77,12,-7,56,-40,-48,-35,40,-35,12,-28,90,-87,-4,79,30,80,82,-20,-43,76,62,70,-30,-92,-42,7,68,-24,75,26,-70,-36,95,86,0,-52,-49,-60,12,63,-11,-20,75,84,-41,-18,41,-82,61,98,70,0,45,-83,8,-96,24,-24,-44,-24,-98,-14,39,97,-51,-60,-78,-24,-44,10,-84,44,89,67,5,-75,-73,-53,-81,64,-55,88,-35,89,-94,72,69,29,-52,-97,81,-73,-35,20,-99,13,36,98,65,69,8,81,13,-25,25,95,-1,51,-58,-5,16,-37,-17,57,-71,-35,29,75,70,53,77,51,79,-58,-51,56,31,84,54,-27,30,-37,-46,-56,14,56,-84,89,7,-43,-16,99,19,67,56,24,-68,-38,-1,-97,-84,-24,53,71,-6,-98,28,-98,63,-18,-25,-7,21,5,13,-88,-39,28,-98,68,61,-15,44,-43,-71,1,81,-39,62,-20,-60,54,33,69,26,-96,48,-69,-94,11,-11,-20,80,87,61,-29,98,-77,75,99,67,37,-38,11,93,-10,88,51,27,28,-68,66,-41,41,36,84,44,-16,91,49,71,-19,-94,28,-32,44,75,-57,66,51,-80,10,-35,-19,97,-65,70,63,86,-2,-9,94,-59,26,35,76,11,-21,-63,-21,-94,84,59,87,13,-96,31,-35,-53,-26,-84,-34,60,-20,23,58,15,-7,21,-22,67,88,-28,-91,14,-93,61,-98,-38,75,-19,-56,59,-83,-91,-51,-79,16,14,-56,90,6,-14,27,63,-91,-15,-22,-22,82,32,-54,47,-96,-69,-61,86,91,-60,-75,43,-3,-31,3,-9,-23,28,11,69,-81,31,59,25,-83,-36,-12,-75,48,42,-21,8,-26,24,-68,-23,31,-30,-60,0,-13,-36,-57,60,32,22,-49,85,-49,38,55,-54,-31,-9,70,-38,54,-65,-37,-20,76,42,64,-73,-57,95,-20,74,-57,19,-49,29,83,-7,-11,-8,-84,40,-45,-57,-45,86,-12,24,-46,-64,62,-91,-30,-74,-35,-76,44,-94,-73,86,77,7,37,-80,-74,87,48,85,-19,-85,-45,-27,31,9,-8,85,-28,79,-14,25,91,-51,10,-61,-49,74,-38,94,56,-12,57,34,71,-5,53,74,-18,-21,59,39,-30,90,-88,-99,-24,3,62,47,-40,-51,-27,-49,-26,82,-11,1,34,27,-5,-10,92,-48,-99,63,23,31,14,-94,-90,-49,44,-44,-59,33,-44,17,-64,-82,-36,-28,-57,13,0,-7,-4,88,70,-93,-7,-35,-4,-15,-6,-26,-75,93,-95,39,98,90,66,20,-54,-93,-47,-22,0,-35,-28,41,14,-8,-46,-86,84,26,-98,55,32,-29,96,-94,32,-33,-21,57,-39,-17,-27,-64,-50,-61,55,-28,-78,84,49,22,-73,-79,-37,40,12,-7,53,-26,-80,31,-94,51,-97,-98,56,34,-54,-88,-32,-17,-29,17,18,20,32,-49,91,54,-65,40,-47,-39,38,-8,-99,-73,84,30,0,-96,-38,5,32,-36,-16,-35,74,29,-23,-80,-88,47,36,29,-32,-54,79,-64,76,91,53,-71,-71,-9,-3,-93,17,-19,36,94,-38,97,-1,70,-62,82,-65,-87,11,11,-68,-1,-41,44,-71,3,89]
	# ]
	# expected_output = [6, 11, 1, -1, 3452]
	# expected_nums = [
	# 	[4,-1,2,1]
	# ]

	# for i, j in enumerate(input_nums):
	# 	if maxSubArray(input_nums[i]) != expected_output[i]:
	# 		print("Wrong!!! Expected Output:", expected_output[i], "; This Output:", maxSubArray(input_nums[i]))
	# 	else:            
	# 		print("Right")
	# print(maxSubArray(input_nums[0]))

	#58
	# input_str = ["Hello World", "Hello World!", "Hello World! ", "Hello World! yes"]
	# expected_output = [5, 6, 6, 3]
	# for i, j in enumerate(input_str):
	# 	if lengthOfLastWord(input_str[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(lengthOfLastWord(input_str[i]))
	# 	else:
	# 		print("Right")		
	# print(lengthOfLastWord(input_str[-1]))

	#66
	# input_digits = [
	# [1,2,3],
	# [4,3,2,1],
	# [9,9,9],
	# [0],
	# [9,8,9]
	# ]
	# expected_output = [
	# [1,2,4],
	# [4,3,2,2],
	# [1,0,0,0]
	# [1],
	# [9,9,0]
	# ]
	# for i in range(len(input_digits)):
	# 	if plusOne(input_digits[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(plusOne(input_digits[i]))
	# 	else:
	# 		print("Right")
	# print(plusOne(input_digits[4]))

	#67
	# input_str_a = ["11", "1010", "100", "101111"]
	# input_str_b = ["1", "1011", "110010", "10"]
	# expected_output = ["100", "10101", "110110", "110001"]
	# for i in range(len(input_str_a)):
	# 	if addBinary(input_str_a[i], input_str_b[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(addBinary(input_str_a[i], input_str_b[i]))
	# 	else:
	# 		print("Right")
	# print(addBinary(input_str_a[-1], input_str_b[-1]))

	#69
	# input_int = [4, 8, 0, 1, 2, 10000000, 1495504530]
	# expected_output = [2, 2, 0, 1, 1, 3162, 38671]
	# for i in range(len(input_int)):
	# 	if mySqrt(input_int[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(mySqrt(input_int[i]))
	# 	else:
	# 		print("Right")
	# print(mySqrt(input_int[-2]))

	#70
	# input_int = [1, 2, 3, 4, 5, 6, 7, 8, 25]
	# expected_output = [1, 2, 3, 5, 8, 13 ,21, 34, 121393]
	# for i in range(len(input_int)):
	# 	if climbStairs(input_int[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(climbStairs(input_int[i]))
	# 	else:
	# 		print("Right")
	# print(climbStairs(input_int[5]))