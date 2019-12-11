# -*- coding: utf-8 -*-
# this file has been found bug

import math



p = [
	(	35	,	29	), 
	(	13	,	38	), 
	(	25	,	62	), 
	(	83	,	10	), 
	(	62	,	82	), 
	(	71	,	28	), 
	(	32	,	16	), 
	(	34	,	48	), 
	(	35	,	55	), 
	(	40	,	32	), 
	(	1	,	60	), 
	(	22	,	66	), 
	(	9	,	32	), 
	(	78	,	23	), 
	(	68	,	19	), 
	(	25	,	5	), 
	(	53	,	69	), 
	(	73	,	72	), 
	(	99	,	97	), 
	(	66	,	4	), 
	(	26	,	23	), 
	(	40	,	93	), 
	(	70	,	90	)]



def distance(a, b):
	return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))



def brute_force(x, n):
	min_dis = distance(x[0], x[1])
	for i in range(0, n - 1):
		for j in range(i + 1, n):
			if distance(x[i], x[j]) < min_dis:
				min_dis = distance(x[i], x[j])
	return min_dis



def strip_closest(strip, dis):
	if strip.__len__() <= 1:
		return dis
	min_dis = dis
	for i in range(0, strip.__len__()):
		for j in range(i + 1, 8):
			if i + j < strip.__len__():
				min_dis = min(min_dis, distance(strip[i], strip[j]))
	return min_dis



def closest_pair(x, y, n):
	if n <= 3:
		return brute_force(x, n)
	
	mid = n // 2
	y_left = []
	y_right = []
	for p in y:
		if p in x[:mid]:
			y_left.append(p)
		else:
			y_right.append(p)
	dis_left = closest_pair(x[:mid], y_left, mid)
	dis_right = closest_pair(x[mid:], y_right, n - mid)
	min_dis = min(dis_left, dis_right)
	
	strip = []
	for p in y:
		if (abs(p[0] - x[mid][0]) < min_dis):
			strip.append(p)
	min_dis = min(min_dis, strip_closest(strip, min_dis))

	return min_dis



def closest(p, n):
	x = sorted(p)
	y = sorted(p, key = lambda x:x[1])
	return closest_pair(x, y, n)



if __name__ == "__main__":
	print("force result:\t", brute_force(p, 23))
	print("divide result:\t", closest(p, 23))
	