import timeit, cProfile
from Database import students
from Student import Student
from BinarySearch import BinarySearch
from LinearSearch import LinearSearch

#Does BigO 
from bigO import BigO
from random import randint
lib = BigO()



# #Calc Big O

# #Linear Search
# def BigOLinearSearch(array, length, key, target):
#     for i in range(0, length): #(n * 2 step) + 1
#         if (key(array[i]) == target): #1 step
#             return i #1 step
#         return -1 #1 step


# #Binary Serach
def BigOBinarySearch(array, beg, end, target):
    
    #Find midpoint
    mid = beg + (end - beg) //2 #1 Step

    while end >= beg: #1 Step
        if (array[mid]) == target:
            return mid
        elif (array[mid]) > target:
            return BinarySearch(array, beg, mid-1, target)
        else:
            return BinarySearch(array, mid + 1, end, target)
    return -1

# arr = [1,2,3,4,14,15,16,17,18,19,20,5,6,7,8,9,10,11,12,13,1,2,3,4,14,15,16,17,18,19,20,5,6,7,8,9,10,34,11,12,13,1,2,3,4,14,15,16,17,18,19,20,5,6,7,8,9,10,11,12,13,1,2,3,4,14,15,16,17,18,19,20,5,6,7,8,9,10,11,12,13,1,2,3,4,14,15,16,17,18,19,20,5,6,7,8,9,10,11,12,13,1,2,3,4,14,15,16,17,18,19,20,5,6,7,8,9,10,11,12,13,1,2,3,4,14,15,16,17,18,19,20,5,6,7,8,9,10,11,12,13]
 
# cProfile.run('BinarySearch(0, len(arr)-1, 34, arr)')
# print(BinarySearch(0, len(arr)-1, 34, arr))



