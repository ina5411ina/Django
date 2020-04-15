from django.http import HttpResponse
import numpy as np
from collections import defaultdict

def sf551(request):
	# 學生資料
	STD_list = list()
	for i in range(100):
		STD_list.append([])
		for j in range(10):
			STD_list[i].append(0)

	# 座位
	seat_list = list()
	for i in range(100):
		seat_list.append([])

# ----------劃座位------------------------------------------------------------
# sf551....................................................................	
	# x +=
	add_height = 50
	# y +=
	add_width = 25

	x = 2
	y = 2

	num = 8
	# row
	for i in range(4):
		# column
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = "CS" + str(seat_num)
			seat_list[seat_num].append(str(seat_name)) #1
			seat_list[seat_num].append(x+(i*10)) #2
			seat_list[seat_num].append(y+(j*10)) #3
			seat_num = num + 8
		num -= 1

	y = y + add_width
	num = 24
	# row 
	for i in range(4):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 8
		num -= 1


	num = 38
	y = y + add_width
	# row 
	for i in range(4):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 6
		num -= 1

	num = 52
	y = y + add_width + 6
	# row 
	for i in range(4):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 8
		num -= 1

	num = 68
	y = y + add_width
	# row 
	for i in range(4):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 8
		num -= 1

	num = 82
	y = y + add_width
	# row 
	for i in range(4):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 6
		num -= 1


	num = 4
	y = 2
	x = x + add_height
	# row 
	for i in range(4):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 8
		num -= 1

	num = 20
	y = y + add_width
	# row 
	for i in range(4):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 8
		num -= 1

	num = 34
	y = y + add_width
	# row 
	for i in range(2):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 6
		num -= 1

	num = 48
	y = y + add_width + 6
	# row 
	for i in range(4):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 8
		num -= 1

	num = 64
	y = y + add_width
	# row 
	for i in range(4):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 8
		num -= 1

	num = 78
	y = y + add_width
	# row 
	for i in range(2):
		# column 
		seat_num = num
		for j in range(2):
			seat_list[seat_num].append(seat_num) #0
			seat_name = 'CS' + str(seat_num)
			seat_list[seat_num].append(seat_name)
			seat_list[seat_num].append(x+(i*10))
			seat_list[seat_num].append(y+(j*10))
			seat_num = num + 6
		num -= 1


	# 導師桌
	num = 90
	seat_list[num].append(num)
	seat_list[num].append('導師桌')
	seat_list[num].append(72)
	seat_list[num].append(52) 

	# 柱子
	num = 91
	seat_list[num].append(num)
	seat_list[num].append('柱子')
	seat_list[num].append(43)
	seat_list[num].append(75) 

	# 白板
	num = 92
	seat_list[num].append(num)
	seat_list[num].append('白板')
	seat_list[num].append(92)
	seat_list[num].append(52) 

	# door
	num = 93
	seat_list[num].append(num)
	seat_list[num].append('門')
	seat_list[num].append(92)
	seat_list[num].append(132) 

	# 工讀生
	num = 94
	seat_list[num].append(num)
	seat_list[num].append('工讀生')
	seat_list[num].append(82)
	seat_list[num].append(155)

# sf551 end......................................................................
# ------------劃座位結束---------------------------------------------------------------
	# square 
	square = defaultdict(list)
	for i in range(100):
		if seat_list[i]:
			square[seat_list[i][0]].append(seat_list[i])


	html = ''
	html += '<html>'

	css = ''
	css += '<style type="text/css">@import url("navigation.css");'
	css += 'body { position:absolute; width:100%; height:100%; margin:1vh; border: 2px;border-style: solid;}'
	css += '.square { position:absolute;text-align: center;width: 10vh;height: 10vh; margin:0; border: 1px;border-style: solid;}'
	css += 'span { font-size: xx-small;}'
	css += 'p {font-size: 2px;margin-top: 5px;margin-bottom: 0px;}'


	for i in range(100):

		if square.__contains__(i):
			# html start
			# 導師桌
			if i == 90:
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'

				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 20vh;height: 10vh; border: 1px;border-style: solid;}'
			
			# 柱子
			elif i == 91:
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'

				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 5vh;height: 5vh; border: 1px;border-style: solid;}'
			
			#白板
			elif i == 92:
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'

				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 20vh;height: 5vh; border: 1px;border-style: solid;}'
			
			#白板
			elif i == 93:
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'

				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 20vh;height: 5vh; border: 1px;border-style: solid;}'

			# 學生座位
			else:
				ID = 'no' + str(i)
				html+= '<div class= "square" id = '+ ID +'>'
				
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '<p>' + str(406261999) + '<br>' + '小可愛</p>'
				html += '</div>'
				

				# css start
				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh;}'


	# css end
	html +=  '</html>'
	css += '</style>'

	S = html + css
	return HttpResponse(S)

