#100
def isSameTree(p, q):
	def levelOrderTraversal(TreeNode):
		"""
		rtype: left_list, right_list
		highest_treenode belongs to left_list
		"""
		level_order_treenode_left = [TreeNode]
		level_order_treenode_right = []
		m, n, last_len = 0, 0, 0
		while last_len != len(level_order_treenode_left + level_order_treenode_right):
			last_len, l, r = len(level_order_treenode_left + level_order_treenode_right), m, n
			level_order_treenode = level_order_treenode_left[m:] + level_order_treenode_right[n:]
			for i in range(len(level_order_treenode)):
				if level_order_treenode[i].left != None:
					level_order_treenode_left.append(level_order_treenode[i].left)
				else:
					level_order_treenode_left.append(None)
				if level_order_treenode[i].right != None:
					level_order_treenode_right.append(level_order_treenode[i].right)
				else:
					level_order_treenode_right.append(None)
				if level_order_treenode[i] in level_order_treenode_left:
					m += 1
				else:
					n += 1
		return level_order_treenode_left, level_order_treenode_right

	if p is None or q is None:
		if p is None and q is None:
			return True
		else:
			return False
	else:
		p_list_left, p_list_right = levelOrderTraversal(p)
		q_list_left, q_list_right = levelOrderTraversal(q)
		if len(p_list_left) != len(q_list_left) or len(p_list_right) != len(q_list_right):
			return False
		p_list, q_list = p_list_left + p_list_right, q_list_left + q_list_right
		for i in range(len(p_list)):
			if p_list[i].val != q_list[i].val:
				return False
		return True

#101
def isSymmetric(root):
	def mirrorTree(tree_node):
		if type(tree_node) != TreeNode:
			return 
		else:
			checked_treenode = 0
			treenode_list = [tree_node]
			while checked_treenode != len(treenode_list):
				level_treenode = treenode_list[checked_treenode:]
				for node in level_treenode:
					if node != None:
						if node.left == None and node.right == None:
							pass
						elif node.left != None or node.right != None:
							_ = node.left
							node.left, node.right = node.right, _
							if node.left != None:
								treenode_list.append(node.left)
							if node.right != None:
								treenode_list.append(node.right)
					checked_treenode += 1
			return tree_node
	def TreeNode2List(tree_node):
		if type(tree_node) != TreeNode:
			return []
		else:
			checked_treenode = 0
			treenode_list = [tree_node]
			while checked_treenode != len(treenode_list):
				level_treenode = treenode_list[checked_treenode:]
				for treenode in level_treenode:
					if treenode != None:
						if treenode.left != None:
							treenode_list.append(treenode.left)
						else:
							treenode_list.append(None)
						if treenode.right != None:
							treenode_list.append(treenode.right)
						else:
							treenode_list.append(None)
					checked_treenode += 1
			for _ in range(len(treenode_list)):
				if treenode_list[-1] == None:
					treenode_list.pop(-1)
				else:
					break
			for i in range(len(treenode_list)):
				if treenode_list[i] != None:
					treenode_list[i] = treenode_list[i].val
			return treenode_list
	original_list = TreeNode2List(root)
	mirror_tree = mirrorTree(root)
	if not mirror_tree:
		return True
	else:
		if original_list == TreeNode2List(mirror_tree):
			return True
		else:
			return False

#104
def maxDepth(root):
	if type(root) != TreeNode:
		return 0
	else:
		checked_treenode, depth = 0, 0
		treenode_list = [root]
		while checked_treenode != len(treenode_list):
			alive_node = len(treenode_list)
			level_treenode = treenode_list[checked_treenode:]			
			for node in level_treenode:
				if node != None:
					if node.left != None:
						treenode_list.append(node.left)
					else:
						treenode_list.append(None)
					if node.right != None:
						treenode_list.append(node.right)
					else:
						treenode_list.append(None)
				checked_treenode += 1
			if len(treenode_list) > alive_node:
				depth += 1
		return depth

#107
def levelOrderBottom(root):
	pass

