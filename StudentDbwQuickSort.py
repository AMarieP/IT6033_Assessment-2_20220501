import pandas as pd
from datetime import date


#Get the Year
thisYear = date.today().year

#Get data from txt file and turn it into a DataFrame
studentTable = "smallDB.txt"
results = []
with open(studentTable) as f:
    line = f.readline()
    while line:
        results.append(line.strip().split(","))
        line = f.readline()
f.close()
myTableData = pd.DataFrame(results, columns = ["fname", "lname", 'email', 'campus'])
#Generate a StudentID
myTableData["studentID"] = myTableData['fname'].str.slice(start=0, stop=3) + myTableData['lname'].str.slice(start=0, stop=3) + str(thisYear)

#Function to generate a student ID
def GenerateID(studentID, fname, lname):
        thisYear = date.today().year
        if studentID == None:
            studentID = fname[0:3] + lname[0:3] + str(thisYear)
            return studentID
        else:
            return studentID

#Student Class
class Student:
    def __init__(self, fname, lname, email, campus, studentID):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.campus = campus
        self.studentID = GenerateID(studentID, self.fname, self.lname)
    
    def __repr__(self):
         return f'{self.__class__.__name__}:\n First Name: {self.fname}, Last Name: {self.lname}, Email: {self.email}, Campus: {self.campus}, ID: {self.studentID}:\n'

    def get_first_name(self):
        return self.fname

#Turn back to Students
students = [Student(**kwargs) for kwargs in myTableData.to_dict(orient='records')]
print(students)

new1 = Student('Alyssa', 'Pilbrow', 'alyssakvasl', 'Auckl', None)

print(new1)

# Function to find the partition position
def partition(arr, key, fst, lst):
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
def quickSort(arr, key, fst, lst):
    #Terminates function if this condition is met
    if len(arr) == 1:
        return arr
    if fst < lst:
        #make the parition
        pi = partition(arr, key, fst, lst)
        #Call left of pivot
        quickSort(arr, key, fst, pi - 1)
        #Call right
        quickSort(arr, key, pi + 1, lst)
 
 

size = len(students)
quickSort(students, Student.get_first_name, 0, size - 1)
print(students)