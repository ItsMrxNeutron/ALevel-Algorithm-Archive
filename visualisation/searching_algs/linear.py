

from typing import List
from manim import *

def linear_search(x:list, wanted) -> int:
    for index in range(len(x)):
        if x[index] == wanted:
            return index
    return None                 # wanted element not in list


test_list = [35, 68, 7, 82, 35, 25, 40, 66, 44, 49, 50, 3, 61]
print(linear_search(test_list, 57))
def normalise(x):
    return [(i-min(test_list))/(max(test_list)-min(test_list)) for i in test_list]

class LinearSearch(Scene):
    def construct(self):
        self._list = test_list
        wanted = 40
        bars: List[Mobject] = []
        first_bar = None
        norm  = normalise(self._list)
        for i in range(len(self._list)):
            g = VGroup()
            rect= Rectangle(width=len(self._list)/20,
                                  height=norm[i]*5,
                                  color=BLUE
                                ).set_fill(BLUE, opacity=0.7).shift(DOWN)
            num = Integer(number=self._list[i]).shift(DOWN*3)
            if first_bar:
                rect = rect.align_to(first_bar, DOWN)
            else:
                first_bar = rect
            bars.append(g)
            g.add(rect, num).shift(RIGHT*len(self._list)*(i-5)/20)
            self.play(Create(g), run_time=0.25)
            
        
            
            
        
        pointer = Triangle(color=BLUE).scale(0.25).shift(DOWN*2.5).set_fill(BLUE, opacity=0.7)
        pointer = pointer.shift(LEFT*len(self._list)*5/20)
        self.play(Create(pointer), run_time=0.75)
        # algorithm part
        index = linear_search(self._list, wanted)
        for i in range(index):
            self.play(pointer.animate.shift(self.shift(RIGHT, 1)))
        self.play(Indicate(pointer), Indicate(bars[index]))

    def swap(self, bar1, bar2):
        ...

    def shift(self, direc, unit):
        return direc*(len(self._list)/20)* unit


