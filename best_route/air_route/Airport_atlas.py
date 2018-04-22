'''
Created on 22 Mar 2018

@author: ozmatron
'''

#code adapted from lab5 solutions

from math import pi, sin, cos, acos

class Airport_atlas():
    
    radius_earth = 6371
    
    def __init__(self, lat1, long1, lat2, long2):
        self.lat1 = lat1
        self.lat2 = lat2
        self.long1 = long1
        self.long2 = long2

    def find_distance(self):
        theta1 = self.long1 * (2 * pi) / 360
        theta2 = self.long2 * (2 * pi) / 360
        phi1 = (90 - self.lat1) * (2*pi) / 360
        phi2 = (90 - self.lat2) * (2*pi) / 360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * self.radius_earth
        rounded_distance = round(distance, 2)
        return rounded_distance
    
    