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
#print (wordsCSV) # deliminter ,

response = urllib2.urlopen('https://raw.githubusercontent.com/ogi-ogham/oghamextractor/master/ciic/ciic_inscriptions.csv')
ciicIns = response.read()
#print (ciicIns) # deliminter tab
