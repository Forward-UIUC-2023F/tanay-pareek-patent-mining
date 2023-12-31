import xmltodict
import json
import os
from pathlib import Path

def output_patent(xml_string):
    patent = xmltodict.parse(xml_string)
    with open(json_file, 'a') as f:
        json.dump(patent, f, indent=4)
        f.write(',\n')

def read_file(file):
    xml_string = ''
    with open(file, 'r') as f:
        for line in f:
            if (line.startswith('<?xml version') and xml_string != '') or line.startswith('\n'):
                output_patent(xml_string)
                xml_string = ''
            xml_string += line

import glob
os.chdir("/Users/tanay/Desktop/ResearchWork/2023")
count = 0
for file in glob.glob("*.xml"):
    xml_file = file
    json_file = Path(xml_file).stem
    json_file = json_file + ".json"
    f = open(json_file, 'w+')
    f.write('[\n')
    f.close()

    read_file(xml_file)

    f = open(json_file, 'a')
    f.write('{\n')
    f.write('}\n')
    f.write(']')
    f.close()
