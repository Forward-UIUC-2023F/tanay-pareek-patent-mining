import json
import sqlite3

# Change database name to your database name
sqliteConnection = sqlite3.connect('/Users/tanay/Desktop/ResearchWork/PatentGrantsBibliography2005on.db')
cursor = sqliteConnection.cursor()

# Change files to your file name as per your directory
with open('/Users/tanay/Desktop/ResearchWork/2004/ipgb20040101.json','r') as json_File :
    load_file = json.load(json_File)
    # count = 0
    for i in range(len(load_file)):
        if i == len(load_file) - 1:
            continue
        try:
            sample_load_file = load_file[i]['PATDOC']
        except:
            continue
        # # PATENT GRANTS TABLE
        b110_doc_number = sample_load_file['SDOBI']['B100']['B110']['DNUM']['PDAT']
        b511_main_classification = sample_load_file['SDOBI']['B500']['B510']['B511']['PDAT']
        b520_dom_national_classification = sample_load_file['SDOBI']['B500']['B520']['B521']['PDAT']
        params_1 = (str(b110_doc_number), str(b511_main_classification), str(b520_dom_national_classification))
        sql_query_1 = '''INSERT OR IGNORE INTO PatentGrants VALUES (?, ?, ?)'''
        cursor.execute(sql_query_1, params_1)
        sqliteConnection.commit()

        # PATENT TECHNICAL INFORMATION TABLE
        # 1. b110_doc_number from above
        b130_kind_of_doc = sample_load_file['SDOBI']['B100']['B130']['PDAT']
        b140_date_of_pub = sample_load_file['SDOBI']['B100']['B140']['DATE']['PDAT'] 
        b190_pub_ctry_org = sample_load_file['SDOBI']['B100']['B190']['PDAT']
        b540_title_of_invention = sample_load_file['SDOBI']['B500']['B540']['STEXT']['PDAT']
        # check if SDODE exists
        if "SDODE" in sample_load_file:
            print(i)
            if i == 1655:
                sdode = sample_load_file['SDODE']['GOVINT']['BTEXT']['PARA'][0]['PTEXT']['PDAT']
            else:
                if sample_load_file['SDODE'] != None and "GOVINT" in sample_load_file['SDODE']:
                    sdode = sample_load_file['SDODE']['GOVINT']['BTEXT']['PARA']['PTEXT']['PDAT']
                else:
                    sdode = ""
        # check if SDOCL exists
        if "SDOCL" in sample_load_file:
            sdocl = sample_load_file['SDOCL']['CL']['CLM']['PARA']['PTEXT']['PDAT']
        else:
            sdocl = ""
        params_2 = (str(b110_doc_number), str(b130_kind_of_doc), str(b140_date_of_pub), str(b190_pub_ctry_org), str(b540_title_of_invention), str(sdode), str(sdocl))
        sql_query_2 = '''INSERT OR IGNORE INTO PatentTechnicalInformation VALUES (?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(sql_query_2, params_2)
        sqliteConnection.commit()
        
        # INVENTORS TABLE
        # 4. b110_doc_number from above
        inventor_arr = sample_load_file['SDOBI']['B700']['B720']['B721']
        if len(inventor_arr) != 0:
            if len(inventor_arr) == 1:
                try:
                    inventor_first_name = inventor_arr['PARTY-US']['NAM']['FNM']['PDAT']
                except:
                    inventor_first_name = " "
                try:
                    inventor_last_name = inventor_arr['PARTY-US']['NAM']['SNM']['STEXT']['PDAT']
                except:
                    inventor_last_name = " "
                inventor_full_name = inventor_first_name + " " + inventor_last_name
                try:
                    inventor_addr_str = inventor_arr['PARTY-US']['ADR']['STR']['PDAT']
                except:
                    inventor_addr_str = ""
                try:
                    inventor_addr_city = inventor_arr['PARTY-US']['ADR']['CITY']['PDAT']
                except:
                    inventor_addr_city = ""
                try:
                    inventor_addr_ctry = inventor_arr['PARTY-US']['ADR']['CTRY']['PDAT']
                except:
                    inventor_addr_ctry = ""
                # if i == 701:
                #     inventor_addr_str = inventor_addr_str['#text']
                #     print(inventor_addr_str)
                inventor_address = inventor_addr_str + ", " + inventor_addr_city + ", " + inventor_addr_ctry
            else:
                # if (i == 1102):
                #     inventor_first_name = inventor_arr['PARTY-US']['NAM']['FNM']['PDAT']
                #     inventor_last_name = inventor_arr['PARTY-US']['NAM']['SNM']['STEXT']['PDAT']
                #     inventor_full_name = inventor_first_name + " " + inventor_last_name
                #     try:
                #         inventor_addr_str = inventor_arr['PARTY-US']['ADR']['STR']['PDAT']
                #     except:
                #         inventor_addr_str = ""
                #     inventor_addr_city = inventor_arr['PARTY-US']['ADR']['CITY']['PDAT']
                #     try:
                #         inventor_addr_ctry = inventor_arr['PARTY-US']['ADR']['CTRY']['PDAT']
                #     except:
                #         inventor_addr_ctry = ""
                #     inventor_address = inventor_addr_str + ", " + inventor_addr_city + ", " + inventor_addr_ctry
                # else:
                for j in range(len(inventor_arr)):
                    try:
                        inventor_first_name = inventor_arr[j]['PARTY-US']['NAM']['FNM']['PDAT']
                    except:
                        inventor_first_name = " "
                    try:
                        inventor_last_name = inventor_arr[j]['PARTY-US']['NAM']['SNM']['STEXT']['PDAT']
                    except:
                        inventor_last_name = " "
                    if type(inventor_first_name) is dict:
                        inventor_first_name = " "
                    inventor_full_name = inventor_first_name + " " + inventor_last_name
                    try:
                        inventor_addr_str = inventor_arr[j]['PARTY-US']['ADR']['STR']['PDAT']
                    except:
                        inventor_addr_str = ""
                    try:
                        inventor_addr_city = inventor_arr['PARTY-US']['ADR']['CITY']['PDAT']
                    except:
                        inventor_addr_city = ""
                    try:
                        inventor_addr_ctry = inventor_arr[j]['PARTY-US']['ADR']['CTRY']['PDAT']
                    except:
                        inventor_addr_ctry = ""
                    inventor_address = inventor_addr_str + ", " + inventor_addr_city + ", " + inventor_addr_ctry
        
            params_3 = (str(inventor_full_name), str(inventor_address), str(b110_doc_number))
            sql_query_3 = '''INSERT OR IGNORE INTO Inventors VALUES (?, ?, ?)'''
            cursor.execute(sql_query_3, params_3)
            sqliteConnection.commit()

        # ASSIGNEES TABLE
        # 4. b110_doc_number from above
        assignee_name = ""
        assignee_address = ""
        
        if "B730" in sample_load_file['SDOBI']['B700']:
            if "B732US" in sample_load_file['SDOBI']['B700']['B730']:
                b732_ustype = sample_load_file['SDOBI']['B700']['B730']['B732US']['PDAT']
            else:
                b732_ustype = ""
            if "B731" in sample_load_file['SDOBI']['B700']['B730']:
                # assignee_arr = sample_load_file[i]['SDOBI']['B700']['B730']['B731']
                try:
                    assignee_name = sample_load_file['SDOBI']['B700']['B730']['B731']['PARTY-US']['NAM']['ONM']['STEXT']['PDAT']
                except:
                    assignee_name = " "
                try:
                    assignee_city = sample_load_file['SDOBI']['B700']['B730']['B731']['PARTY-US']['ADR']['CITY']['PDAT']
                except:
                    assignee_city = " "
                try:
                    assignee_state = sample_load_file['SDOBI']['B700']['B730']['B731']['PARTY-US']['ADR']['STATE']['PDAT']
                except:
                    assignee_state = " "
                try:
                    assignee_ctry = sample_load_file['SDOBI']['B700']['B730']['B731']['PARTY-US']['ADR']['CTRY']['PDAT']
                except:
                    assignee_ctry = " "
                assignee_address = assignee_city + ", " + assignee_state + ", " + assignee_ctry
        else:
            assignee_name = ""
            assignee_address = ""
            b732_ustype = 0
        
        params_4 = (str(assignee_name), str(assignee_address), b732_ustype, str(b110_doc_number))
        sql_query_4 = '''INSERT OR IGNORE INTO Assignees VALUES (?, ?, ?, ?)'''
        cursor.execute(sql_query_4, params_4)
        sqliteConnection.commit()

cursor.close()
if sqliteConnection:
    sqliteConnection.close()