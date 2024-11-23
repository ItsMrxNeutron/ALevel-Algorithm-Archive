
from random import randint, randrange


NULL_PTR = -1
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.curr = None
        self.free = 1
        self.memory = []
    
    def add_node(self, data):
        if self.root is None:
            self.root = 0
            self.memory.append(Node(data)) # root node
        # leaf nodes below
        self.curr = self.root
        while True:
            if data <= self.memory[self.curr].data:
                if self.memory[self.curr].left_ptr == NULL_PTR:
                    # check if end of tree
                    self.memory[self.curr].left_ptr = self.free
                    self.memory.append(Node(data))
                    self.free += 1
                    return self
                # go left
                self.curr = self.memory[self.curr].left_ptr
            else:
                if self.memory[self.curr].right_ptr == NULL_PTR:
                    # check if end of tree
                    self.memory[self.curr].right_ptr = self.free
                    self.memory.append(Node(data))
                    self.free += 1
                    return self
                self.curr = self.memory[self.curr].right_ptr


            
        
            


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left_ptr = -1
        self.right_ptr = -1

test_tree = BinaryTree()
[test_tree.add_node(randint(0, 30)) for i in range(10)]


from manim import *


class CreationTree(Scene):
    def construct(self):
        # self.draw_plane()
        self.nodes_anim()
    
    def draw_plane(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        self.play(Create(number_plane))

    def nodes_anim(self):
        self.text_pool = [Tex(test_tree.memory[i].data) for i in range(len(test_tree.memory))]
        self.node_pool = [Circle(color=BLUE, fill_opacity=0.4).surround(self.text_pool[i], buffer_factor=2.0) for i in range(len(test_tree.memory))]
        self.group_pool = [VGroup(self.node_pool[i], self.text_pool[i]) for i in range(len(self.node_pool))]
        
        

            
        self.draw_nodes(0, 0)
        self.play(LaggedStart(*[Write(self.group_pool[i]) for i in range(len(self.group_pool))], lag_ratio=0.1))
        # self.play(Write(self.text_pool[0]), Create(self.node_pool[0]))

    def draw_nodes(self, curr, depth, prev=0, direction = None):
        current = curr
        if direction is not None:
            if direction[0] > 0: 
                arrow = Arrow(start=self.node_pool[prev].point_at_angle(-(3/8)*PI), end=self.node_pool[curr].point_at_angle(0.5*PI))
            else:
                arrow = Arrow(start=self.node_pool[prev].point_at_angle(-(PI/2)-(3/8)*PI), end=self.node_pool[curr].point_at_angle(0.5*PI))
            self.play(Write(arrow))
        if current != NULL_PTR:
            # self.draw_nodes(test_tree[current].data)
            # set a circle to this depth
            if direction is None:
                self.group_pool[current].shift(*self.node_calc(depth))
            else:
                self.group_pool[current].shift(*self.node_calc(depth, direction))
            if test_tree.memory[current].left_ptr != NULL_PTR:
                depth += 1
                if test_tree.memory[current].data <= test_tree.memory[prev].data:
                    self.draw_nodes(test_tree.memory[current].left_ptr, depth, curr, LEFT*2)
                else:
                    self.draw_nodes(test_tree.memory[current].left_ptr, depth, curr, LEFT*1.5)
            if test_tree.memory[current].right_ptr != NULL_PTR:
                depth += 1
                if test_tree.memory[current].data > test_tree.memory[prev].data:
                    self.draw_nodes(test_tree.memory[current].right_ptr, depth, curr, RIGHT*2)
                else:
                    self.draw_nodes(test_tree.memory[current].right_ptr, depth, curr, RIGHT*1.5)


    def node_calc(self, depth, direction = 0*DOWN):
        if direction is None:
            direction = 0*DOWN
        return [depth * 0.5 * DOWN, direction * 0.25 * depth]
        






