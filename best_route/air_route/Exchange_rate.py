'''
Created on 23 Mar 2018

@author: ozmatron
'''
import csv

class Exchange:
    def __init__(self):
        self.xchange_dict = {}
        
    def make_dict(self):
        with open('/Users/ozmatron/Desktop/Algo/currencyrates.csv', 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.xchange_dict[row[1]] = row[2]
        return self.xchange_dict