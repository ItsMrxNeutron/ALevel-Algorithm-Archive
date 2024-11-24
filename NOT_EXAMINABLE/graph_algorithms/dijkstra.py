

from graph_data_structures.adjacency_list import AdjacencyListGraph

import heapq  # i cannot be bothered enough to implement a minheap

INFINITE = float('inf')

def adjacency_list_dijkstra(graph: AdjacencyListGraph, source: int, destination: int) -> tuple[list, list]:
    
    distance = [INFINITE] * len(graph)
    predecessor = [None] * len(graph)
    distance[source] = 0
    minheap = []
    heapq.heappush(minheap, (0, source))
    
    while minheap:
        vertex_dist, current_vertex = heapq.heappop(minheap)
        if distance[current_vertex] == vertex_dist:
            for temp_edge in graph[current_vertex]:
                vertex_destination = temp_edge[0]
                edge_weight = temp_edge[1]
                if distance[vertex_destination] > distance[current_vertex] + edge_weight:
                    distance[vertex_destination] = distance[current_vertex] + edge_weight
                    predecessor[vertex_destination] = current_vertex
                    heapq.heappush(minheap, (distance[vertex_destination], vertex_destination))
    return distance, predecessor

def get_path(predecessor: list[int | None], source: int, destination: int):
    path = [destination]
    backtrace = destination
    while backtrace != source:
        path.append(predecessor[backtrace])
        backtrace = predecessor[backtrace]
    return path[::-1]

if __name__ == "__main__":
    a = AdjacencyListGraph()
    a.add_vertex()
    a.add_vertex()
    a.add_vertex()
    a.add_vertex()
    a.add_vertex()
    a.add_vertex()
    
    a.add_edge(0, 1, 10)
    a.add_edge(1, 2, 25)
    
    a.add_edge(3, 2, 1)
    a.add_edge(0, 3, 90)
    
    a.add_edge(2, 4, 3)
    a.add_edge(4, 5, 5)
    
    print(a)
    
    distance, predecessor = adjacency_list_dijkstra(a, 0, 5)
    print(f"path: {get_path(predecessor, 0, 5)}")
    print(f"distance/cost: {distance[5]}")
    
