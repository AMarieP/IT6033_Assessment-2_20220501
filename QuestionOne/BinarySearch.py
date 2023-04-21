#Binary Search using a key to search an arrayay of Student Objects
#Returns index number

def BinarySearch(array, beg, end, target, key):
    
    #Find midpoint
    mid = beg + (end - beg) //2

    if end >= beg:
        if key(array[mid]) == target:
            return mid
        elif key(array[mid]) > target:
            return BinarySearch(array, beg, mid-1, target, key)
        else:
            return BinarySearch(array, mid + 1, end, target, key)
    else: 
        return -1