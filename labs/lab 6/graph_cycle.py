# ----------------------------------------------------------
# Lab #6: Graph Cycle Detection
# General cryptarithmetic puzzle solver.
#
# Date: 03-Nov-2023
# Authors:
#           A01747433 Carlos Alberto Sánchez Calderón
#           A01753486 Diego Manjarrez Viveros
# ----------------------------------------------------------

from calendar import c
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

test2: Graph = {
    'A': ['D'],
    'B': ['E'],
    'C': ['E', 'I'],
    'D': ['A', 'E', 'F'],
    'E': ['B', 'C', 'D'],
    'F': ['D', 'G'],
    'G': ['F', 'H'],
    'H': ['G', 'I'],
    'I': ['C', 'H']
}


def depth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    stack: deque[str] = deque()
    reps: list[str] = []
    visited: set[str] = set()
    cycle: list[str] = []
    stack.append(start)

    while stack:
        current: str = stack.pop()
        if (current not in visited) and (current not in reps):
            yield current
            stack.extend(graph[current][::-1])
            visited.add(current)
            reps.append(current)
            cycle.append(current)
            if len(cycle) == 4:
                cycle = cycle[1:]
        elif (current in visited) and (current in reps) and (len(cycle) == 3) and (current == cycle[0]):
            cycle.append(current)
            return cycle


def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
    ...


if __name__ == '__main__':
    # print(f'{list(depth_first_search("A", g))}')
    print(f'{list(depth_first_search("A", test))}')
    print(f'{list(depth_first_search("B", test2))}')
