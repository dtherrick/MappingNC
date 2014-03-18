import sys, string, os

inFileName = "2011_10_NC_Unemp.csv"
outFileName = "2011_10_NC_Unemp_Modified.csv"

findStr= " County"                                  
replaceStr = ""

inFile = open(inFileName, 'r')
inFileStr = inFile.read()
inFile.close()  

outputStr = inFileStr.replace(findStr, replaceStr) #Find & Replace
outputStr = outputStr.replace(" Hanover", "_Hanover")
        
outFile = open(outFileName, 'w')
outFile.write(outputStr)
outFile.close()