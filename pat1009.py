sentence = input()
words = sentence.split()
out = []

words.reverse()
for x in words:
	out.append(x)
	out.append(' ')
	pass
out.pop()
for x in out:
	print(x, end = '')
	pass