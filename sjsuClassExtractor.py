#! /usr/bin/env python3

import re
import csv

# Create the lecture regex


lectureRegex = re.compile('''
        ([A-Z]+\s\d+[A-Z]*)
        (.+?)
        \s\d+\s\d+.+?
        (\d\d\/\d\d\/\d\d)
        -
        (\d\d\/\d\d\/\d\d)
        \s
        (?:.*?([A-Z]\s[A-Z]+-*[A-Z]+))?
''', re.VERBOSE)

# create a new csv file in the same directory
outputFile = open('misc/output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

# Open file that contains the Data to be parsed in .txt format
file = open('misc/sjsuclassdata-utf8.txt', 'r')

regexMatches = lectureRegex.findall(file.read())

for match in regexMatches:
    print(match[1])
    outputWriter.writerow([match[0], match[1], match[2], match[3], match[4]])

outputFile.close()
