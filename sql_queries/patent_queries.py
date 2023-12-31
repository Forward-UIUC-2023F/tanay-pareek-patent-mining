import json
import sqlite3

# NOTE: Change all database and file paths as per user's computer

sqliteConnection = sqlite3.connect('/Users/tanay/Desktop/ResearchWork/PatentGrantsBibliography05on.db')
cursor = sqliteConnection.cursor()

# returns all the inventors from San Francisco
sql_query_1 = '''SELECT B721_Inventor_Name FROM Inventors WHERE B721_Inventor_Address LIKE "%San Francisco%" '''
cursor.execute(sql_query_1)
output = cursor.fetchall()
print(output)
print(len(output))

# returns all the assignees from Champaign
sql_query_2 = '''SELECT DISTINCT B731_Name FROM Assignees WHERE B731_Address LIKE "%Champaign%" '''
cursor.execute(sql_query_2)
output_2 = cursor.fetchall()
print(output_2)
print(len(output_2))

# returns top 3 assignees from Champaign
sql_query_3 = '''SELECT B731_Name, COUNT(*) AS assignee_count 
                    FROM Assignees 
                    WHERE B731_Address LIKE "%Champaign%" 
                    GROUP BY B731_Name 
                    ORDER BY assignee_count DESC 
                    LIMIT 3'''
cursor.execute(sql_query_3)
output_3 = cursor.fetchall()
print(output_3)

# returns top 4 assignees throughout the world ignoring empty assignees as 1st one
sql_query_4 = '''SELECT B731_Name, B731_Address, COUNT(*) AS assignee_count 
                    FROM Assignees 
                    GROUP BY B731_Name 
                    ORDER BY assignee_count DESC 
                    LIMIT 4'''
cursor.execute(sql_query_4)
output_4 = cursor.fetchall()
print(output_4)

# returns top 4 places with highest inventors ignoring empty addresses as 1st one
sql_query_5 = '''SELECT B721_Inventor_Address, COUNT(*) AS inventor_count 
                    FROM Inventors 
                    GROUP BY B721_Inventor_Address 
                    ORDER BY inventor_count DESC 
                    LIMIT 4'''
cursor.execute(sql_query_5)
output_5 = cursor.fetchall()
print(output_5[1:3])

cursor.close()
if sqliteConnection:
    sqliteConnection.close()