def sf645(request):
	# 學生資料
	STD_list = list()
	for i in range(100):
		STD_list.append([])
		for j in range(10):
			STD_list[i].append(0)

	# 座位
	seat_list = list()
	for i in range(100):
		seat_list.append([])

# ----------劃座位------------------------------------------------------------
# sf645....................................................................	

	x = 2
	y = 2 + 27

	num = 1
	# row
	for i in range(10):
		if i%4 == 0 and num != 1:
			y = y + 7 
		seat_list[num].append(num) #0
		seat_name = 'PC' + str(num)
		seat_list[num].append(seat_name)
		seat_list[num].append(x)
		seat_list[num].append(y+(i*10))
		num += 1

	x = x + 15
	y = 2 

	num = 11
	# row
	for i in range(12):
		if i == 2:
			y = y + 7
		elif (i-2)%4 == 0 and num != 0:
			y = y + 7
		seat_list[num].append(num) #0
		seat_name = 'PC' + str(num)
		seat_list[num].append(seat_name)
		seat_list[num].append(x)
		seat_list[num].append(y+(i*10))
		num += 1

	x = x + 15
	y = 2 + 10

	num = 23
	# row
	for i in range(10):
		if i == 1:
			y = y + 7
		elif (i-1)%4 == 0 and num != 0:
			y = y + 7
		seat_list[num].append(num) #0
		seat_name = 'PC' + str(num)
		seat_list[num].append(seat_name)
		seat_list[num].append(x)
		seat_list[num].append(y+(i*10))
		num += 1

	x = x + 15
	y = 2

	num = 33
	
	for i in range(3):
		for i in range(12):
			if num == 63:
				break
			if i == 2:
				y = y + 7
			elif (i--2)%4 == 0 and num != 0:
				y = y + 7
			seat_list[num].append(num) #0
			seat_name = 'PC' + str(num)
			seat_list[num].append(seat_name)
			seat_list[num].append(x)
			seat_list[num].append(y+(i*10))
			num += 1
		x = x + 15
		y = 2

	x = x - 10
	y = 87

	num = 63
	# row
	for i in range(2):
		seat_list[num].append(num) #0
		seat_name = 'PC' + str(num)
		seat_list[num].append(seat_name)
		seat_list[num].append(x)
		seat_list[num].append(y+(i*10))
		num += 1


	# 導師桌
	num = 70
	seat_list[num].append(num)
	seat_list[num].append('導師桌')
	seat_list[num].append(2)
	seat_list[num].append(2)

	# 空桌
	num = 71
	seat_list[num].append(num)
	seat_list[num].append('空桌')
	seat_list[num].append(32)
	seat_list[num].append(2)

	# 空桌
	num = 72
	seat_list[num].append(num)
	seat_list[num].append('柱子')
	seat_list[num].append(32)
	seat_list[num].append(133)

	# door
	num = 73
	seat_list[num].append(num)
	seat_list[num].append('門')
	seat_list[num].append(x)
	seat_list[num].append(138)



