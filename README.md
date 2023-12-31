# tanay-pareek-patent-mining

## Overview

This module is responsible for setting up the database with information from the USPTO Patent Grant Bibliographic section and then use the data to match the given faculty list of a specific university.

## Setup

1. pip 23.3.1 and python 3.11.7 were used when running this module.
2. Install necessary modules by running the following command line in the terminal:
   ```
   pip install -r requirements.txt
   ```
3. Go to https://bulkdata.uspto.gov/ and look for the **Patent Grant Bibliographic (Front Page) Text Data (JAN 1976 - PRESENT)**. Once found download the xml files for each year and move them into one place. Then, go to the scripts folder to run the xmltojsonconvert.py script in this repository based on the path of your xml files.
4. Download DB Browser for SQlite over here - https://sqlitebrowser.org/dl/. Once downloaded open and create a new database, manually adding tables and column names based on the schema provided in the images folder in this repository.
5. Run both the json extraction files in the database_setup folder in this repository to populate the database with the extracted data.
6. This section gives an overview of the repository's file structure:
   ```
   tanay-pareek-patent-mining/
    - database_setup/
        -- jsonextraction2002-2004.py
        -- jsonextraction2005on.py
    - Faculty_Data/
        -- R1_UCB.txt
        -- R1_UIUC.txt
        -- R1_Umich_Ann_Arbor.txt
    - images/
        -- database_schema.png
        -- algorithmic_design.png
    - output/
        -- berkeley_inventors.txt
        -- illinois_inventors.txt
        -- michigan_inventors.txt
        -- UCB_faculty.txt
        -- UCB_nondup_patent.txt
        -- UIUC_faculty.txt
        -- UIUC_nondup_patent.txt
        -- UMich_faculty.txt
        -- UMich_nondup_patent.txt
    - python_scripts/
        -- find_faculty_in_database.py
        -- find_faculty_in_inventors.py
        -- xmltojsonconvert.py
    - sql_queries/
        -- patent_queries.py
    - src/
        -- accuracy_analysis.py
    - README.md
    - requirements.txt
   ```
   * database_setup/jsonextraction2002-2004.py - extracts data from json files for the years 2002-2004.
   * database_setup/jsonextraction2005on.py - extracts data from json files for the years 2005-2022.
   * Faculty_Data/ - contains all the raw files with CS faculty information for 3 universities.
   * images/database_schema.png - contains the image for the database schema to follow in step 4 of Setup.
   * output/berkeley_inventors.txt - contains the list of all UC Berkeley faculty that have patents when searched for in the database.
   * output/illinois_inventors.txt - contains the list of all UIUC faculty that have patents when searched for in the database.
   * output/michigan_inventors.txt - contains the list of all UMich Ann-Arbor faculty that have patents when searched for in the database.
   * output/UCB_faculty.txt - contains a list of all the UCB faculty extracted from the raw data file in "Faculty_Data" folder. 
   * output/UCB_nondup_patent.txt - cotains a list of all the UC Berkeley faculty that have patents when searched for in the database after removing duplicates.
   * output/UIUC_faculty.txt - contains a list of all the UIUC faculty extracted from the raw data file in "Faculty_Data" folder. 
   * output/UIUC_nondup_patent.txt - cotains a list of all the UIUC faculty that have patents when searched for in the database after removing duplicates.
   * output/UMich_faculty.txt - contains a list of all the UMich faculty extracted from the raw data file in "Faculty_Data" folder. 
   * output/UMich_nondup_patent.txt - cotains a list of all the UMich Ann-Arbor faculty that have patents when searched for in the database after removing duplicates.
   * python_scripts/find_faculty_in_database.py - Script to match the faculty names from output/*university_name*_faculty.txt to the inventors in the database and output list in the format "illinois_inventors.txt" found in output.
   * python_scripts/find_faculty_in_inventors.py - Script to extract all faculty names from the raw data files found in Faculty_Data folder in the repository.
   * python_scripts/xmltojsonconvert.py - Script to convert xml file to json file.
   * sql_queries/patent_queries.py - file that runs basic queries when the database has been populated completely.
   * src/accuracy_analysis.py - Once the specific faculty and their corresponding patent document numbers are outputed, this script combines duplicates and tries to perform fuzzy name-matching on the output. It also tests that the data extraction works fine.
  
## Functional Design(Usage)
1. After Step 5 in setup, run python_scripts/find_faculty_in_inventors.py, editing the paths in the code as required.
2. Then run python_scripts/find_faculty_in_database.py, editing the paths within the code as required.
3. Lastly, run src/accuracy_analysis.py, once again editing the paths within the code as required.

## Code Demo Overview
Google drive link - https://drive.google.com/drive/u/2/folders/1psoHeCSVvQxPqiLeudqyNtMRioi_xkIy

## Algorithmic Design
* Step 1: When we run python_scripts/find_faculty_in_inventors.py, all faculty names from the raw data files are extracted.
* Step 2: When we run python_scripts/find_faculty_in_database.py, all faculty names previously extracted are matched with assignees in database and the final faculty and their corresponding patent document numbers are outputted.
* Step 3: When we run src/accuracy_analysis.py, we attempt to perform name deduplication as well as fuzzy name-matching and return the result. We also return the basic tests on data extraction.

<img width="601" alt="algorithmic_design" src="https://github.com/Forward-UIUC-2023F/tanay-pareek-patent-mining/assets/68942780/bf33aa7f-3cc7-4b1e-b5c8-a628f133512f">

## Issues and Future Work

* The fuzzy matching algorithm needs to be changed from Levenshtein and improved. Tried the hmni package, which is also unable to perform the proper name matching.
* Need to add tests for the validity of fuzzy name-matching once implemented correctly.
* Currently, the github repository does not have a proper functional design in that we need to run specific files on the whole to get our final output for all 3 universities. I need to add a small functional design change which would take a specific assignee i.e. specific university, and perform the faculty search_up.

## References

* Dataset (Patent Grant Bibliographic (Front Page) Text Data): https://bulkdata.uspto.gov/
* Data decoding (2002-2004): https://www.uspto.gov/sites/default/files/products/PatentGrantSGMLv19-Documentation.pdf
* Data decoding (2005-2012): https://bulkdata.uspto.gov/data/patent/grant/redbook/2007/PatentGrantXMLv4.2Documentation.doc

