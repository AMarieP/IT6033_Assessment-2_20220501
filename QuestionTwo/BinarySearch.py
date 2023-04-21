#Binary Search using a key to search an array of Student Objects
#Returns index number

def BinarySearch(arr, beg, end, target, key):
    
    #Find midpoint
    mid = beg + (end - beg) //2

    if end >= beg:
        if key(arr[mid]) == target:
            return mid
        elif key(arr[mid]) > target:
            return BinarySearch(arr, beg, mid-1, target, key)
        else:
            return BinarySearch(arr, mid + 1, end, target, key)
    else: 
        return -1