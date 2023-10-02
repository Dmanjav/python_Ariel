from typing import Any, Optional, Iterator
from collections import deque

Tree = Optional[list[Any]]

t: Tree = \
    ['A', 
     ['B',
      ['D', None, None],
      None],
     ['C',
      None,
      ['E',
       ['F', None, None],
       ['G', None, None]]]]
    

    
def in_order(root: Tree) -> Iterator[str]:
    if root:
        value, left, right = root
        yield from in_order(left)
        yield value
        yield from in_order(right)
        
# Depth First Search
def pre_order(root: Tree) -> Iterator[str]:
    if root:
        value, left, right = root
        yield value
        yield from pre_order(left)
        yield from pre_order(right)
        
def post_order(root: Tree) -> Iterator[str]:
    if root:
        value, left, right = root
        yield from post_order(left)
        yield from post_order(right)
        yield value
        
# Algunos dices que esté es el Breath First Search
def level_order(root: Tree) -> Iterator[str]:
    if root is None:
        return
    queue: deque[Tree] = deque()
    queue.append(root)
    while queue: 
        current = queue.popleft()
        if current:
            value, left, right = current
            queue.append(left)
            queue.append(right)
            yield value

if __name__ == '__main__':
    print(f'{list(in_order(t))}')
    print(f'{list(pre_order(t))}')
    print(f'{list(post_order(t))}')
    print(f'{list(level_order(t))}')