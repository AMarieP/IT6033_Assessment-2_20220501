#Teacher Class
class Teacher:
    def __init__(self, name, courses):
        self.name = name,
        self.courses = []
    
    def __repr__(self):
         return '\n[blue]Course Title: ' + self.name + '\n[blue]Course Name: ' + self.name

    def AddACourse(self, course):
        newCourse = course.title
        #Checks for duplicate
        for x in self.courses:
            if x.title == newCourse:
                return "Course Already Added"
        #Adds course object
        self.courses.append(course)