# bubble sort

size = input("Enter The Number Of Elements : ")
arr = []
for i in range(0, size):
	arr.append(input("Enter The Element : "))

# sort in ascending order
for i in range(0, size-1):
	for j in range(0, size-1-i):
		if arr[j]>arr[j+1]:
			arr[j], arr[j+1] = arr[j+1], arr[j]
print "Ascending Order  : ", arr

# sort in descending order
for i in range(0, size-1):
	for j in range(0, size-1-i):
		if arr[j]<arr[j+1]:
			arr[j], arr[j+1] = arr[j+1], arr[j]
print "Descending Order : ", arr
