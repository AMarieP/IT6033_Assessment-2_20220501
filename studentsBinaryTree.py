def GenerateID(studentID, fname, lname):
        if studentID == None:
            studentID = fname[0:3] + lname[0:3]
            return studentID

#Individual Student Record
class Student:
    def __init__(self, fname, lname, email, campus, studentID):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.campus = campus
        self.studentID = GenerateID(studentID, self.fname, self.lname)



#Student in a Binary Tree
class Students():
    def __init__(self) -> None:
        self.students = []
    
    def NewStudent():
        pass

    def RemoveStudent():
        pass

    def ShowAllStudents():
        pass

    def SearchStudentByID():
        pass

    def SearchStudentByFirstName():
        pass

    def SearchStudentByLastName():
        pass

new = Student('Alyssa', 'Pilbrow', 'alyssakvasl', 'Auckl', None)
print(new.studentID)

list = Students(new)
