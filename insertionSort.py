
arr = [1, 3, 2, 0]

for i in range(1, len(arr)):
	key = arr[i]
	j = i - 1

	while j >= 0 and key < arr[j]:
		# temp = arr[j]
		# arr[j] = key

		arr[j + 1] = arr[j]		# Swapping the two adj. elements 
								# (i.e. smaller value "key", with 
								# the larger left adj. value)
		j -= 1

	arr[j + 1] = key			# Putting the key in place

print(arr)


for i in range(1, len(arr)):
	key = arr[i]
	j = i - 1

	while j >= 0 and key < arr[j]:
		arr[j + 1] = arr[j]
		j -= 1

	arr[j + 1] = key

print(arr)



