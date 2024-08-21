arr = [ 3, 2, 1]
	 #[ 1, 2, 3]
for i in range(len(arr)):
	swapped = False
	for j in range(0, len(arr) - i - 1):

		if arr[j] > arr[j + 1]:
			arr[j], arr[j + 1] = arr[j + 1], arr[j]
			swapped = True
	if swapped == False:
		break

print(arr)
