'''
Created on 21 Apr 2018

@author: ozmatron
'''
import unittest
from air_route.Airport import Airport
from air_route.Airport_atlas import Airport_atlas
from air_route.Currency import Currency
from air_route.Exchange_rate import Exchange

class Testing(unittest.TestCase):
    
    """Test if distance calculation is correct"""    
    def test_distance(self):
        self.lat1 = 53.421333
        self.long1 = -6.270075
        self.lat2 = 52.380001
        self.long2 = 13.5225
        route1 = Airport_atlas(self.lat1, self.long1, self.lat2, self.long2).find_distance()
        self.assertEqual(route1,1328.27)
    
    """Test if cost and exchange rate calculation is correct"""     
    def test_cost(self):
        self.airport_dict = Airport().make_dict()
        self.currency_dict = Currency().make_dict()
        self.xchange_dict = Exchange().make_dict()
        self.itinerary  = ['LHR','DUB']
        
        for key, value in self.airport_dict.items():
            if key == self.itinerary[0]:
                info1 = value
            if key == self.itinerary[1]:
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
                
        self.route1 = Airport_atlas(info1['lat'], info1['long'], info2['lat'], info2['long']).find_distance()
        self.cost = self.route1 * float(rate1)
        self.assertEqual(self.cost,629.747781)