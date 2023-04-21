from rich import print
import datetime



#Get the Year
year = str(datetime.date.today().year)
# year = str(today.year)

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
         return '\n[blue]Student ID: ' + self.studentID + '\nFirst Name: ' + self.fname + '\nLast Name: ' + self.lname + '\nEmail: ' + self.email + '\nCampus: ' + self.campus

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