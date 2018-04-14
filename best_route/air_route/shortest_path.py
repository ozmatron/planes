'''
Created on 23 Mar 2018

@author: ozmatron
'''
graph = {1: ['DUB', 'SXF', 1328.27], 2: ['DUB', 'LHR', 448.89], 3: ['DUB', 'CPH', 1241.54], 4: ['DUB', 'NYO', 1546.53], 5: ['SXF', 'DUB', 1328.27], 6: ['SXF', 'LHR', 962.55], 7: ['SXF', 'CPH', 364.46], 8: ['SXF', 'NYO', 743.53], 9: ['LHR', 'DUB', 629.75], 10: ['LHR', 'SXF', 1350.36], 11: ['LHR', 'CPH', 1373.66], 12: ['LHR', 'NYO', 1914.54], 13: ['CPH', 'DUB', 166.37], 14: ['CPH', 'SXF', 48.84], 15: ['CPH', 'LHR', 131.21], 16: ['CPH', 'NYO', 58.39], 17: ['NYO', 'DUB', 169.04], 18: ['NYO', 'SXF', 81.27], 19: ['NYO', 'LHR', 149.16], 20: ['NYO', 'CPH', 47.63]}


itinerary  = ['DUB','SXF','LHR','CPH','NYO']
limit = len(itinerary)
start = 'DUB'
visited = []
visited_len = len(visited)
sub_total = 0

while visited_len < limit:
    current_cost_dict = {}
    for key, value in graph.items():
        if graph[key][0] not in visited and graph[key][1] not in visited and graph[key][0] == start:
            current_cost = graph[key][2]
            next_hop = graph[key][1]
            current_cost_dict[next_hop] = current_cost;
    
    visited.append(start)
    print("the dict", current_cost_dict)
    # Adapted from: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php
    best_hop = min(current_cost_dict.keys(), key=(lambda k: current_cost_dict[k]))
    best_price = current_cost_dict[best_hop]
    print(best_hop)
    start = best_hop
    sub_total += best_price
    current_cost_dict.clear()
    if len(visited) == 4:
        visited.append(start)
        for key, value in graph.items():
            if graph[key][0] == start and graph[key][1] == 'DUB':
                last_cost = graph[key][2]
                print(last_cost)
                sub_total += last_cost
                visited.append('DUB')
    print(sub_total)
    print(visited)
    print(start)
    if len(visited) > 5:
        break




