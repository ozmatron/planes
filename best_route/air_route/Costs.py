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
    
    """Make a graph of all connected nodes and weights, return as a dictionary"""
    def find_costs(self):
        # Construct the graph by filling keys with tuples of connected airports
        for i in self.itinerary:
            for j in self.itinerary:
                if i == j:
                    continue
                ports_value = [i,j]
                ports_key = (i,j)
                self.all_costs[ports_key] = ports_value      
        # Find the weights
        for key in self.all_costs.keys():
            # See if weight is in cache
            if key in self.cache.keys():
                the_value = self.cache.get(key)
                self.all_costs[key].append(the_value[2])
            # Not there? Find it in the csv docs then
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
                    # Check if chosen aircraft can make the distance, add string if not
                    if route > self.range:
                        self.all_costs[prime_key].append("Too far!") 
                    # If ok, divide distance by from_euro rate, add to graph as a weight
                    else:
                        cost = route / float(rate1)
                        self.all_costs[prime_key].append(round(cost,2)) 
                # Update the cache with new nodes and weights          
                self.cache.update(self.all_costs)
            return self.all_costs
        
    
    def __str__(self):
        return 'Current cache: {}'.format(self.cache)