# sf645 end......................................................................
# ------------劃座位結束---------------------------------------------------------------
	# square 
	square = defaultdict(list)
	for i in range(100):
		if seat_list[i]:
			square[seat_list[i][0]].append(seat_list[i])


	html = ''
	html += '<html>'

	css = ''
	css += '<style type="text/css">@import url("navigation.css");'
	css += 'body { position:absolute; width:100%; height:100%; margin:1vh; border: 2px;border-style: solid;}'
	css += '.square { position:absolute;text-align: center;width: 10vh;height: 10vh; margin:0; border: 1px;border-style: solid;}'
	css += 'span { font-size: xx-small;}'
	css += 'p {font-size: 2px;margin-top: 5px;margin-bottom: 0px;}'

	for i in range(1, 100):

		if square.__contains__(i):
			# html start
			# 導師桌
			if i == 70:
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'

				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 20vh;height: 10vh; border: 1px;border-style: solid;}'
			# 空桌
			elif i == 71:
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'
				
				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 10vh;height: 10vh; border: 1px;border-style: solid;}'
			
			# 柱子
			elif i == 72:
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'

				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 10vh;height: 10vh; border: 1px;border-style: solid;}'
			# door
			elif i == 73:
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'

				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 5vh;height: 10vh; border: 1px;border-style: solid;}'


			else:
				ID = 'no' + str(i)
				html += '<div class= "square" id = ' + ID + '>'
				
				html += '<span>' + str(square[i][0][1]) + '</span>' 
				html += '<p>' + str(406261999) + '<br>' + '小可愛</p>'
				html += '</div>'
				
				# css start
				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh;}'

			

	# css end
	html +=  '</html>'
	css += '</style>'

	S = html + css
	return HttpResponse(S)


def sf648(request):
	# 學生資料
	STD_list = list()
	for i in range(100):
		STD_list.append([])
		for j in range(10):
			STD_list[i].append(0)

	# 座位
	seat_list = list()
	for i in range(100):
		seat_list.append([])

# ----------劃座位------------------------------------------------------------
# sf648....................................................................	
	x = 2
	y = 2 

	num = 48
	for L in range(3):
		for i in range(2):
			for j in range(8):
				seat_list[num].append(num) #0
				seat_name = 'NT' + str(num)
				seat_list[num].append(seat_name)
				seat_list[num].append(x+(j*10))
				seat_list[num].append(y+(i*10))
				num -= 1

		y += 30

	# door
	num = 50
	seat_list[num].append(num)
	seat_list[num].append('門')
	seat_list[num].append(87)
	seat_list[num].append(90)

	# 導師桌
	num = 51
	seat_list[num].append(num)
	seat_list[num].append('導師桌')
	seat_list[num].append(82)
	seat_list[num].append(2)

	#空桌1
	num = 52
	seat_list[num].append(num)
	seat_list[num].append('空桌1')
	seat_list[num].append(82)
	seat_list[num].append(32)

	#空桌2
	num = 53
	seat_list[num].append(num)
	seat_list[num].append('空桌2')
	seat_list[num].append(82)
	seat_list[num].append(62)


	



# sf648 end......................................................................
# ------------劃座位結束---------------------------------------------------------------
	# square 
	square = defaultdict(list)
	for i in range(100):
		if seat_list[i]:
			square[seat_list[i][0]].append(seat_list[i])


	html = ''
	html += '<html>'

	css = ''
	css += '<style type="text/css">@import url("navigation.css");'
	css += 'body { position:absolute; width:100%; height:100%; margin:1vh; border: 2px;border-style: solid;}'
	css += '.square { position:absolute;text-align: center;width: 10vh;height: 10vh; margin:0; border: 1px;border-style: solid;}'
	css += 'span { font-size: xx-small;}'
	css += 'p {font-size: 2px;margin-top: 5px;margin-bottom: 0px;}'

	for i in range(1, 100):

		if square.__contains__(i):
			# html start
			# door
			if i == 50:
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'
				
				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 5vh;height: 10vh; border: 1px;border-style: solid;}'

			elif i == 51 :
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'
				
				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 20vh;height: 10vh; border: 1px;border-style: solid;}'

			elif i == 52 :
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'
				
				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 20vh;height: 10vh; border: 1px;border-style: solid;}'

			elif i == 53 :
				ID = 'no' + str(i)
				html+= '<div id = '+ ID +'>'
				html += '<span>' + 	str(square[i][0][1]) + '</span>' 
				html += '</div>'
				
				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh; position:absolute;text-align: center;width: 20vh;height: 10vh; border: 1px;border-style: solid;}'


			else:
				ID = 'no' + str(i)
				html += '<div class= "square" id = ' + ID + '>'
				
				html += '<span>' + str(square[i][0][1]) + '</span>' 
				html += '<p>' + str(406261999) + '<br>' + '小可愛</p>'
				html += '</div>'
				

				# css start
				css += '#'+ ID + '{ margin:0; margin-top:' + str(square[i][0][2]) + 'vh; margin-left:' + str(square[i][0][3]) + 'vh;}'

	# css end
	html +=  '</html>'
	css += '</style>'

	S = html + css
	return HttpResponse(S)