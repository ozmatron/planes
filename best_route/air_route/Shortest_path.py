'''
Created on 23 Mar 2018

@author: ozmatron
'''
from itertools import permutations

class Shortest_path():
    
    def __init__(self, graph, itinerary):
        self.graph = graph
        self.itinerary = itinerary
    
    """Find the most economical route (visiting all nodes) and back home"""
    def path_finder(self):
        # Find the cheapest hop from the start node
        aircraft_error = ""
        start = self.itinerary[0]          
        start_cost_dict = {}
        for key, value in self.graph.items():
            if self.graph[key][0] == start:
                # Check if range check inserted a string 
                if isinstance(self.graph[key][2], float):
                    current_cost = self.graph[key][2]
                    next_hop = self.graph[key][1]
                    start_cost_dict[next_hop] = current_cost
        # Check if aircraft has range to even leave home                
        if start_cost_dict == {}:
            aircraft_error += "Cannot make the distance, get a bigger plane"
            return aircraft_error
        else:
            # Adapted from: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php
            best_hop = min(start_cost_dict.keys(), key=(lambda k: start_cost_dict[k]))
            best_price = start_cost_dict[best_hop]
            # Create new array for rest of method, begin with first hop
            visiting = [best_hop]
            # Fill new array with other unvisited nodes
            for i in self.itinerary:
                if i not in visiting and i != start:
                    visiting.append(i)
            # Create new array with all permutations of possible hops
            permu = []
            # From https://docs.python.org/2/library/itertools.html
            for combo in permutations(visiting, 2):
                permu.append(combo)
            
            route1_to_print = "" 
            route2_to_print = ""     
            route3_to_print = ""   
            route4_to_print = ""
            route5_to_print = ""
            route6_to_print = ""
            route_totals = []
            # Check if hop in route is out of range
            # If ok, add up all weights and create string of route
            if isinstance(self.graph[permu[0]][2], str) or isinstance(self.graph[permu[4]][2], str) or isinstance(self.graph[permu[8]][2], str) or isinstance(self.graph[permu[8][1],start][2], str):
                aircraft_error += "error"
            else:    
                route1 = self.graph[permu[0]][2] + self.graph[permu[4]][2] + self.graph[permu[8]][2] + self.graph[permu[8][1],start][2] + best_price
                route1_to_print += start + " → " + str(permu[0][0]) + " → " + str(permu[4][0]) + " → " + str(permu[8][0])  + " → " + str(permu[8][1])  + " → " + start + ", Total cost: " + str(round(route1,2))
                route_totals.append(route1)
                
            if isinstance(self.graph[permu[0]][2], str) or isinstance(self.graph[permu[5]][2], str) or isinstance(self.graph[permu[11]][2], str) or isinstance(self.graph[permu[11][1],start][2], str):
                aircraft_error += "error"
            else:
                route2 = self.graph[permu[0]][2] + self.graph[permu[5]][2] + self.graph[permu[11]][2] + self.graph[permu[11][1],start][2] + best_price
                route2_to_print += start + " → " + str(permu[0][0]) + " → " + str(permu[5][0]) + " → " + str(permu[11][0])  + " → " + str(permu[11][1])  + " → " + start + ", Total cost: " + str(round(route2,2))
                route_totals.append(route2)
            
            if isinstance(self.graph[permu[1]][2], str) or isinstance(self.graph[permu[7]][2], str) or isinstance(self.graph[permu[5]][2], str) or isinstance(self.graph[permu[5][1],start][2], str):
                aircraft_error += "error"
            else:
                route3 = self.graph[permu[1]][2] + self.graph[permu[7]][2] + self.graph[permu[5]][2] + self.graph[permu[5][1],start][2] + best_price
                route3_to_print += start + " → " + str(permu[1][0]) + " → " + str(permu[7][0]) + " → " + str(permu[5][0])  + " → " + str(permu[5][1])  + " → " + start + ", Total cost: " + str(round(route3,2))
                route_totals.append(route3)
            
            if isinstance(self.graph[permu[1]][2], str) or isinstance(self.graph[permu[8]][2], str) or isinstance(self.graph[permu[10]][2], str) or isinstance(self.graph[permu[10][1],start][2], str):
                aircraft_error += "error"
            else:       
                route4 = self.graph[permu[1]][2] + self.graph[permu[8]][2] + self.graph[permu[10]][2] + self.graph[permu[10][1],start][2] + best_price
                route4_to_print += start + " → " + str(permu[1][0]) + " → " + str(permu[8][0]) + " → " + str(permu[10][0])  + " → " + str(permu[10][1])  + " → " + start + ", Total cost: " + str(round(route4,2))
                route_totals.append(route4)
            
            if isinstance(self.graph[permu[2]][2], str) or isinstance(self.graph[permu[10]][2], str) or isinstance(self.graph[permu[4]][2], str) or isinstance(self.graph[permu[4][1],start][2], str):
                aircraft_error += "error"
            else:
                route5 = self.graph[permu[2]][2] + self.graph[permu[10]][2] + self.graph[permu[4]][2] + self.graph[permu[4][1],start][2] + best_price
                route5_to_print += start + " → " + str(permu[2][0]) + " → " + str(permu[10][0]) + " → " + str(permu[4][0])  + " → " + str(permu[4][1])  + " → " + start + ", Total cost: " + str(round(route5,2))
                route_totals.append(route5)
                
            if isinstance(self.graph[permu[2]][2], str) or isinstance(self.graph[permu[11]][2], str) or isinstance(self.graph[permu[7]][2], str) or isinstance(self.graph[permu[7][1],start][2], str):
                aircraft_error += "error"
            else:
                route6 = self.graph[permu[2]][2] + self.graph[permu[11]][2] + self.graph[permu[7]][2] + self.graph[permu[7][1],start][2] + best_price
                route6_to_print += start + " → " + str(permu[2][0]) + " → " + str(permu[11][0]) + " → " + str(permu[7][0])  + " → " + str(permu[7][1])  + " → " + start + ", Total cost: " + str(round(route6,2))
                route_totals.append(route6)
            # Find lowest cost from all permutations
            if route_totals != []:
                best_price = min(route_totals)
            # Return appropriate string
            if aircraft_error != "":
                return "Cannot make the distance, get a bigger plane"
            elif best_price == route1:
                return route1_to_print
            elif best_price == route2:
                return route2_to_print
            elif best_price == route3:
                return route3_to_print
            elif best_price == route4:
                return route4_to_print
            elif best_price == route5:
                return route5_to_print
            else:
                return route6_to_print


