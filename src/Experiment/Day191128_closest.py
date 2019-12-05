# -*- coding: utf-8 -*-

import math



def calc_distance(a, b):
	return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))



def closest_force(f, n):
	min_dis = calc_distance(f[0], f[1])
	for i in range(len(f) - 1):
		for j in range(i + 1, len(f)):
			min_dis = min(min_dis, calc_distance(f[i], f[j]))
	return min_dis



def strip_closest(arrleft, arrright, min_dis):
	lenleft = arrleft.__len__()
	lenright = arrright.__len__()
	if lenleft == 0 or lenright == 0:
		return min_dis
	
	for pleft in arrleft:
		pos = 0
		while pleft[1] > arrright[pos][1]:
			pos += 1
			if pos >= lenright:
				break
		if pos < 4:
			pos = 0
		else:
			pos -= 4
		for i in range(pos, min(pos + 8, lenright)):
			min_dis = min(min_dis, calc_distance(pleft, arrright[i]))
	return min_dis



def closest_dichotomy(xarr, yarr, n):
	if n <= 3:
		return closest_force(xarr, n)
	
	mid = n // 2
	y_left = []
	y_right = []
	for p in yarr:
		if p in xarr[:mid]:
			y_left.append(p)
		else:
			y_right.append(p)
	
	dis_left = closest_dichotomy(xarr[:mid], y_left, mid)
	dis_right = closest_dichotomy(xarr[mid:], y_right, n - mid)
	min_dis = min(dis_left, dis_right)

	strip_left = []
	strip_right = []
	for p in y_left:
		if (abs(p[0] - xarr[mid][0]) < min_dis):
			strip_left.append(p)
	for p in y_right:
		if (abs(p[0] - xarr[mid][0]) < min_dis):
			strip_right.append(p)
	
	min_dis = min(min_dis, strip_closest(strip_left, strip_right, min_dis))

	return min_dis



def closest(f, n):
	xarr = sorted(f)
	yarr = sorted(f, key = lambda f:f[1])
	return closest_dichotomy(xarr, yarr, n)



def input_data():
	try:
		infile = open('closest.in', 'r')
		n = int(infile.readline())
		f = [[] for i in range(n)]
		for i in range(n):
			f[i] = [int(a) for a in infile.readline().split()]
		infile.close()
	except IOError:
		n = int(input())
		f = [[] for i in range(n)]
		for i in range(n):
			f[i] = [int(a) for a in input().split()]

	return f



if __name__ == "__main__":
	f = input_data()
	print("force result:\t", closest_force(f, f.__len__()))
	print("divide result:\t", closest(f, f.__len__()))
