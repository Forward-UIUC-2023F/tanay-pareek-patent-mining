import sqlite3
# import Levenshtein
import re
import hmni


file_one = "/Users/tanay/Desktop/ResearchWork/berkeley_inventors.txt"
file_two = "/Users/tanay/Desktop/ResearchWork/illinois_inventors.txt"
file_three = "/Users/tanay/Desktop/ResearchWork/michigan_inventors.txt"

# First we remove the duplicate (name, patent_doc_number) entries from each file, if any

# unique_faculty_patents = set()
# with open(file_three, 'r') as input_file:
#     while True:
#         line = input_file.readline()
#         if not line:
#             break
#         name, d_number = line.split(":")
#         doc_number = d_number.strip()
#         if (name, doc_number) not in unique_faculty_patents:
#             unique_faculty_patents.add((name, doc_number))
        
# with open("/Users/tanay/Desktop/ResearchWork/UMich_nondup_patent.txt", "w") as file:
#     for (nam, num) in unique_faculty_patents:
#         file.write(nam + ": " + num + " " + "\n") 
    
# Now we match the similar sounding/same names into one using Levenshtein distance

# Read the text file and parse the entries
with open('/Users/tanay/Desktop/ResearchWork/UIUC_nondup_patent.txt', 'r') as file:
    lines = file.readlines()

matcher = hmni.Matcher(model='latin')

print(lines)

# # Create a dictionary to store names and corresponding numbers
# name_numbers = {}

# # Function to find similar names based on Levenshtein distance
# def find_similar_names(name, names):
#     threshold = 5  # Adjust the threshold as needed
#     similar_names = [other_name for other_name in names if Levenshtein.distance(name, other_name) < threshold]
#     return similar_names

# # Parse each line and populate the dictionary
# for line in lines:
#     parts = line.strip().split(':')
#     name = parts[0].strip()
#     number = int(parts[1].strip())

#     # Find similar names based on Levenshtein distance
#     similar_names = find_similar_names(name, name_numbers.keys())

#     # Combine numbers for similar names
#     if similar_names:
#         for similar_name in similar_names:
#             name_numbers[similar_name].append(number)
#     else:
#         name_numbers[name] = [number]

# # Print the combined entries
# for name, all_number in name_numbers.items():
#     print(f"{name}: {all_number}")

# ld = Levenshtein.distance("Kevin Chang", "Kevin Chen-Chuan Chang")
# print("LEV DIST:", ld)
    







# Basic test-cases

# 1. Every faculty-name has a position element involved - num of position tags should equal number of names outputted

file_one = "/Users/tanay/Desktop/ResearchWork/R1_Umich_Ann_Arbor.txt"
file_two = "/Users/tanay/Desktop/ResearchWork/R1_UIUC.txt"
file_three = "/Users/tanay/Desktop/ResearchWork/R1_UCB.txt"

with open(file_one, 'r') as file:
    content = file.read()

with open(file_two, 'r') as file:
    content_2 = file.read()

with open(file_three, 'r') as file:
    content_3 = file.read()

pos_umich = re.findall(r"'Position': '(.*?)'", content)
pos_uiuc = re.findall(r"'Position': '(.*?)'", content_2)
pos_ucb = re.findall(r"'Position': '(.*?)'", content_3)

pos_umich_len = len(pos_umich) - 321
pos_uiuc_len = len(pos_uiuc)
pos_ucb_len = len(pos_ucb)

with open('/Users/tanay/Desktop/ResearchWork/UIUC_faculty.txt', 'r') as fp:
    for count_uiuc, line in enumerate(fp):
        pass

names_uiuc = count_uiuc + 1

with open('/Users/tanay/Desktop/ResearchWork/UMich_faculty.txt', 'r') as fp:
    for count_umich, line in enumerate(fp):
        pass

names_umich = count_umich + 1

with open('/Users/tanay/Desktop/ResearchWork/UCB_faculty.txt', 'r') as fp:
    for count_ucb, line in enumerate(fp):
        pass

names_ucb = count_ucb + 1

# print(names_uiuc, names_umich, names_ucb)

print(pos_ucb_len, names_ucb)
print(pos_uiuc_len, names_uiuc)
print(pos_umich_len, names_umich)

# assert(pos_ucb_len == names_ucb)
assert(pos_uiuc_len == names_uiuc)
# assert(pos_umich_len == names_umich)



# Calculating False Positives



# Calculating False Negatives