def lengthOfLongestSubstring(s):
    unrepeated_substring = []
    substring = ""
    for i, j in enumerate(list(s)):  #
        if substring.count(j) == 0:
            substring = substring + j
        else:
            unrepeated_substring.append(substring)
            for i, k in enumerate(list(substring)):
                if k == j:
                    sub_substring = ""
                    for y in list(substring)[i + 1:]:
                        sub_substring = sub_substring + y
                    substring = sub_substring + j
                    break
    unrepeated_substring.append(substring)
    max_count = 0
    for i, _ in enumerate(unrepeated_substring):
        count = len(unrepeated_substring[i])
        if count > max_count:
            max_count = count
    return max_count

#P4
def findMedianSortedArrays(nums1, nums2):
	def Combine2SortedArrays(l1,l2):
		l0 = []
		if l1 == []:
			l1, l2 = l2, l1
		for i, j in enumerate(l1):
			if l2 != []:
				if j < l2[0]:
					l0.append(j)
					l1 = l1[1:]
				else:
					for l, k in enumerate(l2):
						if k < j:
							l0.append(k)
							l2 = l2[1:]
						else:
							l0.append(j)
							l1 = l1[1:]
							break
					if l2 == []:
						l0.append(j)
						l1 = l1[1:]
			else:
				l0.append(j)
				l1 = l1[1:]
		for k in l2:
			l0.append(k)
		return l0

	nums_combined = Combine2SortedArrays(nums1,nums2)
	if len(nums_combined)%2 == 1:
		return float(nums_combined[len(nums_combined)//2])
	else:
		return (nums_combined[len(nums_combined)//2]+nums_combined[(len(nums_combined)//2)-1])/2.0

#5 new
def longestPalindrome(s):
	if type(s) != str:
		return
	if len(s) == 0:
		return
	reversed_s = s[::-1]
	palindrome_list = list()
	while len(reversed_s) > 1:
		sub_reversed_s = reversed_s
		while len(sub_reversed_s) > 1:
			if sub_reversed_s in s:
				palindrome_list.append(sub_reversed_s)
				break
			sub_reversed_s = sub_reversed_s[:-1]
		reversed_s = reversed_s[1:]
	return max(palindrome_list)
	
#6
def convert(s, numRows):
	#
	if numRows == 1:
		answer = s
	else:
		needed_List = []
		for i in range(numRows):
			needed_List.append([])
		#
		onetime_steps = numRows *2 -2
		for i, j in enumerate(list(s)):
			numofStep = i%onetime_steps
			if numofStep < numRows :
				needed_List[numofStep].append(j)
			else:
				l = numofStep - numRows
				needed_List[-2-l].append(j) #numRows>2
		#
		answer =''
		for i, j in enumerate(needed_List):
			for i in needed_List[i]:
				answer += i
	return answer

#7
def reverse(x):
	#
	negative = False
	if x < 0:
		x = -x
		negative = True
	#
	reverse_str = []
	for i in range(len(str(x))):
		reverse_str.append(str(x)[-1-i])
	revers_x = ''
	for j in reverse_str:
		revers_x = revers_x + j
	revers_x = int(revers_x)
	if negative==True:
		revers_x = 0 - revers_x
	if revers_x<-2**31 or revers_x>2**31-1:
		revers_x = 0
	return revers_x

#8
def myAtoi(str):
	negative = False
	nums = 0
	pre_answer = ''
	for i, j in enumerate(str):
		if j == ' ' and pre_answer == '' and nums==0:
			pass
		elif j == '-' and pre_answer == '' and nums == 0:
			negative = True
			nums += 1
		elif j == '+' and pre_answer == '' and nums == 0:
			nums += 1
		elif j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9' or j == '0':
			pre_answer = pre_answer + j
		else:
			if pre_answer == '':
				pre_answer = '0'
			break
	if pre_answer == '':
		pre_answer = '0'
	if negative == False:
		answer = int(pre_answer)
	else: 
		answer = 0 - int(pre_answer)
	if answer<-2**31 or answer>2**31-1:
		if answer < -2**31:
			answer = -2147483648
		else:
			answer = 2147483647
	return answer

#9
def isPalindrome(x):
	substring =str(x)
	answer = True
	half_len = len(substring)//2
	for i, j in enumerate(substring):
		if i >= half_len :
			if len(substring)%2 == 1:
				break
			else:
				break
		if substring[i] == substring[-1-i]:
			pass
		else:
			answer = False
	if answer != False:
		answer = True
	return answer

#13
def romanToInt(s):
	answer = 0
	step = 0
	for i in range(len(s)):
		if step == 1:
			step = 0
			pass
		elif s[i] == 'M':
			answer += 1000
		elif s[i] == 'D':
			answer += 500
		elif s[i] == 'L':
			answer += 50
		elif s[i] == 'V':
			answer += 5
		elif i+1 == len(s):
			if s[i] == 'M':
				answer += 1000
			elif s[i] == 'D':
				answer += 500
			elif s[i] == 'C':
				answer += 100
			elif s[i] == 'L':
				answer += 50
			elif s[i] == 'X':
				answer += 10
			elif s[i] == 'V':
				answer += 5
			elif s[i] == 'I':
				answer += 1
		elif i+1 < len(s):
			if s[i] == 'C':
				if s[i+1] == 'M':
					answer += 900
					step = 1
				elif s[i+1] == 'D':
					answer += 400
					step = 1
				else:
					answer += 100
			
			elif s[i] == 'X':
				if s[i+1] == 'C':
					answer += 90
					step = 1
				elif s[i+1] == 'L':
					answer += 40
					step = 1
				else:
					answer += 10
			
			elif s[i] == 'I':
				if s[i+1] == 'X':
					answer += 9
					step = 1
				elif s[i+1] == 'V':
					answer += 4
					step = 1
				else:
					answer += 1
	return answer

#14
def longestCommonPrefix(strs):
	if strs == []:
		return ''
	elif len(strs) == 1:
		return strs[0]
	else:
		nums_shortest_str = 1000
		longest_common_prefix = ''
		for i, j in enumerate(strs):
			if nums_shortest_str > len(strs[i]):
				nums_shortest_str = len(strs[i])
		for i in range(nums_shortest_str):
			common = 0
			prefix = strs[1][i]
			for l in range(len(strs)):
				if strs[l][i] == prefix:
					common += 1
				else:
					break
			if common == len(strs):
				longest_common_prefix = longest_common_prefix + prefix
			else:
				break
		return longest_common_prefix

#20
def isValid(s):
	symbols_left = ["{", "(", "["]
	symbols_right = ["}", ")", "]"]
	s_symbols = str()
	for c in s:
		if c in symbols_left or c in symbols_right:
			s_symbols += c
	s_symbols_len = len(s_symbols)
	if s_symbols_len == 0:
		return True
	if s_symbols_len % 2 != 0:
		return False

	while len(s_symbols) != 0:
		if s_symbols[0] not in symbols_left:
			return False

		r = s_symbols.rfind(symbols_right[symbols_left.index(s_symbols[0])])
		if r == -1:
			return False
		s_symbols = s_symbols[1:r] + s_symbols[r + 1:]
	return True

#21
def mergeTwoLists(l1, l2):
	if l1 or l2:
		l0 = ListNode(0)
		l = []
		while l1 and l2:
			if l1.val < l2.val:
				l0.val = l1.val
				l1 = l1.next
			else:
				l0.val = l2.val
				l2 = l2.next
			l.append(l0)
			l0.next = ListNode(0)
			l0 = l0.next	
		while l1:
			l0.val = l1.val
			l1 = l1.next
			l.append(l0)
			l0.next = ListNode(0)
			l0 = l0.next
		while l2:
			l0.val = l2.val
			l2 = l2.next
			l.append(l0)
			l0.next = ListNode(0)
			l0 = l0.next
		l[-1].next = None
		return l[0]
	else:
		if l1:
			return l1
		elif l2:
			return l2
		else:
			return

#26
def removeDuplicates(nums):
	j1 = nums[0]
	count = 1
	for j in nums:
		if j1 != j:
			nums[count] = j
			j1 = j
			count += 1
	nums = nums[:count]
	return len(nums)

#27
def removeElement(nums,val):
	count = 0
	for i, j in enumerate(nums):
		if j != val:
			nums[count] = nums[i]
			count += 1
	nums = nums[:count]
	return len(nums)

#28
def strStr(haystack, needle):
	if needle not in haystack:
		return -1
	elif needle == "":
		return 0
	else:
		answer = -1
		for i in range(len(haystack)):
			if haystack[i] == needle[0]:
				count = 0
				for l in range(len(needle)):
					if haystack[i+l] == needle[l]:
						count += 1
				if count == len(needle):
					answer = i
					break
		if answer != -1:
			return answer
		else:
			return -1

if __name__ == "__main__":
   # string01: str = "abcabcbb"    # string02 = " "
    # string03 = "dvdf"
    # print(lengthOfLongestSubstring(string03))
    
    
    # # P4
    # nums0 = [[[3],[1,2,5],2.5]
    # nums1 = [[1,2],[3,4],2.5]
    # nums2 = [[1,2,7,8],[3,4,5],4.0]
    # nums3 = [[3,4,5],[1,2,7,8],4.0]

    # nums1, nums2, nums3 = nums3[0:]

    # print("nums1= %s ,nums2= %s " %(nums1, nums2))
    # if nums3 != findMedianSortedArrays(nums1,nums2):
    #     print("Wrong Answer! Expect:%s, Output%s"%(nums3, findMedianSortedArrays(nums1,nums2)))
    # else:
    #     print("Right Answer! %s"%(findMedianSortedArrays(nums1,nums2)))

    #5
	# input_s = ["babcd", "cbbd"]
	# expected_output = ["bab", "bb"]

	# for i in range(len(input_s)):
	# 	if longestPalindrome(input_s[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(longestPalindrome(input_s[i]))
	# 	else:
	# 		print("Right")
	# print(longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
	# print(longestPalindrome(input_s[-1]))



	#6
	# string = ["PAYPALISHIRING","PAYPALISHIRING"]
	# numRows = [3, 4]
	# expected_output = ["PAHNAPLSIIGYIR","PINALSIGYAHRPI"]
	# print(convert(string[1],numRows[1]))

	#7
	# x = [123, -123, 120, 1534236469, 900000, 1463847412]
	# expected_output = [321, -321, 21, 0, 9, 2147483641]
	# for i, j in enumerate(x):
	# 	print(reverse(x[i]))

	#8
	# input = ['42','   -42', '4193 with words', 'words and 987', '-91283472332', '+1','+-2', '--1', '-+1', '   +0 123', '-   234' ,'0-1']
	# expected_output = [42, -42, 4193, 0, -2147483648, 1, 0, 0 ,0, 0, 0, 0]
	# for i, j in enumerate(input):
	# 	if myAtoi(input[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(myAtoi(input[i]))
	# 	else:
	# 		print("Right")
	# print(myAtoi(input[2]))

	#9
	# input = [121, 1234, 1234321]
	# expected_output = [True, False, True]
	# for i, j in enumerate(input):
	# 	if isPalindrome(input[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(isPalindrome(input[i]))
	# 	else:
	# 		print("Right")
	# # print(myAtoi(input[2]))

	#13
	# input = ["III", "IV", "IX", "LVIII", "MCMXCIV", "MDLXX"]
	# expected_output = [3, 4, 9, 58, 1994, 1570]
	# for i, j in enumerate(input):
	# 	if romanToInt(input[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(romanToInt(input[i]))
	# 	else:
	# 		print("Right")
	# print(romanToInt(input[1]))

	#14
	# input = [["flower","flow","flight"], ["dog","racecar","car"], [], ["a"], ["c","c"], ["aca","cba"]]
	# expected_output = ["fl", "", "", "a", "c", ""]
	# for i, j in enumerate(input):
	# 	if longestCommonPrefix(input[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(longestCommonPrefix(input[i]))
	# 	else:
	# 		print("Right")
	# print(longestCommonPrefix(input[-1]))

	#20
	input_s = ["()", "()[]{}", "(]", "([)]", "{[]}", "[", "]","][]","[]{","(afadfadf)","(([]){})","((","[({(())}[()])]", "[({(())}[()])]", "[([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([([()])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])])]"]
	expected_output = [True, True, False, False, True, False, False, False, False, True, True, False, True, True, True]
	for i in range(len(input_s)):
		if isValid(input_s[i]) != expected_output[i]:
			print("Wrong!!! Output:", isValid(input_s[i]))
		else:
			print("Right")
	# print(isValid(input_s[-2]))

	#21
	# class ListNode:
	#     def __init__(self, x):
	#         self.val = x
	#         self.next = None
	# class LinkedListFuc:
	# 	def LinkedList2List(ListNode):
	# 		list1 = []
	# 		l0 = ListNode
	# 		while l0.next !=None:
	# 			list1.append(l0.val)
	# 			l0 = l0.next
	# 		list1.append(l0.val)
	# 		return list1
	# 	def List2LinkedList(List):
	# 		l = [] 
	# 		l0 = ListNode(List[0])
	# 		for i, j in enumerate(List):
	# 			l0.val = j
	# 			if i + 1 < len(List):
	# 				l0.next = ListNode(List[i+1])
	# 			l.append(l0)
	# 			if i + 1 < len(List):
	# 				l0 = l0.next
	# 		return l
	# input0 = [[1,2,4],[1,3,4]]
	# input1 = [
	# 	[[1,2,4],[1,3,4]],
	# 	[[1,9],[6,12,50,100]],
	# 	[[],[]],
	# 	[[1,2,3],[]],
	# 	[[],[1,2,3]]
	# 	]
	# expected_output = [[1,1,2,3,4,4],[1,6,9,12,50,100],[],[1,2,3],[1,2,3]]
	# # print(LinkedListFuc.List2LinkedList(input0[0]))
	# # print(LinkedListFuc.List2LinkedList(input0[0])[2].val)
	
	# for i, j in enumerate(input1):
	# 	l1, l2 = LinkedListFuc.List2LinkedList(input1[i][0]), LinkedListFuc.List2LinkedList(input1[i][1])
	# 	if LinkedListFuc.LinkedList2List(mergeTwoLists(l1[0], l2[0])) != expected_output[i]:
	# 		print("Wrong!!! Output:", LinkedListFuc.LinkedList2List(mergeTwoLists(l1[0], l2[0])))
	# 		print("Expected Output:", expected_output[i])
	# 	else:
	# 		print("Right")
	
	#26
	# input1 = [
	# 	[1,1,2],
	# 	[1,1,1,1],
	# 	[-50,-50,-50,-49,-49,-48,-46,-46,-46,-46,-45,-45,-45,-45,-44,-44,-44,-43,-43,-43,-43,-43,-43,-43,-42,-41,-41,-40,-40,-39,-38,-38,-38,-38,-38,-38,-36,-35,-34,-33,-32,-31,-31,-30,-29,-28,-27,-26,-26,-26,-25,-22,-21,-21,-21,-21,-20,-20,-19,-18,-17,-17,-17,-17,-17,-17,-17,-16,-16,-14,-13,-12,-11,-11,-11,-10,-9,-7,-7,-7,-5,-5,-5,-4,-4,-4,-3,-3,-3,-2,-2,-1,-1,-1,-1,0,1,1,1,2,2,3,3,5,6,6,7,8,8,10,10,10,11,11,11,14,14,17,17,17,18,18,18,19,20,21,21,23,23,23,23,24,24,24,24,24,25,27,27,27,28,29,30,30,31,32,33,34,35,36,37,37,37,37,37,38,38,38,39,39,41,41,41,41,44,44,45,45,46,46,46,46,46,47,47,47,47,48,48,50,50]
	# 	]
	# expected_nums = [
	# 	[1,2],
	# 	[1],
	# 	[-50,-49,-48,-46,-45,-44,-43,-42,-41,-40,-39,-38,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-22,-21,-20,-19,-18,-17,-16,-14,-13,-12,-11,-10,-9,-7,-5,-4,-3,-2,-1,0,1,2,3,5,6,7,8,10,11,14,17,18,19,20,21,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,45,46,47,48,50]
	# ]
	# expected_output = [2,1,82]
	# for i, j in enumerate(input1):
	# 	if removeDuplicates(input1[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(removeDuplicates(input1[i]))
	# 	else:
	# 		print("Right")
	# print(removeDuplicates(input1[-1]))

	#27
	# input_nums = [[3,2,2,3],[0,1,2,2,3,0,4,2]]
	# input_val = [3,2]
	# expected_output = [2,5]
	# expected_nums = [[2,2],[0,1,3,0,4]]
	# for i, j in enumerate(input_nums):
	# 	if removeElement(input_nums[i],input_val[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(removeElement(input_nums[i],input_val[i]))
	# 	else:
	# 		print("Right")
	# print(removeElement(input_nums[-1],input_val[-1]))

	#28
	# input_haystack = ["hello", "aaaaa", "aaaaa","helloll","heLLoll","a"]
	# input_needle = ["ll", "bba", "","ll","ll","a"]
	# expected_output = [2, -1, 0, 2, 5, 0]
	# for i, j in enumerate(input_haystack):
	# 	if strStr(input_haystack[i], input_needle[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(strStr(input_haystack[i], input_needle[i]))
	# 	else:
	# 		print("Right")
	# print(strStr(input_haystack[-1], input_needle[-1]))