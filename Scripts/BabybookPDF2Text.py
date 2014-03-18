#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, string, os
import time
import csv
import re


# This is the basic command we'll run to convert the PDFs to text	
BASE_LIST_CMD = 'pdftotext -layout '

# Babybook source
os.chdir('/Users/damian/Documents/Lake-Hill-Analytics/data/MappingNC/SourceData')
reader = csv.reader(open('babybookSource.txt', 'r'), delimiter="|")

# create a subdirectory called 'babybook-PDFs'
LIST_PAGES_SUBDIR = 'babybook-PDFs'

d = os.getcwd()

if not os.path.exists(d + '/' + LIST_PAGES_SUBDIR) :
	os.mkdir(d + '/' + LIST_PAGES_SUBDIR)
	print 'Created directory: ' + d + '/' + LIST_PAGES_SUBDIR
	
os.chdir(d + '/' + LIST_PAGES_SUBDIR)


for row in reader :

	try:
		textname = re.sub(r'\.pdf$', '.txt', row[0])
	   	command = BASE_LIST_CMD + str(row[0]) + ' ' + textname
	   	
	   	os.system(command)
	   	time.sleep(4)
	   	
	   	print 'Successfully converted: ' + str(row[0])
    	
	except:
    		print 'Failed to convert ' + str(row[0])