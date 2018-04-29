'''
Created on 21 Apr 2018

@author: ozmatron
'''
from air_route.Costs import Costs
from air_route.Aircraft import Aircraft
from air_route.Shortest_path import Shortest_path
import csv
import collections
try:
    with open('/Users/ozmatron/Desktop/Algo/test.csv', newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            list = line
            aircraft = list[5]
            list = list[0:5]
            range = Aircraft(aircraft).find_range()
            costs_dict = Costs(list,range).find_costs()
            
            the_path = Shortest_path(costs_dict,list).path_finder()
            print(the_path)
            if the_path != "Cannot make the distance, get a bigger plane":
                output = []
                x = 0
                y = 3
                while x < 34:
                    output.append(the_path[x:y])
                    x+=6
                    y+=6
                output.append(the_path[x-1:])
                
                with open("/Users/ozmatron/Desktop/Algo/bestroutes.csv", "a") as writing_file:
                    writing = csv.writer(writing_file,lineterminator = '\n')
    
                    writing.writerow(output)
    
                writing_file.close()
except Exception:
    print("Make sure your CSV input only includes IATA codes for airports and aircraft!")

