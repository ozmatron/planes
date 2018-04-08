'''
Created on 2 Apr 2018

@author: ozmatron
'''
'''
Created on 23 Mar 2018

@author: ozmatron
'''
from Airport import Airport
from Airport_atlas import Airport_atlas
from Currency import Currency
from Exchange_rate import Exchange

airport_dict = Airport().make_dict()
currency_dict = Currency().make_dict()
xchange_dict = Exchange().make_dict()
itinerary  = ['DUB','SXF','LHR','CPH','NYO']

all_costs = {}
temp_dict = {}
key_value = 1
for i in itinerary:
    ports = ()
    for j in itinerary:
        if i == j:
            continue
        ports = (i,j)
        temp_dict[key_value] = ports
        all_costs[ports] = None
        key_value+=1      
      
for prime_key in temp_dict:
    #print(all_costs[prime_key][0])
              
    for key, value in airport_dict.items():
        if key == temp_dict[prime_key][0]:
            info1 = value
        if key == temp_dict[prime_key][1]:
            info2 = value
                
    for key, value in currency_dict.items():
        if key == info1['country']:
            currency1 = value
        if key == info2['country']:
            currency2 = value
             
    for key, value in xchange_dict.items():
        if key == currency1:
            rate1 = value
        if key == currency2:
            rate2 = value
        
    route1 = Airport_atlas(info1['lat'], info1['long'], info2['lat'], info2['long']).find_distance()
        
    #print("Distance:", route1)
    cost = route1 * float(rate1)
    for key in all_costs:
        all_costs[key] = round(cost,2)
        
    #final_dict[key_value] = ports
    print("Fuel cost:", round(cost,2))
print(all_costs)
#print(temp_dict)
   
# print(Currency().make_dict())
# print(Exchange().make_dict())





