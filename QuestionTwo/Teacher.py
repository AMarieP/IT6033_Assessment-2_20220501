from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

#Teacher Class
class Teacher:
    def __init__(self, name):
        self.name = name,
        self.courses = []
    
    def __repr__(self):
         return '\n[blue]Course Title: ' + self.name + '\n[blue]Course Name: ' + self.name

    def AddACourse(self, course):
        newCourse = course.title
        #Checks for duplicate
        for x in self.courses:
            if x.title == newCourse:
                print("[bold red]Course Already Added")
        #Adds course object
        self.courses.append(course)

teachers = [Teacher('Miss Honey'), Teacher('Ms Trunchbull')]

