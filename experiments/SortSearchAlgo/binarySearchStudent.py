def binarySearch(arr, beg, end, target, key):
    
    #Find midpoint
    mid = beg + (end - beg) //2

    if end >= beg:
        if key(arr[mid]) == target:
            return mid
        elif key(arr[mid]) > target:
            return binarySearch(arr, beg, mid-1, target, key)
        else:
            return binarySearch(arr, mid + 1, end, target, key)
    else: 
        return 'No Such Element Exists'

x = binarySearch(students, 0, len(students)-1, 'Ethan', Student.get_first_name)

print(students[x])