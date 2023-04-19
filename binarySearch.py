#Returns Index

def binarySearch(arr, beg, end, target):
    
    #Find midpoint
    mid = beg + (end - 1) //2
    
    if end >= beg:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, beg, mid-1, target)
        else:
            return binarySearch(arr, mid + 1, end, target)
    else: 
        return 'No Such Element Exists'

x = [1,2,3,4,5,6,7,8,9,10]

print(binarySearch(x, 0, len(x)-1, 99))
    
