import json
import re
from itertools import cycle

file_one = "/Users/tanay/Desktop/ResearchWork/R1_Umich_Ann_Arbor.txt"
file_two = "/Users/tanay/Desktop/ResearchWork/R1_UIUC.txt"
file_three = "/Users/tanay/Desktop/ResearchWork/R1_UCB.txt"

with open(file_one, 'r') as file:
    content = file.read()

with open(file_two, 'r') as file:
    content_2 = file.read()

with open(file_three, 'r') as file:
    content_3 = file.read()

names_umich = re.findall(r"'Name': '(.*?)'", content)
names_uiuc = re.findall(r"'Name': '(.*?)'", content_2)
names_ucb = re.findall(r"'Name': '(.*?)'", content_3)

faculty_umich = []
faculty_uiuc = []
faculty_ucb = []


count = 0
# Print the extracted names
for name in names_umich:
    if "Office" in name or "Title" in name or "Fax" in name or "Associate" in name:
        count += 1
        continue
    elif "," in name:
        cont = name.split(",")
        full_name = cont[1].strip() + " " + cont[0].strip()
        faculty_umich.append(full_name)
    else:
        faculty_umich.append(name.strip())

print(count)

for name in names_uiuc:
    if "," in name:
        parts = name.split(",")
        full_name = parts[1].strip() + " " + parts[0].strip()
        full_name = full_name.strip()
        faculty_uiuc.append(full_name)
    else:
        faculty_uiuc.append(name.strip())
    
    
for name in names_ucb:
    if "," in name:
        con = name.split(",")
        faculty_ucb.append(con[0].strip())
    else:
        faculty_ucb.append(name.strip())

# file_newone = "/Users/tanay/Desktop/ResearchWork/UMich_faculty.txt"
# file_newtwo = "/Users/tanay/Desktop/ResearchWork/UIUC_faculty.txt"
# file_newthree = "/Users/tanay/Desktop/ResearchWork/UCB_faculty.txt"

# f = open(file_newone, 'w')
# for n in faculty_umich:
#     f.write(n+"\n")
# f.close()

# f = open(file_newtwo, 'w')
# for n in faculty_uiuc:
#     f.write(n+"\n")
# f.close()

# f = open(file_newthree, 'w')
# for n in faculty_ucb:
#     f.write(n+"\n")
# f.close()