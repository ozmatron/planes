'''
Created on 23 Mar 2018

@author: ozmatron
'''
import collections

class Shortest_path():
    
    def __init__(self, graph, itinerary):
        self.graph = graph
        self.itinerary = itinerary
        self.visited = collections.deque()
        self.sub_total = 0

    def the_path(self):
        limit = len(self.itinerary)
        start = self.itinerary[0]
        
        for key, value in self.graph.items():     
            while len(self.visited) < limit:
                current_cost_dict = {}
                for key, value in self.graph.items():
                    if self.graph[key][0] not in self.visited and self.graph[key][1] not in self.visited and self.graph[key][0] == start:
                        current_cost = self.graph[key][2]
                        if isinstance(current_cost, float):
                            next_hop = self.graph[key][1]
                            current_cost_dict[next_hop] = current_cost
                if current_cost_dict == {}:
                    self.visited.appendleft('Too far!')
                else:           
                    self.visited.append(start)
                    # Adapted from: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php
                    best_hop = min(current_cost_dict.keys(), key=(lambda k: current_cost_dict[k]))
                    best_price = current_cost_dict[best_hop]
                    start = best_hop
                    self.sub_total += best_price
                    current_cost_dict.clear()
                    if len(self.visited) == limit - 1:
                        self.visited.append(start)
                        for key, value in self.graph.items():
                            if self.graph[key][0] == start and self.graph[key][1] == self.itinerary[0]:
                                last_cost = self.graph[key][2]
                                self.sub_total += last_cost
                                self.visited.append(self.itinerary[0])
                    if len(self.visited) > limit:
                        break
               
            return self.visited, self.sub_total




