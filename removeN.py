def removeEven (list):
	for i in list:
		if i % 2 == 0:
			list.remove(i)
	return list
list = [1, 2, 3, 4, 5, 6, 7, 8]
print(removeEven(list))

def removeMultTwo (n):
	list = []
	for i in range(2, n+1):
		list.append(i)
	for p in list:
		# p starts as 2
		# multiplier = 2
		# multiplier = 3
		# ...
		for multiplier in range(2, len(list)):
			if (p * multiplier) in list:
				list.remove(p * multiplier)
				# remove 4, 6, 8, 10... based on multiplier
	return list

print("using mult two\n")
list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(removeMultTwo(120))

def removeMultTwoByCount (n):
	list = []
        for i in range(2, n+1):
                list.append(i)
        for p in list:
		sum = 2 * p
		while sum <= list[-1]:
			if sum in list:
				list.remove(sum)
			sum += p
	return list

print(removeMultTwoByCount(100))
