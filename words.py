__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2020, Research Squirrel Engineers"
__credits__ = ["Florian Thiery"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Research Squirrel Engineers"
__email__ = "rse@fthiery.de"
__status__ = "draft"

# import dependencies
import urllib2
import uuid
import pandas as pd
import os
import codecs
import datetime

# set paths
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in1 = dir_path + "\\" + "words.csv"
file_out1 = dir_path + "\\" + "out1.csv"

# read words.csv
response = urllib2.urlopen('https://raw.githubusercontent.com/ogi-ogham/oghamextractor/master/words/words.csv')
wordsCSV = response.read()
text_file1 = open(file_in1, "w")
text_file1.write(wordsCSV)
text_file1.close()

# read csv file
data1 = pd.read_csv(
    file_in1, # relative python path to subdirectory
    encoding='utf-8',
    sep=',', # deliminiter
    quotechar="\"",  # single quote allowed as quote character
    usecols=['word','variants'], # only load the  columns specified
    skiprows=0 # skip X rows of the file
)

# create triples from dataframe
outStr1 = ""
lines1 = []
for index1, row1 in data1.iterrows():
    lines1.append(row1['word'] + "," + row1['variants'])

# write output file
file1 = codecs.open(file_out1, "w", "utf-8")
for line1 in lines1:
    file1.write(line1)
    file1.write("\r\n")
file1.close()

# read ciic_inscriptions.csv
response = urllib2.urlopen('https://raw.githubusercontent.com/ogi-ogham/oghamextractor/master/ciic/ciic_inscriptions.csv')
ciicInsc = response.read()
text_file2 = open(file_in1, "w")
text_file2.write(ciicInsc)
text_file2.close()

# read csv file
data2 = pd.read_csv(
    file_in1, # relative python path to subdirectory
    encoding='utf-8',
    sep='\t', # deliminiter
    quotechar="\"",  # single quote allowed as quote character
    usecols=['label_en','P1684'], # only load the  columns specified
    skiprows=0 # skip X rows of the file
)

# create triples from dataframe
outStr2 = ""
lines2 = []
for index2, row2 in data2.iterrows():
    lines2.append(str(row2['label_en']) + "," + str(row2['P1684']))

# write output file
file2 = codecs.open(file_out2, "w", "utf-8")
for line2 in lines2:
    file2.write(line2)
    file2.write("\r\n")
file2.close()
