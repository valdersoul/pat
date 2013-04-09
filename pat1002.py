number = input()
sum = sum( map ( int, number ))
number = sum
digital=[]
while (sum != 0):
	number = sum % 10
	if  (number == 1):
		digital.append(' ')
		digital.append('yi')
	elif (number == 2):
		digital.append(' ')
		digital.append('er')
	elif (number == 3):
		digital.append(' ')
		digital.append('san')
	elif (number == 4):
		digital.append(' ')
		digital.append('si')
	elif (number == 5):
		digital.append(' ')
		digital.append('wu')
	elif (number == 6):
		digital.append(' ')
		digital.append('liu')
	elif (number == 7):
		digital.append(' ')
		digital.append('qi')
	elif (number == 8):
		digital.append(' ')
		digital.append('ba')
	elif (number == 9):
		digital.append(' ')
		digital.append('jiu')
	elif (number == 0):
		digital.append(' ')
		digital.append('ling')
	sum = sum // 10								
else :
	digital.reverse()
	digital.pop()
	for x in digital:
		print(x, end='')