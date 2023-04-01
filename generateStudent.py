class Student:
    def __init__(self, fname, lname, email, campus, studentID) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email
        self.campus = campus
        self.studentID = studentID
    
    # def __str__(self) -> str:
    #     pass
        


file = open('sampleStudentDatabase.txt', "r+")
content = file.readlines()

Students = []

for line in content:
    fname, lname, email, campus = line.strip().split(',')
    studentID = fname[0:3] + lname[0:3]
    Students.append(Student(fname, lname, email, campus, studentID))

print(Students[1].fname)

file.close()

#But how do I read again once the ID is generated