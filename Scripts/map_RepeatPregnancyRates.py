import csv
import sys, string, os

# sample data
# Area Name,Year,Month,Adjusted,Unemployment Rate(%)
# Alamance,2000,00,Unadjusted,3.2
reader = csv.reader(open('2010_repeat_pregnancies15-19FIPS.txt', 'r'), delimiter="|")
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
        rate = float( row[3].strip() )
        unemployment[name] = rate
        rates_only.append(rate)
    except:
        pass

    # Determine the colors
    rates_only.sort()
    q1_index = int(0.2 * len(rates_only))
    q1 = rates_only[q1_index]
    q2_index = int(0.4 * len(rates_only))
    q2 = rates_only[q2_index]
    q3_index = int(0.6 * len(rates_only))
    q3 = rates_only[q3_index]
    q4_index = int(0.8 * len(rates_only))
    q4 = rates_only[q4_index]

    min_rate = rates_only[0]
    max_rateIndex = len(rates_only) - 1
    max_rate = rates_only[max_rateIndex]
    
    if rate > q4:
        color_class = 4
    elif rate > q3:
        color_class = 3
    elif rate > q2:
        color_class = 2
    elif rate > q1:
        color_class = 1
    else:
        color_class = 0
    
    color = colors[color_class]

    use_string = use_string + '<use ' + use_style_county + name + use_style_fill + color + '" />\n' 

use_string = use_string + '</svg>'

findStr="</svg>"

output = svg.replace(findStr, use_string)
print output

diagsStr1 = 'min: ' + str(min_rate) + '\nq1: ' + str(q1) + '\nq2: ' + str(q2) + '\nq3: ' + str(q3) + '\nq4: ' + str(q4) + '\nMax: ' + str(max_rate) + '\n'
diagsStr2 = 'Color 1: ' + colors[0] + '\nColor 2: ' + colors[1] + '\nColor 3: ' + colors[2] + '\nColor 4: ' + colors[3] + '\nColor 5: ' + colors[4]
diagsFile = open('Diags_RepeatPregnancyRates.txt', 'w')
diagsFile.write(diagsStr1)
diagsFile.write(diagsStr2)
diagsFile.close()