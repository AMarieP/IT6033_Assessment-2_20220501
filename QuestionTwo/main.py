from LinearSearch import LinearSearch
from QuickSort import QuickSort
from Student import Student
from Database import students, UpdateTxt, studentTable, myTableData, ToDataframe
from Teaching import Teaching, AddCourseToTeacher
from Teacher import Teacher, teachers
from Course import Course
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


#Program uses a Binary Search and a Quick Sort to access records

def Main():
    panel = Panel(Text("Welcome TO WHITECLIFFE College of Information Technology's Student Portal", justify="center", style="bold magenta"))
    print(panel)
    running = True
    if running == True:
        running = MainMenu()

        
#Main Menu Function
def MainMenu():
    options = Text("""ADD NEW STUDENT (A)
DELETE STUDENT (D)
SHOW STUDENTS (S)
SEARCH STUDENT (F)
ADD STUDENT TO COURSE (C)
ADD A COURSE TO TEACHER (T)

Type EXIT to quit the application.
        """, justify='center', style='blue')
    menu = Panel(options, title="[bold green]Main Menu")
    print(menu)
    userChoice = Prompt.ask("[bold green]Enter Your Choice[/bold green]", choices=["A", "D", "S", "F", "EXIT", 'C', 'T'])
    if userChoice == 'A':
        AddStudent()
    elif userChoice == 'D':
        DeleteStudent()
    elif userChoice == 'S':
        ShowStudents()
    elif userChoice == 'F':
        SearchStudents()
    elif userChoice == 'C':
        Teaching()
        GoAgain(Teaching, 'ADD A STUDENT TO A COURSE', MainMenu)
    elif userChoice == 'T':
        AddCourseToTeacher()
        GoAgain(AddCourseToTeacher, 'ADD A COURSE TO A TEACHER', MainMenu)
    elif userChoice == 'EXIT':
        updatedDataframe = ToDataframe(students)
        UpdateTxt(updatedDataframe, studentTable)
        return False

#Show/ Manipulate Record Functions

#Makes a Pretty Table
def MakeTable(array):
    studentTable = Table(title="Whitecliffe Student Database" )
    studentTable.add_column('Student ID', style="blue", header_style='bold blue')
    studentTable.add_column('First Name', style="green")
    studentTable.add_column('Last Name', style="green")
    studentTable.add_column('Email', style="yellow")
    studentTable.add_column('Campus', justify="right", style="magenta", header_style='bold magenta')

    for x in array:
        studentTable.add_row(x.studentID, x.fname, x.lname, x.email, x.campus)
    console.print(studentTable)

def AddStudent():
    print("[bold blue]Enter Student Details: ")
    newfname = InputIsValid("First Name")
    newlname = InputIsValid("Last Name")
    newemail = InputIsValid("Email Address")
    newCampus = CampusIsValid()
    students.append(Student(newfname, newlname, newemail, newCampus, None))
    print("[bold green]Your Record has been added")
    GoAgain(AddStudent, "ADD A RECORD", MainMenu)

def DeleteStudent():
    toDelete = Prompt.ask("[bold blue]Enter StudentID to Delete: ")
    index = LinearSearch(students, len(students)-1, Student.GetStudentID)
    if IndexIsValid(students, index) == "No Such Record Exists":
        print("[bold red]Student ID Does Not Exist")
        DeleteStudent()
    else:
        students.pop(index)
        print("""[bold red]RECORD DELETED""")
        GoAgain(DeleteStudent, "DELETE A STUDENT", MainMenu)
    
def ShowStudents():
    options = Text("""
SHOW ALL STUDENTS BY ID (I)
SHOW ALL STUDENTS BY FIRST NAME (F)
SHOW ALL STUDENTS BY LAST NAME (L)
SHOW ALL STUDENTS BY CAMPUS (C)
        """, justify='center', style='blue')
    menu = Panel(options, title="[bold green]STUDENTS SHOW MENU", subtitle='[i magenta]Shown in Ascending Order')
    print(menu)
    userChoice = Prompt.ask("[bold green]Please make a selection ", choices=['I', 'F', 'L', 'C'])
    if userChoice == 'I':
        QuickSort(students, Student.GetStudentID, 0, len(students)-1)
    elif userChoice == 'F':
        QuickSort(students, Student.GetFirstName, 0, len(students)-1)
    elif userChoice == 'L':
        QuickSort(students, Student.GetLastName, 0, len(students)-1)
    elif userChoice == 'C':
        QuickSort(students, Student.GetCampus, 0, len(students)-1)
    print("[bold green]Here are your sorted records:")
    MakeTable(students)
    GoAgain(ShowStudents, 'SORT', MainMenu)

def SearchStudents():
    options = Text("""
SEARCH STUDENT BY ID (I)
SEARCH STUDENT BY FIRST NAME (F)
SEARCH STUDENT BY LAST NAME (L)
        """, justify='center', style='blue')
    menu = Panel(options, title="[bold green]STUDENT SEARCH MENU")
    print(menu)
    userChoice = Prompt.ask("[bold green]Please make a selection", choices=['I', 'F', 'L'])
    index = 0
    if userChoice == 'I':
        searchTarget = Prompt.ask("[bold green]Please input the ID to Search")
        index = LinearSearch(students, len(students), Student.GetStudentID, searchTarget)
    elif userChoice == 'F':
        searchTarget = Prompt.ask("[bold green]Please input the First Name to Search")
        index = LinearSearch(students, len(students), Student.GetFirstName, searchTarget)
    elif userChoice == 'L':
        searchTarget = Prompt.ask("[bold green]Please input the Last Name to Search")
        index = LinearSearch(students, len(students), Student.GetLastName, searchTarget)
    print("[bold magenta]Your Record is: [/bold magenta]" + str(IndexIsValid(students, index)))
    GoAgain(SearchStudents, 'SEARCH', MainMenu)

Main()


