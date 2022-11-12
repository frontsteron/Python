from os.path import exists
from CSV_creating import csv_creating
from Writing import writing_scv
from Writing import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    csv_creating()

writing_scv()
writing_txt()