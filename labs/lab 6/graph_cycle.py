# ----------------------------------------------------------
# Lab #6: Graph Cycle Detection
# General cryptarithmetic puzzle solver.
#
# Date: 03-Nov-2023
# Authors:
#           A01747433 Carlos Alberto Sánchez Calderón
#           A01753486 Diego Manjarrez Viveros
# ----------------------------------------------------------

from typing import Iterator, Optional
from collections import deque

Graph = dict[str, list[str]]

g: Graph = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'D'],
    'C': ['A', 'E', 'F'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['A', 'C', 'E', 'G'],
    'G': ['F']
}

test: Graph = {
    'A': ['B'],
    'B': ['A', 'D'],
    'C': ['D', 'E'],
    'D': ['C', 'E'],
    'E': ['C', 'D']
}


def depth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    stack: deque[str] = deque()
    visited: set[str] = set()
    cycle: list[str] = []
    stack.append(start)
    while stack:
        current: str = stack.pop()
        if (current not in cycle or cycle[0] == current):
            yield current
            stack.extend(graph[current][::-1])
            visited.add(current)
            
            if len(cycle) == 4 and cycle[0] != cycle[-1]:
                cycle.append(current)
                cycle = cycle[1:]
                print(cycle)
            elif len(cycle) == 4 and cycle[0] == cycle[-1]:
                return cycle
            else:
                return "Hola"
            
def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
    ...


if __name__ == '__main__':
    # print(f'{list(depth_first_search("A", g))}')
    print(f'{list(depth_first_search("A", test))}')