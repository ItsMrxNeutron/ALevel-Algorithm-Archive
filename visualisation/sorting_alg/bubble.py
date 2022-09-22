
from typing import List
from manim import *

def bubble_sort(x:list) -> list:
    changes = 1          # flag set to true to jumpstart the first cycle
    optimise_counter = 0    # 1 cycle of bubble sort guarentees at least one sorted element on the end
    while changes:          # since 0 in python is falsy, if changes is bigger than 0 means that there could still be an unsorted element
        
        changes = 0
        for i in range(len(x)-1 - optimise_counter):
            # one cycle of the sort
            if x[i] > x[i+1]:
                temp = x[i+1]
                x[i+1] = x[i]
                x[i] = temp
                changes += 1
        optimise_counter += 1   # one extra element is sorted, we do not need to check it anymore
    return x


test_list = [9,5,1,5,2,2]

print(bubble_sort(test_list))


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




