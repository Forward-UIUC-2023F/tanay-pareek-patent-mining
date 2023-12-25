import json
import sqlite3

# try:
#     sqliteConnection = sqlite3.connect('/Users/tanay/Desktop/UniversityPatentingData.db')
#     cursor = sqliteConnection.cursor()
#     print("Database created and Successfully Connected to SQLite")
#     sqlite_select_Query = "select sqlite_version();"
#     cursor.execute(sqlite_select_Query)
#     record = cursor.fetchall()
#     print("SQLite Database Version is: ", record)
#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")

inventor_first_names = []
inventor_last_names = []
inventor_cities = []
inventor_states = []
assignee_names = []
assignee_cities = []
assignee_countries = []
assignee_type_code = []
claims_sdocl = []
inventor_doc_number = []
with open('/Users/tanay/Downloads/xmltojson.json','r') as json_File :
    sample_load_file = json.load(json_File)
    test = sample_load_file['PATDOC']
    # try:
    #     claims_sdocl.append [dic5['SDOCL']['CL']['CLM']['PARA']['PTEXT']['PDAT'] for dic5 in test]
    all_doc_numbers = [dic['SDOBI']['B100']['B110']['DNUM']['PDAT'] for dic in test]
    main_ipc_classifications = [dic1['SDOBI']['B500']['B510']['B511']['PDAT'] for dic1 in test]
    main_domestic_or_national_classifications = [dic2['SDOBI']['B500']['B520']['B521']['PDAT'] for dic2 in test]
    titles_of_inventions = [dic3['SDOBI']['B500']['B540']['STEXT']['PDAT'] for dic3 in test]
    kinds_of_documents = [dic3['SDOBI']['B100']['B130']['PDAT'] for dic3 in test]
    date_of_publication = [dic3['SDOBI']['B100']['B140']['DATE']['PDAT'] for dic3 in test]
    publishing_country_or_organization = [dic3['SDOBI']['B100']['B190']['PDAT'] for dic3 in test]
    inventors = [dic3['SDOBI']['B700']['B720']['B721'] for dic3 in test]
    for item in inventors:
        if len(item) > 1:
            for x in item:
                inventor_first_names.append(x['PARTY-US']['NAM']['FNM']['PDAT'])
                inventor_last_names.append(x['PARTY-US']['NAM']['SNM']['STEXT']['PDAT'])
                inventor_cities.append(x['PARTY-US']['ADR']['CITY']['PDAT'])
                try:
                    inventor_states.append(x['PARTY-US']['ADR']['STATE']['PDAT'])
                except:
                    inventor_states.append(" ")
        else:
            try:
                inventor_first_names.append(item['PARTY-US']['NAM']['FNM']['PDAT'])
            except:
                inventor_first_names.append(" ")
            
            try:
                inventor_last_names.append(item['PARTY-US']['NAM']['SNM']['STEXT']['PDAT'])
            except:
                inventor_last_names.append(" ")

            try:
                inventor_cities.append(item['PARTY-US']['ADR']['CITY']['PDAT'])
            except:
                inventor_cities.append(" ")

            try:
                inventor_states.append(item['PARTY-US']['ADR']['STATE']['PDAT'])
            except:
                inventor_states.append(" ")
    
    inventor_full_names = [[i + " " + j for i, j in zip(inventor_first_names, inventor_last_names)]]
    inventor_addresses = [[i + ", " + j for i, j in zip(inventor_cities, inventor_states)]]

    a = [dic3['SDOBI']['B700'] for dic3 in test]
    for item in a:
        try:
            assignee_names.append(item['B730']['B731']['PARTY-US']['NAM']['ONM']['STEXT']['PDAT'])
        except:
            assignee_names.append(" ")

        try:
            assignee_cities.append(item['B730']['B731']['PARTY-US']['ADR']['CITY']['PDAT'])
        except:
            assignee_cities.append(" ")

        try:
            assignee_countries.append(item['B730']['B731']['PARTY-US']['ADR']['CTRY']['PDAT'])
        except:
            assignee_countries.append(" ")
        
        try:
            assignee_type_code.append(item['B730']['B732US']['PDAT'])
        except:
            assignee_type_code.append(" ")
    
    assignee_addresses = [[i + ", " + j for i, j in zip(assignee_cities, assignee_countries)]]

# PATENT GRANTS TABLE

# sqliteConnection = sqlite3.connect('/Users/tanay/Desktop/UniversityPatentingData.db')
# cursor = sqliteConnection.cursor()
# lenn = len(all_doc_numbers)
# print(lenn)
# for i in range(lenn):
#     params = (str(all_doc_numbers[i]), str(main_ipc_classifications[i]), str(main_domestic_or_national_classifications[i]))
#     sql_query = '''INSERT INTO PatentGrants(B110_Patent_Document_Number, B511_Main_IPC_Classification, B520_Main_Domestic_National_Classification) VALUES (?, ?, ?)'''
#     cursor.execute(sql_query, params)
#     sqliteConnection.commit()

# cursor.close()
# if sqliteConnection:
#     sqliteConnection.close()

# param = (str(all_doc_numbers), )
# sql_query = '''INSERT INTO PatentGrants(B110_Patent_Document_Number) VALUES (?)'''
# print(cursor.fetchall())


# INVENTORS TABLE

# sqliteConnection = sqlite3.connect('/Users/tanay/Desktop/UniversityPatentingData.db')
# cursor = sqliteConnection.cursor()
# lenn = len(inventor_full_names[0])
# for i in range(lenn):
#     params = (str(inventor_full_names[0][i]), )
#     sql_query = '''INSERT INTO Inventors(B721_Inventor_Name) VALUES (?)'''
#     cursor.execute(sql_query, params)
#     sqliteConnection.commit()

# cursor.close()
# if sqliteConnection:
#     sqliteConnection.close()

# ASSIGNEES TABLE

# sqliteConnection = sqlite3.connect('/Users/tanay/Desktop/UniversityPatentingData.db')
# cursor = sqliteConnection.cursor()
# lenn = len(assignee_names)
# for i in range(lenn):
#     params = (str(assignee_names[i]), str(assignee_addresses[0][i]), assignee_type_code[i])
#     sql_query = '''INSERT INTO Assignees(B731_Name, B731_Address, B732US_Type) VALUES (?, ?, ?)'''
#     cursor.execute(sql_query, params)
#     sqliteConnection.commit()

# cursor.close()
# if sqliteConnection:
#     sqliteConnection.close()

# PATENT TECHNICAL INFORMATION TABLE

# sqliteConnection = sqlite3.connect('/Users/tanay/Desktop/UniversityPatentingData.db')
# cursor = sqliteConnection.cursor()
# lenn = len(assignee_names)
# for i in range(lenn):
#     params = (str(titles_of_inventions[i]), str(kinds_of_documents[i]), str(date_of_publication[i]), str(publishing_country_or_organization[i]))
#     sql_query = '''INSERT INTO PatentTechnicalInformation(B540_Title_of_Invention, B130_Kind_of_Document, B140_Date_of_Publication, B190_Publishing_Country_or_Org) VALUES (?, ?, ?, ?)'''
#     cursor.execute(sql_query, params)
#     sqliteConnection.commit()

# cursor.close()
# if sqliteConnection:
#     sqliteConnection.close()