#226
def invertTree(root):
	pass

#231
def isPowerOfTwo(n):
	if n%2 == 1 and n != 1:
		return False
	else:
		i = 0
		while 2**i <= n:
			if 2**i == n:
				return True
			i += 1
		return False

#235
def lowestCommonAncestor(root, p, q):
	pass

#263
def primeFactorization(num):
	prime = 2
	checked_primes = set({2})
	x = set(range(3,num+1,2))
	primes = set()
	while prime <= num:
		if num % prime == 0:
			primes.add(prime)
			while num % prime == 0:
				num = num // prime
		if len(x) != 0:
			prime = min(x)
			checked_primes.add(prime)
			x.remove(prime)
			x -= x.intersection(set(range(prime**2,num+1,prime)))
	return primes

#290
def wordPattern(patternstr, str):
	nums_str = str.split(' ')
	if len(patternstr) != len(nums_str):
		return False
	p_to_s = {}
	have_ds = set()
	for dp, ds in zip(patternstr, nums_str):
		if dp not in p_to_s:
			if ds in have_ds:
				return False
			p_to_s[dp] = ds
			have_ds.add(ds)
		if p_to_s[dp] != ds:
			return False
	return True

#299
def getHint(secret, guess):
	if guess == '':
		return '0A0B'
	elif secret == guess:
		return str(len(secret)) + 'A0B'
	bulls, cows = 0, 0
	secret, guess = list(secret), list(guess)
	s_g_nums = list()
	for s_g in zip(secret,guess):
		s_g_nums.append(s_g)
	secret, guess = list(), list()
	for s_num, g_num in s_g_nums.copy():
		if s_num == g_num:
			bulls +=1
			s_g_nums.remove((s_num,g_num))
		else:
			secret.append(s_num)
			guess.append(g_num)
	for num in guess:
		if num in secret:
			cows += 1
			secret.remove(num)
	return str(bulls) + 'A' + str(cows) + 'B'

def isUgly(num):
	def findPrimes(n):
		pass
	num = abs(num)
	num_primes = findPrimes(num)
	if num_primes - set({2,3,5}) == set({}):
		return True
	return False

#392
def isSubsequence(s, t):
	i = 0
	for alphabet in t:
		if alphabet == s[i]:
			i += 1
		if i == len(s):
			break
	return i == len(s)

#409
def longestPalindrome(s):
	count_nums = list()
	for alphabet in set(s):
		count_nums.append(s.count(alphabet))
	longest_palindrome = 0
	for i, num in enumerate(count_nums):
		if num//2 >= 1:
			longest_palindrome += num - num%2
			count_nums[i] = num%2
	if 1 in count_nums:
		longest_palindrome += 1
	return longest_palindrome

#443
def compress(chars):
	alph = str()
	start = 0
	chars_copy = chars.copy()
	for i, j in enumerate(chars_copy):
		if j != alph or i == len(chars_copy)-1:
			if i != 0 and i - start not in [0,1]:
				for m, count in enumerate(list(str(i-start))):
					chars.insert(start+1+m, count)
			if j == alph:
				chars.remove(j)
				break
			alph = j
			start = i
		else:
			chars.remove(j)
	return len(chars)


if __name__ == '__main__':
	class TreeNode:
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None

		def PrintTree(self):
			if self.left:
				self.left.PrintTree()
			print(self.val),
			if self.right:
				self.right.PrintTree()

		def insert(self, val):
			if self.val:
				if val < self.val :
					if self.left is None:
						self.left = TreeNode(val)
					else:
						self.left.insert(val)
				elif val > self.val:
					if self.right is None:
						self.right = TreeNode(val)
					else:
						self.right.insert(val)
			else:
				self.val = val

	#226
	# input_nums = [[4, 2, 7, 1, 3, 6, 9]]
	# for nums in input_nums:
	# 	root = TreeNode(nums[0])
	# 	for i in nums[1:]:
	# 		root.insert(i)
	# invertTree(root)

	#231
	# print(isPowerOfTwo(16))

	#263
	# import time
	# now = time.time()
	# for i in range(1, 2**31-1):
	# 	print(primeFactorization(i))
	# print(time.time() - now)

	#290
	# input_patternstr = ["abba", "abba", "aaaa", "abba"]
	# input_str = ["dog cat cat dog", "dog cat cat fish", "dog cat cat dog", "dog dog dog dog"]
	# expected_output = [True, False, False, False]
	# for i in range(len(input_patternstr)):
	# 	if wordPattern(input_patternstr[i], input_str[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(wordPattern(input_patternstr[i], input_str[i]))
	# 	else:
	# 		print("Right")
	# print(wordPattern(input_patternstr[2], input_str[1]))

	#299
	# input_secret = ["1807", "1123", "11"]
	# input_guess = ["7810", "0111", "11"]
	# expected_output = ["1A3B", "1A1B", "2A0B"]
	# for i in range(len(input_secret)):
	# 	if getHint(input_secret[i], input_guess[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(getHint(input_secret[i], input_guess[i]))
	# 	else:
	# 		print("Right")
	# print(getHint(input_secret[-1], input_guess[-1]))

	#392
	# print(isSubsequence("acb", "ahbgdc"))

	#409
	# print(longestPalindrome("abccccdd"))

	#443
	print(compress(["a","a","b","b","c","c","c"]))

