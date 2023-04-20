#Creates Array of Student Objects from .txt using Pandas
import pandas as pd
import datetime


#Get the Year
today = datetime.date.today()
year = str(today.year)

#Reads the txt file and turns to dataframe
studentTable = "Program\smallDB.txt"
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

#Function to generate a student ID for a new student
def GenerateID(studentID, fname, lname):
        if studentID == None:
            studentID = fname[0:3] + lname[0:3] + year
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

    def GetFirstName(self):
        return self.fname

    def GetLastName(self):
        return self.lname
    
    def GetEmail(self):
        return self.email

    def GetCampus(self):
        return self.campus
    
    def GetStudentID(self):
        return self.studentID

#Turn back to Students
students = [Student(**kwargs) for kwargs in myTableData.to_dict(orient='records')]



