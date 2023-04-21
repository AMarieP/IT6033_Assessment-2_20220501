import pandas as pd
from Student import Student
import datetime

#Get the Year
today = datetime.date.today()
year = str(today.year)

#Reads the txt file and turns to dataframe
studentTable = "databasefiles/smallDB.txt"

results = []
with open(studentTable) as f:
    line = f.readline()
    while line:
        results.append(line.strip().split(","))
        line = f.readline()
f.close()
myTableData = pd.DataFrame(results, columns = ["fname", "lname", 'email', 'campus', 'studentID'])
myTableData.studentID = myTableData.fname.str.slice(start=0, stop=3) + myTableData.lname.str.slice(start=0, stop=3) + year

#Turn back to Students
students = [Student(**kwargs) for kwargs in myTableData.to_dict(orient='records')]

#Convert Object to Dataframe
def ToDataframe(table):
    newDataframe = pd.DataFrame([vars(s) for s in table])
    return newDataframe

#Updates the TXT file
def UpdateTxt(df, file):
    with open(file, 'w') as f:
        rows = df.shape[0]
        dfAsString = []
        while rows > 0:
            rows = rows - 1
            seriesAsAString = df.iloc[rows].fillna('').str.strip().str.cat(sep=',')
            dfAsString.append(seriesAsAString + '\n')
        f.writelines(dfAsString)

