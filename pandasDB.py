import pandas as pd
import datetime

#Get the Year
today = datetime.date.today()
year = str(today.year)

studentTable = "smallDB.txt"
results = []
with open(studentTable) as f:
    line = f.readline()
    while line:
        results.append(line.strip().split(","))
        line = f.readline()
f.close()
myTableData = pd.DataFrame(results, columns = ["fname", "lname", 'email', 'campus'])

myTableData["ID"] = myTableData['fname'].str.slice(start=0, stop=3) + myTableData['lname'].str.slice(start=0, stop=3) + year

# Display
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(myTableData)

print(myTableData.head())