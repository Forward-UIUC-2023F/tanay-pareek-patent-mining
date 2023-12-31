import json
import sqlite3
import glob, os
os.chdir("/Users/tanay/Desktop/ResearchWork/2023")

sqliteConnection = sqlite3.connect('/Users/tanay/Desktop/ResearchWork/PatentGrantsBibliography05on.db')
cursor = sqliteConnection.cursor()

for file in glob.glob("*.json"):
    print(file)
    with open(file,'r') as json_File :
        load_file = json.load(json_File)
        for i in range(len(load_file)):
            if i == len(load_file) - 1:
                continue
            # PATENT GRANTS TABLE
            b110_doc_number = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["publication-reference"]["document-id"]["doc-number"]
            try:
                b511_main_classification = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["classification-ipc"]["main-classification"]
            except:
                b511_main_classification = "NA"
            try:
                b520_dom_national_classification = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["classification-national"]["main-classification"]
            except:
                b520_dom_national_classification = "NA"
            params_1 = (str(b110_doc_number), str(b511_main_classification), str(b520_dom_national_classification))
            sql_query_1 = '''INSERT OR IGNORE INTO PatentGrants VALUES (?, ?, ?)'''
            cursor.execute(sql_query_1, params_1)
            sqliteConnection.commit()

            # PATENT TECHNICAL INFORMATION TABLE
            # 1. b110_doc_number from above
            b130_kind_of_doc = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["publication-reference"]["document-id"]["kind"]
            b140_date_of_pub = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["publication-reference"]["document-id"]["date"]
            b190_pub_ctry_org = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["publication-reference"]["document-id"]["country"]
            if "#text" in load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["invention-title"]:
                b540_title_of_invention = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["invention-title"]["#text"]
            elif "i" in load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["invention-title"]:
                b540_title_of_invention = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["invention-title"]["i"]
            else:
                b540_title_of_invention = ""
            sdode = "NA"
            sdocl = "NA"
            params_2 = (str(b110_doc_number), str(b130_kind_of_doc), str(b140_date_of_pub), str(b190_pub_ctry_org), str(b540_title_of_invention), str(sdode), str(sdocl))
            sql_query_2 = '''INSERT OR IGNORE INTO PatentTechnicalInformation VALUES (?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(sql_query_2, params_2)
            sqliteConnection.commit()

            # INVENTORS TABLE
            # 4. b110_doc_number from above
            if "us-parties" in load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]:
                inventor_arr = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["us-parties"]["inventors"]["inventor"]
            elif "parties" in load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]:
                inventor_arr = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["parties"]["applicants"]["applicant"]
            if isinstance(inventor_arr, list):
                # If there are multiple applicants, iterate through the list
                for applicant in inventor_arr:
                    #name
                    if "first-name" in applicant["addressbook"]:
                        inventor_fname = applicant["addressbook"]["first-name"]
                    else:
                        inventor_fname = ""
                    if "last-name" in applicant["addressbook"]:
                        inventor_lname = applicant["addressbook"]["last-name"]
                    else:
                        inventor_lname = ""
                    if inventor_fname == None:
                        inventor_fname = ""
                    if inventor_lname == None:
                        inventor_lname = ""
                    inventor_name = inventor_fname + " " + inventor_lname
                    # print(inventor_name)
                    
                    #address
                    flag = True
                    if "address" in applicant["addressbook"]:
                        try:
                            inventor_street = applicant["addressbook"]["address"]["street"]
                        except:
                            flag = False
                        if "city" in applicant["addressbook"]["address"]:
                            inventor_city = applicant["addressbook"]["address"]["city"]
                        else:
                            inventor_city = ""
                        inventor_ctry = applicant["addressbook"]["address"]["country"]
                        if flag:
                            inventor_address = inventor_street + ", " + inventor_city + ", " + inventor_ctry
                        else:
                            inventor_address = inventor_city + ", " + inventor_ctry
                    else:
                        inventor_address = ""
                    params_3 = (str(inventor_name), str(inventor_address), str(b110_doc_number))
                    sql_query_3 = '''INSERT INTO Inventors VALUES (?, ?, ?)'''
                    cursor.execute(sql_query_3, params_3)
                    sqliteConnection.commit()
                    
            else:
                # If there's only one applicant, extract the information
                if "first-name" in inventor_arr["addressbook"]:
                    inventor_fname = inventor_arr["addressbook"]["first-name"]
                else:
                    inventor_fname = ""
                if "last-name" in inventor_arr["addressbook"]:
                    inventor_lname = inventor_arr["addressbook"]["last-name"]
                else:
                    inventor_lname = ""
                inventor_name = inventor_fname + " " + inventor_lname
                # print(inventor_name)
                # address
                flag = True
                if "address" in inventor_arr["addressbook"]:
                    try:
                        inventor_street = inventor_arr["addressbook"]["address"]["street"]
                    except:
                        flag = False
                    if "city" in inventor_arr["addressbook"]["address"]:
                        inventor_city = inventor_arr["addressbook"]["address"]["city"]
                    else:
                        inventor_city = ""
                    inventor_ctry = inventor_arr["addressbook"]["address"]["country"]
                    if flag:
                        inventor_address = inventor_street + ", " + inventor_city + ", " + inventor_ctry
                    else:
                        inventor_address = inventor_city + ", " + inventor_ctry
                else:
                    inventor_address = ""  

                params_3 = (str(inventor_name), str(inventor_address), str(b110_doc_number))
                sql_query_3 = '''INSERT INTO Inventors VALUES (?, ?, ?)'''
                cursor.execute(sql_query_3, params_3)
                sqliteConnection.commit()

            if "us-deceased-inventor" in load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]:
                deceased_inventor_arr = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["us-deceased-inventor"]
                if isinstance(deceased_inventor_arr, list):
                # If there are multiple applicants, iterate through the list
                    for invent in deceased_inventor_arr:
                        #name
                        if "first-name" in invent["addressbook"]:
                            inventor_fname = invent["addressbook"]["first-name"]
                        else:
                            inventor_fname = ""
                        if "last-name" in invent["addressbook"]:
                            inventor_lname = invent["addressbook"]["last-name"]
                        else:
                            inventor_lname = ""
                        inventor_name = "Deceased - " + inventor_fname + " " + inventor_lname
                        # print(inventor_name)
                        
                        #address
                        flag = True
                        try:
                            inventor_street = invent["addressbook"]["address"]["street"]
                        except:
                            flag = False
                        if "city" in invent["addressbook"]["address"]:
                            inventor_city = invent["addressbook"]["address"]["city"]
                        else:
                            inventor_city = ""
                        inventor_ctry = invent["addressbook"]["address"]["country"]
                        if flag:
                            inventor_address = inventor_street + ", " + inventor_city + ", " + inventor_ctry
                        else:
                            inventor_address = inventor_city + ", " + inventor_ctry  

                        params_3 = (str(inventor_name), str(inventor_address), str(b110_doc_number))
                        sql_query_3 = '''INSERT INTO Inventors VALUES (?, ?, ?)'''
                        cursor.execute(sql_query_3, params_3)
                        sqliteConnection.commit()
                else:
                    if "first-name" in deceased_inventor_arr["addressbook"]:
                        inventor_fname = deceased_inventor_arr["addressbook"]["first-name"]
                    else:
                        inventor_fname = ""
                    if "last-name" in deceased_inventor_arr["addressbook"]:
                        inventor_lname = deceased_inventor_arr["addressbook"]["last-name"]
                    else:
                        inventor_lname = ""
                    inventor_name = "Deceased - " + inventor_fname + " " + inventor_lname
                    print(inventor_name)

                    flag = True
                    try:
                        inventor_street = deceased_inventor_arr["addressbook"]["address"]["street"]
                    except:
                        flag = False
                    if "city" in  deceased_inventor_arr["addressbook"]["address"]:
                        inventor_city = deceased_inventor_arr["addressbook"]["address"]["city"]
                    else:
                        inventor_city = ""
                    inventor_ctry = deceased_inventor_arr["addressbook"]["address"]["country"]
                    if flag:
                        inventor_address = inventor_street + ", " + inventor_city + ", " + inventor_ctry
                    else:
                        inventor_address = inventor_city + ", " + inventor_ctry  

                    # print(inventor_name)
                    # print(inventor_address)

                    params_3 = (str(inventor_name), str(inventor_address), str(b110_doc_number))
                    sql_query_3 = '''INSERT INTO Inventors VALUES (?, ?, ?)'''
                    cursor.execute(sql_query_3, params_3)
                    sqliteConnection.commit()


            # ASSIGNEES TABLE
            if "assignees" in load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]:
                assignee_arr = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]
                if isinstance(assignee_arr, list):
                    for assgn in assignee_arr:
                        if "addressbook" in assgn:
                            try:
                                assignee_name = assgn["addressbook"]["orgname"]
                            except:
                                assignee_fname = assgn["addressbook"]["first-name"]
                                assignee_lname = assgn["addressbook"]["last-name"]
                                assignee_name =  assignee_fname + " " + assignee_lname
                            
                            flag = True
                            try:
                                assignee_cty =  assgn["addressbook"]["address"]["city"]
                            except:
                                flag = False
                            assignee_ctry = assgn["addressbook"]["address"]["country"]
                            if flag:
                                assignee_address = assignee_cty + ", " + assignee_ctry
                            else:
                                assignee_address = assignee_ctry

                            b732_ustype = assgn["addressbook"]["role"]

                            params_4 = (str(assignee_name), str(assignee_address), b732_ustype, str(b110_doc_number))
                            sql_query_4 = '''INSERT INTO Assignees VALUES (?, ?, ?, ?)'''
                            cursor.execute(sql_query_4, params_4)
                            sqliteConnection.commit()

                        else:
                            try:
                                assignee_name = assgn["orgname"]
                            except:
                                assignee_fname = assgn["first-name"]
                                assignee_lname = assgn["last-name"]
                                assignee_name =  assignee_fname + " " + assignee_lname

                            try:
                                assignee_cty =  assgn["address"]["city"]
                            except:
                                flag = False
                            try:
                                assignee_ctry = assgn["address"]["country"]
                            except:
                                assignee_ctry = ""
                            
                            if flag:
                                assignee_address = assignee_cty + ", " + assignee_ctry
                            else:
                                assignee_address = assignee_ctry
                            
                            b732_ustype = assgn["role"]
                            
                            params_4 = (str(assignee_name), str(assignee_address), b732_ustype, str(b110_doc_number))
                            sql_query_4 = '''INSERT INTO Assignees VALUES (?, ?, ?, ?)'''
                            cursor.execute(sql_query_4, params_4)
                            sqliteConnection.commit()

                else:
                    if "addressbook" in assignee_arr:
                        try:
                            assignee_name = assignee_arr["addressbook"]["orgname"]
                        except:
                            if "first-name" in assignee_arr:
                                assignee_fname = assignee_arr["addressbook"]["first-name"]
                            else:
                                assignee_fname = ""
                            if "last-name" in assignee_arr["addressbook"]:
                                assignee_lname = assignee_arr["addressbook"]["last-name"]
                            else:
                                assignee_lname = ""
                            assignee_name =  assignee_fname + " " + assignee_lname

                        flag_one = True
                        try:
                            assignee_cty =  load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["addressbook"]["address"]["city"]
                        except:
                            flag_one = False
                        try:
                            assignee_st = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["addressbook"]["address"]["state"]
                        except:
                            assignee_st = ""
                        assignee_ctry = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["addressbook"]["address"]["country"]
                        if flag_one:
                            assignee_address = assignee_cty + ", " + assignee_st + ", " + assignee_ctry
                        else:
                            assignee_address = assignee_st + ", " + assignee_ctry

                        b732_ustype = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["addressbook"]["role"]

                        params_4 = (str(assignee_name), str(assignee_address), b732_ustype, str(b110_doc_number))
                        sql_query_4 = '''INSERT INTO Assignees VALUES (?, ?, ?, ?)'''
                        cursor.execute(sql_query_4, params_4)
                        sqliteConnection.commit()

                    else:
                        try:
                            assignee_name = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["orgname"]
                        except:
                            assignee_fname = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["first-name"]
                            assignee_lname = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["last-name"]
                            assignee_name =  assignee_fname + " " + assignee_lname

                        flag_one = True
                        try:
                            assignee_cty =  load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["address"]["city"]
                        except:
                            flag_one = False
                        try:
                            assignee_st = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["address"]["state"]
                        except:
                            assignee_st = ""
                        try:
                            assignee_ctry = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["address"]["country"]
                        except:
                            assignee_ctry = ""
                        if flag_one:
                            assignee_address = assignee_cty + ", " + assignee_st + ", " + assignee_ctry
                        else:
                            assignee_address = assignee_st + ", " + assignee_ctry

                        b732_ustype = load_file[i]["us-patent-grant"]["us-bibliographic-data-grant"]["assignees"]["assignee"]["role"]

                        params_4 = (str(assignee_name), str(assignee_address), b732_ustype, str(b110_doc_number))
                        sql_query_4 = '''INSERT INTO Assignees VALUES (?, ?, ?, ?)'''
                        cursor.execute(sql_query_4, params_4)
                        sqliteConnection.commit()
        


cursor.close()
if sqliteConnection:
    sqliteConnection.close()