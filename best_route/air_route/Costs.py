'''
Created on 2 Apr 2018

@author: ozmatron
'''
'''
Created on 23 Mar 2018

@author: ozmatron
'''
from air_route.Airport import Airport
from air_route.Airport_atlas import Airport_atlas
from air_route.Currency import Currency
from air_route.Exchange_rate import Exchange
import collections

class Costs(Airport, Airport_atlas, Currency, Exchange):
    
    cache = {}
    airport_dict = Airport().make_dict()
    currency_dict = Currency().make_dict()
    xchange_dict = Exchange().make_dict()
    
    def __init__(self, itinerary, range):
        self.itinerary = itinerary
        self.range = range
        self.all_costs = {}      
    
    def find_costs(self):
        for i in self.itinerary:
            for j in self.itinerary:
                if i == j:
                    continue
                ports_value = [i,j]
                ports_key = (i,j)
                self.all_costs[ports_key] = ports_value      
     
        for key in self.all_costs.keys():
            #See if it's in cache
            if key in self.cache.keys():
                the_value = self.cache.get(key)
                self.all_costs[key].append(the_value[2])
            #Find it in the csv docs then
            else:
                for prime_key in self.all_costs:                  
                    for key, value in self.airport_dict.items():
                        if key == self.all_costs[prime_key][0]:
                            info1 = value
                        if key == self.all_costs[prime_key][1]:
                            info2 = value
                                 
                    for key, value in self.currency_dict.items():
                        if key == info1['country']:
                            currency1 = value
                        if key == info2['country']:
                            currency2 = value
                              
                    for key, value in self.xchange_dict.items():
                        if key == currency1:
                            rate1 = value
                        if key == currency2:
                            rate2 = value
                      
                    route = Airport_atlas(info1['lat'], info1['long'], info2['lat'], info2['long']).find_distance()
                    if route > self.range:
                        self.all_costs[prime_key].append("Too far!") 
                    else:
                        cost = route / float(rate1)
                        self.all_costs[prime_key].append(round(cost,2))   
                self.cache.update(self.all_costs)
            return self.all_costs
        
    
    def __str__(self):
        return 'Current cache: {}'.format(self.cache)

