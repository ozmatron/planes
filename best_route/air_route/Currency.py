'''
Created on 23 Mar 2018

@author: ozmatron
'''
import csv

class Currency:
    
    def __init__(self):
        self.currency_dict = {}
    
    """Make a dictionary of required currency info"""    
    def make_dict(self):
        with open('/Users/ozmatron/Desktop/Algo/countrycurrency.csv', 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.currency_dict[row[0]] = row[14]
        return self.currency_dict
