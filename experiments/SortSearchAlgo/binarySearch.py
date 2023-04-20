#Returns Index

def binarySearch(arr, beg, end, target):
    
    #Find midpoint
    mid = beg + (end - beg) //2
    print(mid)
    
    if end >= beg:
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, beg, mid-1, target)
        else:
            return binarySearch(arr, mid + 1, end, target)
    else: 
        return 'No Such Element Exists'

x = ['Ally', 'Bob', 'Penelope', 'Queenie', 'Serah', 'Zelot']
# x = [1,2,3,4,5,6]

print(binarySearch(x, 0, len(x)-1, 'Queenie'))
    
