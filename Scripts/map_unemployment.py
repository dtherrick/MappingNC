import csv
import sys, string, os

# sample data
# Area Name,Year,Month,Adjusted,Unemployment Rate(%)
# Alamance,2000,00,Unadjusted,3.2
reader = csv.reader(open('2011_10_NC_unemp_ByFIPS.csv', 'r'), delimiter=",")
svg = open('NorthCarolinaCountiesByFIPS.svg', 'r').read()

# color pallette
colors = ["#EDF8FB", "#B2E2E2", "#66C2A4", "#2CA25F", "#006D2C" ]

# filling the county map:
# use this code in the svg:
# <use xlink:href="#Dare" stroke="none" fill="red" />
use_style_county = 'stroke="none" xlink:href="#'
use_style_fill = '" fill="'
use_string = ""

unemployment = {}
rates_only = [] # To calculate quartiles
min_value = 100; max_value = 0; past_header = False

for row in reader:
    if not past_header:
        past_header = True
        continue
    
    try:
        name = row[0]
        rate = float( row[4].strip() )
        unemployment[name] = rate
        rates_only.append(rate)
    except:
        pass

    if rate > 12:
        color_class = 4
    elif rate > 10:
        color_class = 3
    elif rate > 8:
        color_class = 2
    elif rate > 6:
        color_class = 1
    else:
        color_class = 0
    
    color = colors[color_class]

    use_string = use_string + '<use ' + use_style_county + name + use_style_fill + color + '" />\n' 

use_string = use_string + '</svg>'

findStr="</svg>"

output = svg.replace(findStr, use_string)
print output