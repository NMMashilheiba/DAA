arr = [1, 5, 2, 3, 0]

for i in range(0, len(arr) - 1):

	# mini = arr[0]
	j = i + 1
	while j < len(arr):
		if arr[j] < arr[i]:
			# temp = arr[i]
			# arr[i] = arr[j]
			# arr[j] = temp

			arr[i], arr[j] = arr[j], arr[i]		# Swpping the two numbers
			print(arr)
		j += 1
# print(arr)