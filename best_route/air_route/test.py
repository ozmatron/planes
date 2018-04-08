'''
Created on 23 Mar 2018

@author: ozmatron
'''
from Airport import Airport
from Airport_atlas import Airport_atlas
from Currency import Currency
from Exchange_rate import Exchange

air1 = Airport('LHR')
air1.findinfo()
lat1 = air1.lat
long1 = air1.long
country1 = air1.country

print(air1.findinfo())

air2 = Airport('DUB')
air2.findinfo()
lat2 = air2.lat
long2 = air2.long
country2 = air2.country

print(air2.findinfo())

route1 = Airport_atlas(lat1, long1, lat2, long2)
display = route1.find_distance()
print("Distance:", display)

air1_currency = Currency(country1)
print("Currency:", air1_currency.findcurrency())

rate = Exchange(air1_currency.findcurrency())
print("Exchange rate:", rate.findrate())



