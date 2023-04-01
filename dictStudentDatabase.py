
file = open('sampleStudentDatabase.txt', "r")
content = file.readlines()

Students = []

for line in content:
    fname, lname, email, campus = line.strip().split(',')
    studentID = fname[0:3] + lname[0:3]
    Students.append({studentID:{'fname': fname, 'lname': lname, 'email': email, 'campus': campus}})

print(Students)

file.close()
