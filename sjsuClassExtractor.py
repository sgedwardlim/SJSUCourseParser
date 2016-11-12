#! /usr/bin/env python3

import re
import csv

# Create the lecture regex
lectureRegex = re.compile('''
        # Sample Data
        # LING 203 SEMANTIC STRUC 01 47621 3 SEM P 13/15 MW 1500-1615 08/24/16-12/12/16 CL 205 K MOORE
        # LING 298 SPEC STUDIES 01 45315 1-4 SUP 61,73 P 0/0 TBA TBA 08/24/16-12/12/16
        ([A-Z]+\s\d+\S+)
        \s+
        (?:\(button\)\s*?)?(?:\(button\)\s*?)?
        ([A-Z]+.+?)
        \s\d+\s\d+.+?
        (\d\d\/\d\d\/\d\d)
        -
        (\d\d\/\d\d\/\d\d)
        \s?
        (?:.*?([A-Z]\s[A-Z]+-*[A-Z]+))?
        \s
''', re.VERBOSE)

# create a new csv file in the same directory
outputFile = open('misc/output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

# Open file that contains the Data to be parsed in .txt format
file = open('misc/sjsuclassdata-utf8.txt', 'r')

regexMatches = lectureRegex.findall(file.read())
count = 0

for match in regexMatches:
    count += 1
    print(count * 100 / len(regexMatches))
    outputWriter.writerow([match[0], match[1], match[2], match[3], match[4]])

outputFile.close()
