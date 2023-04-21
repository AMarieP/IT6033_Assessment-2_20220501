#Courses module

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []
    
    def __repr__(self):
         return 'Course Title: ' + str(self.title)

    def GetTitle(self):
        return self.title
    
    def GetEnrolled(self):
        for x in self.students:
            print(x.GetFirstname + x.GetLastName)


    def EnrollStudent(self, student):
        self.students.append(student)

courses = [Course('MATH'), Course('ENGLISH'), Course('SCIENCE')]
