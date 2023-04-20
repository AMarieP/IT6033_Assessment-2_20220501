from BinarySearch import BinarySearch
from QuickSort import QuickSort
from Student import students, Student



def Main():
    print(
f"""**** Welcome TO WHITECLIFFE College of Information Technology ***

******************** STUDENT PORTAL *************************"""
        )
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
    userInput = input(f"{field}: ")
    if userInput == '':
        print(f"Please enter a Valid {field}")
        InputIsValid(field)
    else:
        return userInput

#Check if Campus is Valid
def CampusIsValid():
    choiceCampus = input("""Please Choose Campus:
    Wellington (W)
    Auckland(A)
    ChristChurch(C)""")
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
    print(f"""DO YOU WANT TO {y} AGAIN? (Y/N)""")
    searchAgain = input("Please input Y or N: ")
    if searchAgain == 'Y':
        x()
    elif searchAgain == 'N':
        MainMenu()
    else: 
        print("Please use a valid input")
        GoAgain(x, y)
        

def MainMenu():
    userChoice = input(
        f"""MAIN MENU
        ADD NEW STUDENT (A)
        DELETE STUDENT (D)
        SHOW STUDENTS (S)
        SEARCH STUDENT (F)

        Type EXIT to quit the application: ____________
        """
    )
    if userChoice == 'A':
        AddStudent()
    elif userChoice == 'D':
        DeleteStudent()
    elif userChoice == 'S':
        ShowStudents()
    elif userChoice == 'F':
        SearchStudents()
    elif userChoice == 'EXIT':
        return False
    else:
        "Please Input a Valid Selection"
        MainMenu()

def AddStudent():
    print("Enter Student Details: ")
    newfname = InputIsValid("First Name")
    newlname = InputIsValid("Last Name")
    newemail = InputIsValid("Email Address")
    newCampus = CampusIsValid()
    students.append(Student(newfname, newlname, newemail, newCampus, None))
    print(f"""Your Record has been added""")
    GoAgain(AddStudent, "ADD A RECORD")


def DeleteStudent():
    toDelete = input("Enter StudentID to Delete: ")
    index = BinarySearch(students, 0, len(students)-1, toDelete, Student.GetStudentID)
    if IndexIsValid(students, index) == "No Such Record Exists":
        print("Student ID Does Not Exist")
        DeleteStudent()
    else:
        students.pop(index)
        print("""RECORD DELETED""")
        GoAgain(DeleteStudent, "DELETE A STUDENT")
    

def ShowStudents():
    print(
        f"""*******************

        STUDENTS SHOW MENU

        *******************
        SHOW ALL STUDENTS BY ID (I)
        SHOW ALL STUDENTS BY FIRST NAME (F)
        SHOW ALL STUDENTS BY LAST NAME (L)
        SHOW ALL STUDENTS BY CAMPUS (C)

        Shown in Ascending Order
            
            """
    )
    userChoice = input("Please make a selection:  ")
    if userChoice == 'I':
        QuickSort(students, Student.GetStudentID, 0, len(students)-1)
    elif userChoice == 'F':
        QuickSort(students, Student.GetFirstName, 0, len(students)-1)
    elif userChoice == 'L':
        QuickSort(students, Student.GetLastName, 0, len(students)-1)
    elif userChoice == 'C':
        QuickSort(students, Student.GetCampus, 0, len(students)-1)
    else:
        print("Please Make a Valid Input")
        ShowStudents()
    print(f"Here are your sorted records: {students}")
    GoAgain(ShowStudents, 'SORT')

def SearchStudents():
    print(
        f"""*******************

        STUDENT SEARCH MENU

        *******************
        SEARCH STUDENT BY ID (I)
        SEARCH STUDENT BY FIRST NAME (F)
        SEARCH STUDENT BY LAST NAME (L)
            
            """
    )
    userChoice = input("Please make a selection:  ")
    index = 0
    if userChoice == 'I':
        searchTarget = input("Please input the ID to Search:  ")
        index = BinarySearch(students, 0, len(students)-1, searchTarget, Student.GetStudentID)
    elif userChoice == 'F':
        searchTarget = input("Please input the First Name to Search:  ")
        index = BinarySearch(students, 0, len(students)-1, searchTarget, Student.GetFirstName)
    elif userChoice == 'L':
        searchTarget = input("Please input the First Name to Search:  ")
        BinarySearch(students, 0, len(students)-1, searchTarget, Student.GetLastName)
    else:
        print("Please Make a Valid Input")
        SearchStudents()
    print(f"Here is your record: {IndexIsValid(students, index)}")
    GoAgain(SearchStudents, 'SEARCH')
    
Main()


