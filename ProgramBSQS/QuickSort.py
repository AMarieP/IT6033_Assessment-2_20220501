#QUICK SORT

# Function to find the partition position
def Partition(arr, key, fst, lst):
    #Pivot
    pivot = arr[lst]
    #Pointer
    point = fst - 1
    for j in range(fst, lst):
        #If less than pivot value, swap j to front of arr and move pointer
        if key(arr[j]) <= key(pivot):
            point = point + 1
            (arr[point], arr[j]) = (arr[j], arr[point])
    #When whole array have been traversed swap pointer w pivot
    (arr[point + 1], arr[lst]) = (arr[lst], arr[point + 1])
    #Return pivot point to split arr
    return point + 1

#Quicksort Function 
def QuickSort(arr, key, fst, lst):
    #Terminates function if this condition is met
    if len(arr) == 1:
        return arr
    if fst < lst:
        #make the parition
        pi = Partition(arr, key, fst, lst)
        #Call left of pivot
        QuickSort(arr, key, fst, pi - 1)
        #Call right
        QuickSort(arr, key, pi + 1, lst)
 
 


