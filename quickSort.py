# Quick sort
def quickSort(arr, left, right):
	if left < right:
		pivot = partition(arr, left, right)
		quickSort(arr, left, pivot - 1)
		quickSort(arr, pivot + 1, right)

def partition(arr, left, right):
	# left is the leftmost element of the array, right is the pivot

	i = left
	j = right - 1
	pivot = arr[right]

	while i < j:
		while i < right and arr[i] < pivot:
			i += 1
		while j > left and arr[j] >= pivot:
			j -= 1
		if i < j:
			arr[i], arr[j] = arr[j], arr[i]
	if arr[i] > pivot:
		arr[i], arr[right] = arr[right], arr[i]

	return i

	
arr = [ 1, 4, 2, 9, 6, 7]
quickSort(arr, 0, len(arr) - 1)
print(arr)