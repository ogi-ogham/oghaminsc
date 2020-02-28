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
file_out = dir_path + "\\" + "out.csv"

# read words.csv
response = urllib2.urlopen('https://raw.githubusercontent.com/ogi-ogham/oghamextractor/master/words/words.csv')
wordsCSV = response.read()
wordsCSV = str(wordsCSV)
#print (wordsCSV) # deliminter ,

# read csv file
data = pd.read_csv(
    wordsCSV, # relative python path to subdirectory
    encoding='utf-8',
    sep=',', # deliminiter
    quotechar="\"",  # single quote allowed as quote character
    usecols=['word'], # only load the  columns specified
    skiprows=0 # skip X rows of the file
    #na_values=['.', '??'] # take any '.' or '??' values as NA
)

response = urllib2.urlopen('https://raw.githubusercontent.com/ogi-ogham/oghamextractor/master/ciic/ciic_inscriptions.csv')
ciicIns = response.read()
#print (ciicIns) # deliminter tab
