#Courses module

class Course:
    def __init__(self, title):
        self.title = title,
        self.names = []
    
    def __repr__(self):
         return '\n[blue]Course Title: ' + self.title + '\n[blue]Course Name: ' + self.title

    def EnrollStudent(self, student):
        self.names.append(student)