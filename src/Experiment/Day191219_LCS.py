# -*- coding: utf-8 -*-



def lcs_dp(str0, str1):
	str0 = ' ' + str0
	str1 = ' ' + str1
	f = [[0 for j in range(len(str1))] for i in range(len(str0))]
	
	# f[i][j]表示str0[:i+1]与str1[:j+1] 的最长公共子序列
	# DP方程：
	#				0							, i == 0 or j == 0
	# f[i][j] = {	f[i-1][j-1] + 1				, str0[i] == str1[j]
	#				max(f[i-1][j], f[i][j-1])	, str0[i] != str1[j]
	for i in range(1, len(str0)):
		for j in range(1, len(str1)):
			if str0[i] == str1[j]:
				f[i][j] = f[i - 1][j - 1] + 1
			else:
				f[i][j] = max(f[i][j - 1], f[i - 1][j])

	# for a in f:
	# 	 print(a)
	
	# 根据dp表求得最长公共子序列
	substr = ""
	x = len(str0) - 1
	y = len(str1) - 1
	while f[x][y] > 0:
		if (str0[x] == str1[y]) and (f[x][y] == f[x - 1][y - 1] + 1):
			substr = str0[x] + substr
			x -= 1
			y -= 1
		else:
			if f[x - 1][y] == f[x][y]:
				x -= 1
			else:
				y -= 1

	return substr



if __name__ == "__main__":
	print(lcs_dp(input(), input()))
