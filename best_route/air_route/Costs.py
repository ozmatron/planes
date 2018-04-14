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

class Costs(Airport, Airport_atlas, Currency, Exchange):

    all_costs = {}
    key_value = 1
    airport_dict = Airport().make_dict()
    currency_dict = Currency().make_dict()
    xchange_dict = Exchange().make_dict()
    
    def __init__(self, itinerary):
        self.itinerary = itinerary       
    #itinerary  = ['DUB','SXF','LHR','CPH','NYO']
    
    def find_costs(self):
        for i in self.itinerary:
            ports = []
            for j in self.itinerary:
                if i == j:
                    continue
                ports = [i,j]
                self.all_costs[self.key_value] = ports
                self.key_value+=1      
        
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
            
            #print(info1) 
            route1 = Airport_atlas(info1['lat'], info1['long'], info2['lat'], info2['long']).find_distance()
                
            #print("Distance:", route1)
            cost = route1 * float(rate1)
            self.all_costs[prime_key].append(round(cost,2))   
            #print("Fuel cost:", round(cost,2))
        return self.all_costs
        #print(temp_dict)
           
        # print(Currency().make_dict())
        # print(Exchange().make_dict())





