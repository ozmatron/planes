'''
Created on 22 Mar 2018

@author: ozmatron
'''
import csv

class Airport:
    
    def __init__(self):
        self.airport_dict = {}
        
    def make_dict(self):
        with open('/Users/ozmatron/Desktop/Algo/airport.csv', 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.airport_dict[row[4]] = {}
                self.airport_dict[row[4]]["country"] = row[3]
                self.airport_dict[row[4]]["city"] = row[2]
                self.airport_dict[row[4]]["name"] = row[1]
                self.airport_dict[row[4]]["long"] = float(row[7])
                self.airport_dict[row[4]]["lat"] = float(row[6])
        return self.airport_dict
    
#    def __str__(self):
#        return 'Country: {} - City: {} - Airport name: {}'.format(self.airport_dict)
