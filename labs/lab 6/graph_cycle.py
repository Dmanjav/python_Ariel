# ----------------------------------------------------------
# Lab #6: Graph Cycle Detection
# General cryptarithmetic puzzle solver.
#
# Date: 03-Nov-2023
# Authors:
#           A01747433 Carlos Alberto Sánchez Calderón
#           A01753486 Diego Manjarrez Viveros
# ----------------------------------------------------------

from typing import Optional

Graph = dict[str, list[str]]

"""
Problem solved with help of:
https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
"""


def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:

    visited: set[str] = set()
    stack: list[str] = []

    def dfs(node, parent):
        visited.add(node)
        stack.append(node)

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor not in visited:
                result = dfs(neighbor, node)
                if result:
                    return result
            if neighbor in stack:
                first = [stack[stack.index(neighbor)]]
                return stack[stack.index(neighbor):] + first
        stack.pop()

        return None

    if initial not in visited:
        cycle = dfs(initial, None)
        if cycle:
            return cycle
    return None

# def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
#     stack: deque[str] = deque()
#     visited: set[str] = set()
#     visited2: set[str] = set()
#     stack.append(initial)
#     while stack:
#         current: str = stack.pop()
#         if current not in visited:
#             yield current
#             stack.extend(graph[current][::-1])
#             visited.add(current)
#         elif (current in visited) and (current not in visited2):
#             yield current
#             elems = list(visited)
#             elems.append(current)
#             return elems
#     return None


if __name__ == '__main__':
    print(has_cycle('A', {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }))

    print(has_cycle(
        'C', {
            'A': ['B'],
            'B': ['A', 'C'],
            'C': ['B', 'D'],
            'D': ['C'],
        })
    )

    print(has_cycle('A', {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }))
