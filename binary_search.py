def binary(arr,x):
	start = 0
	end = len(arr)-1
	while(start <= end):
		mid = (start + end)//2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			end = mid - 1
		else:
			start = mid + 1
	return -1