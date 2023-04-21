from LinearSearch import LinearSearch
from QuickSort import QuickSort
from Student import Student
from Database import students, UpdateTxt, studentTable, myTableData, ToDataframe

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

#Check if returned Index is Valid
def IndexIsValid(array, index):
    if index == -1:
        return "No Such Record Exists"
    else:
        return array[index]

#Check if Input is Valid
def InputIsValid(field):
    userInput = Prompt.ask("[bold green]" + field)
    if userInput == '':
        print("[bold green]Please enter a Valid " + field)
        InputIsValid(field)
    else:
        return userInput

#Check if Campus is Valid
def CampusIsValid():
    campusOptions = Text("""Please Choose Campus:
Wellington (W)
Auckland(A)
ChristChurch(C)""", justify='left', style='bold green')
    print(campusOptions)
    choiceCampus = Prompt.ask("[bold green]Input Choice:", choices=['W', 'A', 'C'])
    if choiceCampus == 'W':
        choiceCampus = 'Wellington'
        return choiceCampus
    elif choiceCampus == 'A':
        choiceCampus = 'Auckland'
        return choiceCampus
    elif choiceCampus == 'C':
        choiceCampus = 'ChristChurch'
        return choiceCampus
    else:
        print("Campus Choice was Invalid.")
        CampusIsValid()

#Prompt to ask if user wants to Go Again        
def GoAgain(x, y):
    print("[bold magenta]DO YOU WANT TO " + y + " [bold magenta]AGAIN?")
    searchAgain = Prompt.ask("[bold green]Please input Y or N", choices=['Y', 'N'])
    if searchAgain == 'Y':
        x()
    elif searchAgain == 'N':
        MainMenu()
        
#Main Menu Function
def MainMenu():
    options = Text("""ADD NEW STUDENT (A)
DELETE STUDENT (D)
SHOW STUDENTS (S)
SEARCH STUDENT (F)

Type EXIT to quit the application.
        """, justify='center', style='blue')
    menu = Panel(options, title="[bold green]Main Menu")
    print(menu)
    userChoice = Prompt.ask("[bold green]Enter Your Choice[/bold green]", choices=["A", "D", "S", "F", "EXIT"])
    if userChoice == 'A':
        AddStudent()
    elif userChoice == 'D':
        DeleteStudent()
    elif userChoice == 'S':
        ShowStudents()
    elif userChoice == 'F':
        SearchStudents()
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
    GoAgain(AddStudent, "ADD A RECORD")

def DeleteStudent():
    toDelete = Prompt.ask("[bold blue]Enter StudentID to Delete: ")
    index = LinearSearch(students, len(students)-1, Student.GetStudentID)
    if IndexIsValid(students, index) == "No Such Record Exists":
        print("[bold red]Student ID Does Not Exist")
        DeleteStudent()
    else:
        students.pop(index)
        print("""[bold red]RECORD DELETED""")
        GoAgain(DeleteStudent, "DELETE A STUDENT")
    
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
    GoAgain(ShowStudents, 'SORT')

def SearchStudents():
    options = Text("""
SEARCH STUDENT BY ID (I)
SEARCH STUDENT BY FIRST NAME (F)
SEARCH STUDENT BY LAST NAME (L)
        """, justify='center', style='blue')
    menu = Panel(options, title="[bold green]STUDENT SEARCH MENU")
    print(menu)
    userChoice = Prompt.ask("[bold green]Please make a selection:  ", choices=['I', 'F', 'L'])
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
    GoAgain(SearchStudents, 'SEARCH')

Main()


