

import json
import networkx as nx
from itertools import permutations

import numpy as np

def read_input_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def find_initial_tour(distances):
    num_nodes = len(distances)
    
    current_node = 0
    tour = [current_node]
    visited = set([current_node])

    for _ in range(num_nodes - 1):
        next_node = min(
            range(num_nodes),
            key=lambda node: distances[current_node][node] if node not in visited else np.inf
        )

        tour.append(next_node)

        visited.add(next_node)

        current_node = next_node

    return tour

    

def main():
    file_path = 'C:\\Hackathon\Input data\level0.json'
    data = read_input_from_json(file_path)
    neighbourhoods = data.get('neighbourhoods', [])
    restaurants = data.get('restaurants', {})
    
    loc_dist=[data['restaurants']['r0']['neighbourhood_distance']]
    loc_dist[0].insert(0,0)

    for neighbours in neighbourhoods.values():
        neighbour_dist=list()
        for dist in neighbours['distances']:
            neighbour_dist.append(dist)
        neighbour_dist.insert(0,0)
        loc_dist.append(neighbour_dist)
    #print("the loc",loc_dist)

    intial_tour=find_initial_tour(loc_dist)
    print(intial_tour)
    final=list()
    for i in range(len(intial_tour)):
        if(intial_tour[i]==0):
            str1="r0"
            final.append(str1)
        else:
            str1=""
            str1="n"+str(intial_tour[i]-1)
            final.append(str1)
    paths = {"v0":{'path':final}}
    print(paths)

    with open("C:\\Hackathon\\answers\\level0_output.json", "w") as outfile: 
        json.dump(paths, outfile)




if __name__ == "__main__":
    main()

