#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, string, os
import time
import urllib2
import csv


# This is the basic address of the babybook PDFs. The indivudual file names come next
BASE_LIST_URL = 'http://www.schs.state.nc.us/SCHS/births/babybook/2010/'

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
	   	page = urllib2.urlopen(BASE_LIST_URL + str(row[0]))
	   	f = open(str(row[0]), "wb")
		f.write(page.read())
	   	f.close()
	   	time.sleep(4)
	   	print 'Successfully grabbed: ' + BASE_LIST_URL + str(row[0])
    	
	except urllib2.URLError:
    		print 'Failed to fetch ' + BASE_LIST_URL + str(row[0])