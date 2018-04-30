'''
Created on 21 Apr 2018

@author: ozmatron
'''
import csv

class Aircraft:
    
    def __init__(self, aircraft):
        self.range = 0
        self.aircraft = aircraft
    
    """Find the range of aircraft, return it in km"""    
    def find_range(self):
        with open('aircraft.csv', 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == self.aircraft:
                    if row[2] == 'imperial':
                        range_imperial = row[4]
                        self.range += float(range_imperial)*1.6
                    else:
                        range_metric = row[4]
                        self.range += float(range_metric)
        return self.range
