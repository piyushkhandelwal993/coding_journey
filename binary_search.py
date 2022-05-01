def binary(arr,x,start ,end):
	
	if start > end:
		return -1

	mid = (start + end)//2
	if(arr[mid]==x):
		return mid
	elif(arr[mid]>x):
		return binary(arr,x,start,mid-1)
	else:
		return binary(arr,x,mid+1,end)

	