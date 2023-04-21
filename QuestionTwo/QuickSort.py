#QUICK SORT

# Function to find the partition position
def Partition(array, key, fst, lst):
    #Pivot
    pivot = array[lst]
    #Pointer
    point = fst - 1
    for j in range(fst, lst):
        #If less than pivot value, swap j to front of array and move pointer
        if key(array[j]) <= key(pivot):
            point = point + 1
            (array[point], array[j]) = (array[j], array[point])
    #When whole arrayay have been traversed swap pointer w pivot
    (array[point + 1], array[lst]) = (array[lst], array[point + 1])
    #Return pivot point to split array
    return point + 1

#Quicksort Function 
def QuickSort(array, key, fst, lst):
    #Terminates function if this condition is met
    if len(array) == 1:
        return array
    if fst < lst:
        #make the parition
        pi = Partition(array, key, fst, lst)
        #Call left of pivot
        QuickSort(array, key, fst, pi - 1)
        #Call right
        QuickSort(array, key, pi + 1, lst)
 
 


