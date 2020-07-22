def is_palindrome(n):
	num_str = str(n)
	if num_str == num_str[::-1]:
		return True
	else:
		return False

def next_palindrome(n):
	curr_num = n + 1
	while True:
		if is_palindrome(curr_num):
			return curr_num
			break
		curr_num += 1


n = int(input())
print(next_palindrome(n))