#import networkx as nx
#import matplotlib.pyplot as plt
import queue as Q

def search(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return
    
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        
        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break
        
        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))


def main():
    graph = {
    'Sports Complex': {'Siwaka':450},
    'Siwaka': {'Phase1A':10,'Phase1B':230,'Sports Complex':450},
    'Phase1A': {'Phase1B':100,'Madaraka':850,'Siwaka':10},
    'Phase1B': {'Phase2':112,'STC':50,'Siwaka':230},
    'STC': {'Parking Lot':250,'Phase1B':50},
    'Phase2':{'J1':600,'Phase3':500,'Phase1B':112},
    'J1':{'Madaraka':200,'Phase2':600},
    'Madaraka':{'Parking Lot':700,'J1':200,'Phase1A':850},
    'Phase3':{'Parking Lot':350,'Phase2':500},
    'Parking Lot':{'Phase3':350,'STC':250,'Madaraka':700},
    
}
    search(graph, "Sports Complex", "Parking Lot")

if __name__ == "__main__":
    main()