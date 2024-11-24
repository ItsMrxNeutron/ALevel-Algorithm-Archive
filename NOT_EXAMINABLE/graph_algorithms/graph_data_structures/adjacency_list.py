
# i hate imports
if __name__ == "__main__":
    from BaseGraph import Graph
else:
    from .BaseGraph import Graph


class AdjacencyListGraph(Graph):
    
    def __init__(self):
        self.adjacency_list: list[list] = []
        
    def __len__(self):
        return len(self.adjacency_list)
    
    def add_vertex(self):
        new_vertex = []
        self.adjacency_list.append(new_vertex)

    def add_edge(self, source_id: int, destination_id: int, weight: int = 0):
        # im not checking if the connection exists already
        # this will become a bootleg multigraph
        self.adjacency_list[source_id].append((destination_id, weight))
        
    def remove_edge(self, source_id: int, destination_id: int):
        for edge in self.adjacency_list[source_id]:
            if edge[0] == destination_id:
                self.adjacency_list[source_id].remove(edge)
                break
    
    def __getitem__(self, key: int):
        return self.adjacency_list[key]
    
    
    def __str__(self):
        string = ["["]
        for i, u in enumerate(self.adjacency_list):
            string.append(f"{i} -> {u}")
        string.append("]")
        return "\n".join(string)
    
    
if __name__ == "__main__":
    a = AdjacencyListGraph()
    a.add_vertex()
    a.add_vertex()
    a.add_vertex()
    a.add_edge(1, 2)
    
    print(a)
    a.remove_edge(1,2)
    print(a)