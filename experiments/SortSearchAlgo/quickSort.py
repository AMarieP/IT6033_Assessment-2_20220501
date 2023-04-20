# Function to find the partition position
def partition(arr, fst, lst):
    #Pivot
    pivot = arr[lst]
    #Pointer
    point = fst - 1
    for j in range(fst, lst):
        #If less than pivot value, swap j to front of arr and move pointer
        if arr[j] <= pivot:
            point = point + 1
            (arr[point], arr[j]) = (arr[j], arr[point])
    #When whole array have been traversed swap pointer w pivot
    (arr[point + 1], arr[lst]) = (arr[lst], arr[point + 1])
    #Return pivot point to split arr
    return point + 1

#Quicksort Function 
def quickSort(arr, fst, lst):
    #Terminates function if this condition is met
    if len(arr) == 1:
        return arr
    if fst < lst:
        #make the parition
        pi = partition(arr, fst, lst)
        #Call left of pivot
        quickSort(arr, fst, pi - 1)
        #Call right
        quickSort(arr, pi + 1, lst)
 
 
data = ['Amy', 'Ethan', 'Amelia', 'Josiah', 'Melanie', 'Joanne', 'Dolly'] 

size = len(data)
quickSort(data, 0, size - 1)
print(data)