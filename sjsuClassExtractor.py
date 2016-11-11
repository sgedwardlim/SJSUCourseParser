#! /usr/bin/env python3

import re
import csv

# Create the lecture regex

lectureRegex = re.compile('''

        # Looks for the class code matching pattern
        # eg. AFAM 002A
        ([A-Z]+[\s][0-9]+[A-Z]*)
        # Looks for the name of the class
        (.+)
        [\s][0-9]+[\s][0-9]+
        # Looks for everything and any character
        .+
        # Looks for the full name of the teacher matching pattern
        # eg. L ROGER-GEE
        ([A-Z][\s][A-Z]+[-]*[A-Z]+)[\n]
''', re.VERBOSE)

# create a new csv file in the same directory
outputFile = open('misc/output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

# Open file that contains the Data to be parsed in .txt format
file = open('misc/decodedata.txt', 'r')

regexMatches = lectureRegex.findall(file.read())

for match in regexMatches:
    print(match[1])
    outputWriter.writerow([match[0], match[1], match[2]])

outputFile.close()
