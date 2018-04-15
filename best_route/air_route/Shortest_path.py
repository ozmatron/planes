'''
Created on 23 Mar 2018

@author: ozmatron
'''

class Shortest_path():
    
    def __init__(self, graph, itinerary):
        self.graph = graph
        self.itinerary = itinerary
        self.visited = []
        self.sub_total = 0
#graph = {1: ['DUB', 'SXF', 1328.27], 2: ['DUB', 'LHR', 448.89], 3: ['DUB', 'CPH', 1241.54], 4: ['DUB', 'NYO', 1546.53], 5: ['SXF', 'DUB', 1328.27], 6: ['SXF', 'LHR', 962.55], 7: ['SXF', 'CPH', 364.46], 8: ['SXF', 'NYO', 743.53], 9: ['LHR', 'DUB', 629.75], 10: ['LHR', 'SXF', 1350.36], 11: ['LHR', 'CPH', 1373.66], 12: ['LHR', 'NYO', 1914.54], 13: ['CPH', 'DUB', 166.37], 14: ['CPH', 'SXF', 48.84], 15: ['CPH', 'LHR', 131.21], 16: ['CPH', 'NYO', 58.39], 17: ['NYO', 'DUB', 169.04], 18: ['NYO', 'SXF', 81.27], 19: ['NYO', 'LHR', 149.16], 20: ['NYO', 'CPH', 47.63]}

    def the_path(self):
        #itinerary  = ['DUB','SXF','LHR','CPH','NYO']
        limit = len(self.itinerary)
        start = 'DUB'
        
        while len(self.visited) < limit:
            current_cost_dict = {}
            for key, value in self.graph.items():
                if self.graph[key][0] not in self.visited and self.graph[key][1] not in self.visited and self.graph[key][0] == start:
                    current_cost = self.graph[key][2]
                    next_hop = self.graph[key][1]
                    current_cost_dict[next_hop] = current_cost;
            
            self.visited.append(start)
            #print("the dict", current_cost_dict)
            # Adapted from: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php
            best_hop = min(current_cost_dict.keys(), key=(lambda k: current_cost_dict[k]))
            best_price = current_cost_dict[best_hop]
            #print(best_hop)
            start = best_hop
            self.sub_total += best_price
            current_cost_dict.clear()
            if len(self.visited) == limit - 1:
                self.visited.append(start)
                for key, value in self.graph.items():
                    if self.graph[key][0] == start and self.graph[key][1] == 'DUB':
                        last_cost = self.graph[key][2]
                        #print(last_cost)
                        self.sub_total += last_cost
                        self.visited.append('DUB')
            #print("New total:", sub_total)
            #print("New start:", start)
            if len(self.visited) > 5:
                break
           
        return self.visited, self.sub_total




