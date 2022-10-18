def test(numbers):
	b = [x for x in numbers]
	vals = [0 for x in numbers]
	for i in range(int((len(numbers)+1)/2)):
		b[i*2] = numbers[i]

	for i in range(1, int(len(numbers)/2)+1):
		print(i, len(numbers)-(i))
		b[i*2-1] = numbers[len(numbers)-(i)]
	print(b)

	for i in range(1, len(numbers)):
		if (b[i-1]<b[i]):
			vals[i]=True
			print(True)
		else:
			vals[i]=False
			return(False)
	print(all(vals))
	return(all(vals))

numbers = [23, 41, 71, 71, 12, 56]
print(test(numbers))

	
	
