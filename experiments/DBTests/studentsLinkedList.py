from datetime import date

def GenerateID(studentID, fname, lname):
        thisYear = date.today().year
        if studentID == None:
            studentID = fname[0:3] + lname[0:3] + str(thisYear)
            return studentID

#Individual Student Record
class Student:
    def __init__(self, fname, lname, email, campus, studentID):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.campus = campus
        self.studentID = GenerateID(studentID, self.fname, self.lname)
        self.next = None



#Students in a Linked List
class StudentsList():
    def __init__(self, students = None):
        self.head = None
        if students != None:
            student = students.pop(0)
            self.head = student
            for x in students:
                student.next = x
                student = student.next

#Currently Prints by FName Only 
    def __repr__(self):
        currentStudent = self.head
        studentList = []
        if currentStudent == None:
            return "There is no Data"
        else:
            while currentStudent:
                studentList.append(str(currentStudent.studentID))
                currentStudent = currentStudent.next
            studentList.append("End of List")
            return " -> ".join(studentList)
    
    def IfHeadIsEmpty():
        return "There is no Data"

    #Currently inserts at the beginning of the list 
    def NewStudent(self):
        print("Enter the Student Details:")
        fname = input("First name: ")
        lname = input("Last Name: ")
        email = input("Email Address: ")
        #NOte to SELF - create validator for inputs and drop down campus
        campus = input("Campus: ")
        newStudent = Student(fname, lname, email, campus, None)
        if self.head == None:
            self.head = newStudent
        else:
            newStudent.next = self.head
            self.head = newStudent

    def RemoveStudent(self):
        removeID = input("Enter Student ID to Delete the Record: ")
        #Search the list for the ID
        if removeID:
            pass
        else:
            print("This student ID is invalid and cannot be deleted.")

    def ShowAllStudentsByID(self):
        #sort algo for students
        currentStudent = self.head
        next = currentStudent.next
        while currentStudent:
            if currentStudent.studentID >= next.studentID:
                currentStudent = next
                next = currentStudent.next
                # print(currentStudent.studentID)
                swapped = False
                if currentStudent.next == None:
                    break
            else:
                print(currentStudent.studentID)
                prev = currentStudent
                print(currentStudent.studentID)
                currentStudent = next
                print(currentStudent.studentID)
                next = prev
                print(currentStudent.studentID)
                swapped = True
                break

    def SearchStudentByID():
        pass

    def SearchStudentByFirstName():
        pass

    def SearchStudentByLastName():
        pass

new1 = Student('Alyssa', 'Pilbrow', 'alyssakvasl', 'Auckl', None)
new2 = Student('Vaughan', 'Pilbrow', 'vaughanKvasl', 'Auckl', None)

list = StudentsList([new1, new2])

print(list)
list.NewStudent()
print(list)
list.ShowAllStudentsByID()
print(list)
