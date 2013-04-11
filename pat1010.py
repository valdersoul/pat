sample = input()
duoxiangshi = sample.split()
out = []

if (duoxiangshi[-1] == duoxiangshi[-2] ):
	number = duoxiangshi.index(duoxiangshi[-1]) + 1
else:
	number = duoxiangshi.index(duoxiangshi[-1])


if (number == 1 and int(duoxiangshi[1]) == 0):
	out.append(0)
	out.append(' ')
	out.append(0)
	out.append(' ')
	pass
else:
	for x in range(1, number + 1, 2):
		if ( int(duoxiangshi[x]) == 0):
			continue
		else :
			out.append(int(duoxiangshi[x - 1]) * int(duoxiangshi[x]))
			out.append(' ')
			out.append(int(duoxiangshi[x]) - 1)
			out.append(' ')
			pass
		pass

out.pop()
for x in out:
	print(x, end='')
	pass