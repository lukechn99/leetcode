# given a rule that you can take one or two steps at a time
def climb(N):
	if (N == 0):
		return 1
	if (N == 1):
		return 1
	else:
		return climb(N - 1) + climb(N - 2)

print(str(climb(4))  + " should be 5\n")
