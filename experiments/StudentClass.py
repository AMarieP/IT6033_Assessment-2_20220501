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
myTableData["studentID"] = myTableData['fname'].str.slice(start=0, stop=3) + myTableData['lname'].str.slice(start=0, stop=3) + year

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
         return f'{self.__class__.__name__}> (fname: {self.fname}, lname: {self.lname}, email: {self.email}, campus: {self.campus}, studentID: {self.studentID})'

#Turn back to Students
students = [Student(**kwargs) for kwargs in myTableData.to_dict(orient='records')]
print(students)

new1 = Student('Alyssa', 'Pilbrow', 'alyssakvasl', 'Auckl', None)