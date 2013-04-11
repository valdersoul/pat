first =  input() 
second = input() 
array = first.split()
sample = second.split()

number = int( array[0] )
move = int( array[1] )
arrayout = []


while (move > number):
	move -= number
	pass

for x in range(1,2*number-1,2):
	sample.insert(x,' ')
	pass
	
if (move == number):
	for x in sample:
		print(x,end='')
		pass
	pass
else:
	arrayout = sample[:]
	for x in range(0, 2*number, 2):
		if( (-move)*2+x+1 < 0 ):
			arrayout[x] = sample[(-move)*2+x+1]
		else:
			arrayout[x] = sample[(-move)*2+x]
	for x in arrayout:
		print(x,end='')
		pass