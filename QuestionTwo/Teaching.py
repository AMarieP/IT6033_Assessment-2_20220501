#Teaching Module to Add a Student to Course
from LinearSearch import LinearSearch
from Student import Student
from Database import students
from Teacher import teachers
from Course import courses, Course
from Validator import IndexIsValid, InputIsValid, CampusIsValid, GoAgain


#Rich is used to Style things in Terminal
from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
console = Console()

Courses = [] 


def Teaching():
        thisStudent = WhatStudent()
        thisCourse = WhatCourse()
        thisStudent.AddToCourse(thisCourse)
        thisCourse.EnrollStudent(thisStudent)
        print('[bold green]Students Courses:')
        print((thisStudent.PrintCourses()))

def AddCourseToTeacher():
        teacher = WhichTeacher()
        course = WhatCourse()
        teacher.AddACourse(course)
        print('*****')


def WhatStudent():
        student = Prompt.ask("[bold green]Please input the ID of the Student to Add")
        thisStudent = LinearSearch(students, len(students)-1, Student.GetStudentID, student)
        print("[bold magenta]Your Record is: [/bold magenta]" + str(IndexIsValid(students, thisStudent)))
        if str(IndexIsValid(students, thisStudent)) == 'No Such Record Exists':
                WhatStudent()
        return students[thisStudent]

def WhatCourse():
        whatCourse = Prompt.ask("[bold green]Please input the name of the Course", choices=["MATH", "ENGLISH", "SCIENCE"])
        thisCourse = courses[LinearSearch(courses, len(courses)-1, Course.GetTitle, whatCourse)]
        return thisCourse

def WhichTeacher():
    teacher = Prompt.ask("[bold green]Which Teacher[/bold green]", choices=["MISS HONEY", "MS TRUNCHBULL"])
    if teacher == "MISS HONEY":
        return teachers[0]
    if teacher == "MS TRUNCHBULL":
        return teachers[1]