if __name__ == '__main__':
	class TreeNode:
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None

	def List2TreeNode(nums):
		"""
		nums: List
		rtype: highest TreeNode
		"""
		if len(nums)==0:
			return
		else:
			alive_node, checked_num = 0, 1 #int: by level
			treenode = [TreeNode(nums[0])]
			while alive_node != len(treenode):
				level_treenode = treenode[alive_node:] #list
				if checked_num <= len(nums):
					rest_nums = nums[checked_num:]
				else:
					break
				for i in range(len(level_treenode)):			
					if i*2 <= len(rest_nums) -1 :
						if rest_nums[i*2] != None:
							treenode[alive_node].left = TreeNode(rest_nums[i*2])
							treenode.append(treenode[alive_node].left)
					if i*2 <= len(rest_nums) -2 :
						if rest_nums[i*2+1] != None:
							treenode[alive_node].right = TreeNode(rest_nums[i*2+1])
							treenode.append(treenode[alive_node].right)
					checked_num += 2
					alive_node += 1
			return treenode[0]

	def TreeNode2List(tree_node):
		if type(tree_node) != TreeNode:
			return []
		else:
			checked_treenode = 0
			treenode_list = [tree_node]
			while checked_treenode != len(treenode_list):
				level_treenode = treenode_list[checked_treenode:]
				for treenode in level_treenode:
					if treenode != None:
						if treenode.left != None:
							treenode_list.append(treenode.left)
						else:
							treenode_list.append(None)
						if treenode.right != None:
							treenode_list.append(treenode.right)
						else:
							treenode_list.append(None)
					checked_treenode += 1
			for _ in range(len(treenode_list)):
				if treenode_list[-1] == None:
					treenode_list.pop(-1)
				else:
					break
			for i in range(len(treenode_list)):
				if treenode_list[i] != None:
					treenode_list[i] = treenode_list[i].val
			return treenode_list

	#100
	# input_p_list = [
	# [1,2],
	# [],
	# [10,5,15],
	# [2, None, 4],
	# [0],
	# [1,None,2,3],
	# [390,255,2266,-273,337,1105,3440,-425,4113,None,None,600,1355,3241,4731,-488,-367,16,None,565,780,1311,1755,3075,3392,4725,4817,None,None,None,None,-187,152,395,None,728,977,1270,None,1611,1786,2991,3175,3286,None,164,None,None,4864,-252,-95,82,None,391,469,638,769,862,1045,1138,None,1460,1663,None,1838,2891,None,None,None,None,3296,3670,4381,None,4905,None,None,None,-58,None,None,None,None,None,None,None,None,734,None,843,958,None,None,None,1163,1445,1533,None,None,None,2111,2792,None,None,None,3493,3933,4302,4488,None,None,None,None,None,None,819,None,None,None,None,1216,None,None,1522,None,1889,2238,2558,2832,None,3519,3848,4090,4165,None,4404,4630,None,None,None,None,None,None,1885,2018,2199,None,2364,2678,None,None,None,3618,3751,None,4006,None,None,4246,None,None,4554,None,None,None,1936,None,None,None,None,2444,2642,2732,None,None,None,None,None,None,None,4253,None,None,None,None,2393,2461,None,None,None,None,4250,None,None,None,None,2537]]
	# input_q_list = [
	# [1,None,2],
	# [],
	# [10,5,None,None,15],
	# [2,3,4],
	# [0],
	# [1,None,2,None,3],
	# [390,255,2266,-273,337,1105,3440,-425,4113,None,None,600,1355,3241,4731,-488,-367,16,None,565,780,1311,1755,3075,3392,4725,4817,None,None,None,None,-187,152,395,None,728,977,1270,None,1611,1786,2991,3175,3286,None,164,None,None,4864,-252,-95,82,None,391,469,638,769,862,1045,1138,None,1460,1663,None,1838,2891,None,None,None,None,3296,3670,4381,None,4905,None,None,None,-58,None,None,None,None,None,None,None,None,734,None,843,958,None,None,None,1163,1445,1533,None,None,None,2111,2792,None,None,None,3493,3933,4302,4488,None,None,None,None,None,None,819,None,None,None,None,1216,None,None,1522,None,1889,2238,2558,2832,None,3519,3848,4090,4165,None,4404,4630,None,None,None,None,None,None,1885,2018,2199,None,2364,2678,None,None,None,3618,3751,None,4006,None,None,4246,None,None,4554,None,None,None,1936,None,None,None,None,2444,2642,2732,None,None,None,None,None,None,None,4253,None,None,None,None,2461,2393,None,None,None,None,4250,None,None,None,None,2537]]
	# expected_output = [False, True, False, False, True, False, False]
	
	# for i in range(len(input_p_list)):
	# 	print(List2TreeNode(input_p_list[i]))

	# print(TreeNode2List(List2TreeNode([10,5,None,None,15,1])))

	# for i in range(len(input_p_list)):
	# 	if isSameTree(List2TreeNode(input_p_list[i]), List2TreeNode(input_q_list[i])) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(TreeNode2List(isSameTree(List2TreeNode(input_p_list[i]), List2TreeNode(input_q_list[i]))))
	# 	else:
	# 		print("Right")

	# print(isSameTree(List2TreeNode(input_p_list[-1]), List2TreeNode(input_q_list[-1])))

	#101
	# input_treenode = [
	# [1,2,7,3,4,4,3],
	# [1,2,2,None,3,3],
	# [1,2,2,None,3,None,3]]
	# expected_output = [True, True, False]
	# for i in range(len(input_treenode)):
	# 	if isSymmetric(List2TreeNode(input_treenode[i])) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(isSymmetric(List2TreeNode(input_treenode[i])))
	# 	else:
	# 		print("Right")
	# print(isSymmetric(List2TreeNode(input_treenode[-1])))

	#104
	# input_nums = [[3,9,20,None,None,15,7]]
	# expected_output = [3]
	# for i in range(len(input_nums)):
	# 	if maxDepth(List2TreeNode(input_nums[i])) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(maxDepth(List2TreeNode(input_nums[i])))
	# 	else:
	# 		print("Right")		
	# print(maxDepth(List2TreeNode(input_nums[-1])))

	#107
	input_nums = [[3,9,20,None,None,15,7]]
	expected_output = [[[15,7],[9,20],[3]]]
	for i in range(len(input1)):
		if levelOrderBottom(List2TreeNode(input_nums[i])) != expected_output[i]:
			print("Wrong!!!")
			print(levelOrderBottom(List2TreeNode(input_nums[i])))
		else:
			print("Right")		
	# print(levelOrderBottom(List2TreeNode(input_nums[-1])))