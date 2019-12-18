# -*- coding: utf-8 -*-



def delete_problem(num: str, k:int):
	f = list(map(lambda x: int(x), num))	# 将字符串转化为整数列表
	f.append(-1)							# 在末尾添加数字-1，可降低代码复杂度

	i = 1									# 当前处理列表下标
	j = 0									# 已删除数量
	while j < k:							# 当删除数量小于目标量
		if f[i - 1] > f[i]:					# 若当前数字小于前一个数字，则删除前一个数字
			del f[i - 1]
			i -= 1
			j += 1
		else:								# 否则继续判断列表中下一个数字
			i += 1

	# 将结果转化为字符串（以便于显示以0开头的数字），同时注意排除列表末尾的数字-1
	return "".join([str(x) for x in f[: f.__len__() - 1]])
	



if __name__ == "__main__":
	# 输入目标数字
	print("Please Input Target Number:", end = "\n  ")
	num = input().strip()

	# 输入删除数量
	print("Please Input k ∈ [0, ", num.__len__(), "):", sep = "", end = "\n  ")
	k = int(input())

	# 输出结果
	print("After Deleteing Number(s):", end = "\n  ")
	print(delete_problem(num, k))
