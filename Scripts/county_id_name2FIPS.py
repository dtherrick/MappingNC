import csv
import sys, string, os
import re

master_path = '/Users/damian/Documents/Lake-Hill-Analytics/data/MappingNC/'
countiesFile = master_path + 'SourceData/nc_fips.csv'

# FIPS Mapping in this File
reader = csv.reader(open(countiesFile, 'r'), delimiter=",")

# Source file with county names
if len(sys.argv[1]) > 0:
	inFileName = sys.argv[1]
else:
	sys.exit("No Input File!")

inFile = open(inFileName, 'r')
inFileStr = inFile.read()
inFile.close()

# Output file with county names replaced with FIPS ID
if len(sys.argv[2]) > 0:
	outFileName = sys.argv[2]
else:
	sys.exit("No Output File!")

fips = {}
past_header = False
past_first_row = False

for row in reader:
    if not past_header:
        past_header = True
        continue
    
    if not past_first_row:
        name = row[0]
        fips = row[1]
        outputStr = re.sub('(?i)' + re.escape(name), fips, inFileStr)
        past_first_row = True

    try:
        name = row[0]
        fips = row[1]
        outputStr = re.sub('(?i)' + re.escape(name), fips, outputStr)
    except:
        pass

# Write the output to a file
outFile = open(outFileName, 'w')
outFile.write(outputStr)
outFile.close()