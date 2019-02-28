import docx2txt
import re

#Find a way to convert docx and pdf into txt files
#Easier for reading and parsing.
import string
#open File
with open("french.txt") as fh:
    count = 0
    for line in fh:
        if line != '':
            print(str(count)+ " " + line)
            count += 1
        #Split Paragraph on basis of '.' or ? or !.

        for l in re.split(r"\-",line):
            #Split line into list using space.
            print(  l )
