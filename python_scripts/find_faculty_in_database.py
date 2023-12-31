import json
import sqlite3

# NOTE: Change all file paths and database paths as per local user's computer

sqliteConnection = sqlite3.connect('/Users/tanay/Desktop/ResearchWork/PatentGrantsBibliography05on.db')
cursor = sqliteConnection.cursor()

file_newone = "/Users/tanay/Desktop/ResearchWork/UMich_faculty.txt"
file_newtwo = "/Users/tanay/Desktop/ResearchWork/UIUC_faculty.txt"
file_newthree = "/Users/tanay/Desktop/ResearchWork/UCB_faculty.txt"

illinois_Assignees = set()
address = "Illinois"
sql_query_2 = '''SELECT B110_Patent_Document_Number FROM Assignees WHERE B731_Name LIKE ? '''
cursor.execute(sql_query_2, ('%' + address + '%',))
output_2 = cursor.fetchall()

illinois_Assignees = []

for x in output_2:
    illinois_Assignees.append(x[0])

illinois_Assignees = set(illinois_Assignees)

final_res = []

with open(file_newtwo, "r") as input_file:
    while True:
        line = input_file.readline()
        if not line:
            break
        line = line.strip()
        sql_query_1 = '''SELECT B721_Inventor_Name, B110_Patent_Document_Number FROM Inventors WHERE B721_Inventor_Name LIKE ? '''
        cursor.execute(sql_query_1, (str(line),))
        output = cursor.fetchall()

        for inventor, doc_number in output:
            if doc_number in illinois_Assignees:
                final_res.append((inventor, doc_number))
            else:
                continue

with open("/Users/tanay/Desktop/ResearchWork/illinois_inventors.txt", "w") as file:
    for line in final_res:
        file.write(line[0] + ": " + line[1] + " " + "\n")            

michigan_Assignees = set()


address = "Michigan"
sql_query_2 = '''SELECT B110_Patent_Document_Number FROM Assignees WHERE B731_Name LIKE ? '''
cursor.execute(sql_query_2, ('%' + address + '%',))
output_2 = cursor.fetchall()

michigan_Assignees = []

for x in output_2:
    michigan_Assignees.append(x[0])

michigan_Assignees = set(michigan_Assignees)

final_res = []

with open(file_newone, "r") as input_file:
    while True:
        line = input_file.readline()
        if not line:
            break
        line = line.strip()
        sql_query_1 = '''SELECT B721_Inventor_Name, B110_Patent_Document_Number FROM Inventors WHERE B721_Inventor_Name LIKE ? '''
        cursor.execute(sql_query_1, (str(line),))
        output = cursor.fetchall()

        for inventor, doc_number in output:
            if doc_number in michigan_Assignees:
                final_res.append((inventor, doc_number))
            else:
                continue

with open("/Users/tanay/Desktop/ResearchWork/michigan_inventors.txt", "w") as file:
    for line in final_res:
        file.write(line[0] + ": " + line[1] + " " + "\n")

berkeley_Assignees = set()


address = "Berkeley"
sql_query_2 = '''SELECT B110_Patent_Document_Number FROM Assignees WHERE B731_Name LIKE ? '''
cursor.execute(sql_query_2, ('%' + address + '%',))
output_2 = cursor.fetchall()

berkeley_Assignees = []

for x in output_2:
    berkeley_Assignees.append(x[0])

berkeley_Assignees = set(berkeley_Assignees)

final_res = []

with open(file_newthree, "r") as input_file:
    while True:
        line = input_file.readline()
        if not line:
            break
        line = line.strip()
        sql_query_1 = '''SELECT B721_Inventor_Name, B110_Patent_Document_Number FROM Inventors WHERE B721_Inventor_Name LIKE ? '''
        cursor.execute(sql_query_1, (str(line),))
        output = cursor.fetchall()

        for inventor, doc_number in output:
            if doc_number in berkeley_Assignees:
                final_res.append((inventor, doc_number))
            else:
                continue

with open("/Users/tanay/Desktop/ResearchWork/berkeley_inventors.txt", "w") as file:
    for line in final_res:
        file.write(line[0] + ": " + line[1] + " " + "\n")               

cursor.close()
if sqliteConnection:
    sqliteConnection.close()