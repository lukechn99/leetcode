Remove Dups (temporary buffer)
```
def remove_dups(list):
	ptr = list
	trl = ptr
	dict = {}
	while ptr != None:
		if ptr.val in dict:
			dict[ptr.val] += 1
			trl.next = ptr.next
		else:
			dict[ptr.val] = 1
		trl = ptr
		ptr = ptr.next
```
  
Remove Dups (without temporary buffer)
```
def remove_dups2(list):
	list.sort()
	trl = list
	ptr = trl.next
	while ptr != None:
		if ptr.val == trl.val:
			trl.next = ptr.next
		trl = ptr
		ptr = ptr.next
```
  
Return Kth to Last
```
def Kth_to_last(list, k):
	ptr = list
	trl = ptr
	prog = 0
	while ptr != None and prog <= k:
		prog += 1
		trl = ptr
		ptr = ptr.next
	trl.next = ptr.next
```
  
Delete Middle Node
```
def delete_middle(node):
	
```
