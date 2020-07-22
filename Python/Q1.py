import math

def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	else:
		for i in range(2, int(math.sqrt(n)+1)):
			if n % i == 0:
				return False
				break
		return True


def twin_prime(n):
	l = 10 ** (n-1)
	u = 10 ** n
	twins = []
	for i in range(l, u-2):
		if is_prime(i) and is_prime(i+2):
			twins.append(str(i) + ' ')
			twins.append(str(i+2))
			twins.append('\n')
	return twins


n = int(input())
file = open("myFirstFile.txt","w") 
file.writelines(twin_prime(n))
file.close() 