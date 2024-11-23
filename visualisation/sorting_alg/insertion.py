
from typing import List
from manim import *

test_list = [9,5,1,5,2,2]

def insertion_sort(_list):
    for next_val in range(1, len(_list)):
        val = _list[next_val]                       # current value held to be sorted in current cycle
        curr = next_val -1                          # makes current points to the element before the value holding
        while curr >= 0 and _list[curr] > val:      # check if: current is not out of list index, value is smaller than the one before
            _list[curr+1] = _list[curr]             # makes the next element in the list the one before
            curr -= 1
        _list[curr+1] = val                         # if the held value is bigger than the one before, sets the current index to the held value (this is the sorted place)
    return _list


# print(insertion_sort(test_list))


def normalise(x):
    return [(i-min(test_list))/(max(test_list)-min(test_list)) for i in test_list]

class InsertionSort(Scene):
    def construct(self):
        self._list = test_list
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
        
        s_bar = bars
        for next_val in range(1, len(self._list)):
            val = self._list[next_val]
            curr = next_val -1
            changes = 0
            s_bar_val = s_bar[next_val]
            bars[curr] = bars[curr].set_color(GREEN)
            while curr >= 0 and self._list[curr] > val:
                self._list[curr+1] = self._list[curr]
                s_bar[curr+1] = s_bar[curr]
                changes += 1
                curr -= 1
            self._list[curr+1] = val
            s_bar[curr+1] = s_bar_val
            self.play(bars[curr].animate.shift(self.shift(RIGHT, 1)))
            bars = s_bar
            self.play(bars[curr+1].animate.shift(self.shift(LEFT, changes)))
            


            # swapped_index = None
            # for i in range(len(diff_list)):
            #     if diff_list[i] != 0:
            #         swapped_index = i
            # self.play(bars[swapped_index].animate.shift(self.shift(RIGHT, diff_list[swapped_index]+1)))
            # for i in range(swapped_index+1, len(diff_list)):
            #     b = bars[i].animate.shift(LEFT)
            #     self.play(b)

    def swap_bars(self, b1:Rectangle, b2:Rectangle):
            x_coord_b1 = b1.get_x()
            b1 = b1.animate.match_x(b2)
            b2 = b2.animate.set_x(b1)
            return b1, b2

    def shift(self, direc, unit):
        return direc*(len(self._list)/20)* unit









