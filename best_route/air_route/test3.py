'''
Created on 8 Apr 2018

@author: ozmatron
'''
from Airport import Airport
from Airport_atlas import Airport_atlas
from Currency import Currency
from Exchange_rate import Exchange

airport_dict = Airport().make_dict()
currency_dict = Currency().make_dict()
xchange_dict = Exchange().make_dict()
itinerary  = ['LHR','DUB','SXF','CPH','NYO']

for key, value in airport_dict.items():
    if key == itinerary[0]:
        info1 = value
    if key == itinerary[1]:
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
print(info1['lat'])
print(info1['long'])
print(info2['lat'])
print(info2['long'])


route1 = Airport_atlas(info1['lat'], info1['long'], info2['lat'], info2['long']).find_distance()
    
print("Distance:", route1)
cost = route1 * float(rate1)
print("Fuel cost(€):", cost)