import numpy as np
from collections import defaultdict

std_list = list()
for i in range(100):
	std_list.append([])
	for j in range(10):
		std_list[i].append(0)


x = 3
y = 3

cnt = 0

num = 8
# row
for i in range(4):
	# column
	sit_num = num
	for j in range(2):
		print(sit_num)
		s = 'CS' + str(sit_num)
		std_list[sit_num][0] = s
		std_list[sit_num][1] = x+(i*10)
		std_list[sit_num][2] = y+(j*10)
		sit_num = num *2
		cnt += 1
	num -= 1
print(type(std_list[8][0]))
	

# print(std_list)

# # square 
# square = {}
# for i in range(100):
# 	square[std_list[i][0]] = std_list[i]

# 	if square.__contains__(i):
# 		print(square[i])
# # print(len(square))
# print(square[8])

# d = defaultdict(list)
# # for i in range(10):
# #     d[0].append(i)
# d[0].append(['a', 'b'])
# print(d[0][0][0])
