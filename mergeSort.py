
def mergeSort(arr):
	global c
	# print("count: ", c)		
	
	if len(arr) > 1:
		
		c += 1

		leftArr = arr[ :len(arr) // 2]
		print("leftArr: ", leftArr)
		rightArr = arr[len(arr) // 2: ]
		print("rightArr: ", rightArr)

		# Recursive splliting:
		mergeSort(leftArr)
		mergeSort(rightArr)


		# Merging part:
		i = 0
		j = 0
		k = 0

		while i < len(leftArr) and j < len(rightArr):
			if leftArr[i] < rightArr[j]:
				arr[k] = leftArr[i]
				i += 1
				k += 1
				# print("partial sort leftArr: ", leftArr)
			else:
				arr[k] = rightArr[j]
				j += 1
				k += 1
				# print("partial sort rightArr: ", rightArr)
		print("partial sorted Array: ", leftArr, rightArr)


		while i < len(leftArr):
			arr[k] = leftArr[i]
			i += 1
			k += 1
			# print("partial srt leftArr: ",leftArr)

		while j < len(rightArr):
			arr[k] = rightArr[j]
			j += 1
			k += 1
			# print("partial sort rightArr: ", rightArr)
	else:
		print("ret: ", arr)
		return arr

arr = [1, 9, 4, 5, 3, 2]
c = 0

mergeSort(arr)
print(arr)
