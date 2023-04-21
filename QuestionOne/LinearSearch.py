#Linear Search returns Index Number for the Target Record

def LinearSearch(array, length, key, target):
    #Can specify the range - does not have to be entire array
    for i in range(0, length):
        if (key(array[i]) == target):
            return i
        return -1