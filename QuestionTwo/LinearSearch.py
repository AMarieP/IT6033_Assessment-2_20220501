#Linear Search returns Index Number for the Target Record

def LinearSearch(arr, length, target):
    #Can specify the range - does not have to be entire array
    for i in range(0, length):
        if (arr[i] == target):
            return i
        return "The Target Does Not Exist"