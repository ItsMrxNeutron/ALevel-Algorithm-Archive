



from binary_tree.creation import BinaryTree
from typing import Union

def traverse(tree:BinaryTree, wanted:int) -> Union[int, None]:
    curr = tree.root
    for i in range(len(tree)):  # worst case = O(n), therefore there can be only n operations occuring at maximum
        if wanted == tree.memory[curr].data:
            return curr
        if wanted <= tree.memory[curr].data:
            curr = tree.memory[curr].left_ptr
        else:
            curr = tree.memory[curr].right_ptr
    else:
        return None










