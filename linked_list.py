





class NodePool:
    def __init__(self) -> None:
        self.node_pool = []
        self.head_ptr = -1
        self.tail_ptr = -1
        self.free_ptr = 0

    def add_node(self, data):
        if len(self.node_pool) == 0:
            self.head_ptr = self.free_ptr
        new_node = Node(data, self.free_ptr)
        self.node_pool.append(new_node)
        self.node_pool[self.free_ptr-1].next = self.free_ptr
        self.tail_ptr = self.free_ptr
        self.free_ptr += 1

    def raw_read_nodes(self):
        print([i for i in self.node_pool])
        print(f'{self.free_ptr=}')
        print(f'{self.head_ptr=}')
        print(f'{self.tail_ptr=}')


    def read_nodes(self):
        print([i.data for i in self.node_pool])
        print([i.next for i in self.node_pool])
        print([i.addr for i in self.node_pool])
        print(f'{self.free_ptr=}')
        print(f'{self.head_ptr=}')
        print(f'{self.tail_ptr=}')
        


    def sort_nodes(self):
        self.node_pool.sort(key=lambda x : x.data)
        for index in range(len(self.node_pool)-1):
            self.node_pool[index].next = self.node_pool[index+1].addr
        self.node_pool[-1].next = -1
        self.head_ptr = self.node_pool[0].addr
        self.tail_ptr = self.node_pool[-1].addr

    
    def search_node(self, wanted_data):
        for i in self.node_pool:
            if i.data == wanted_data:
                return i.addr
        return None

    def insert_node(self, addr_before, data):
        print(len(self.node_pool))
        for i in range(len(self.node_pool)):
            u = self.node_pool[i]
            if u.addr == addr_before:
                x = Node(data, self.free_ptr)
                x.next = self.node_pool[i+1].addr
                self.node_pool[i].next = self.free_ptr
                self.free_ptr += 1
                self.node_pool.insert(i, x)
                return 
                

    

        

class Node:
    def __init__(self, data:int, addr, next_addr = -1) -> None:
        self.data = data
        self.addr = addr
        self.next = next_addr

    

np = NodePool()

test_data = [34, 20, 14, 77, 73, 17, 25, 2, 47, 31]
[np.add_node(i) for i in test_data]

np.read_nodes()
np.insert_node(2, 420)
np.read_nodes()




