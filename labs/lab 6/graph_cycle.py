# ----------------------------------------------------------
# Lab #6: Graph Cycle Detection
# General cryptarithmetic puzzle solver.
#
# Date: 03-Nov-2023
# Authors:
#           A01747433 Carlos Alberto Sánchez Calderón
#           A01753486 Diego Manjarrez Viveros
# ----------------------------------------------------------

from collections import deque
import re
from turtle import position
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


""" Tried our own method but it didn't work :("""
# def has_cycle(initial: str, graph: Graph) -> Optional[list[str]]:
#     stack: deque[str] = deque()
#     visited: set[str] = set()
#     visited2: list[str] = []
#     stack.append(initial)
#     result: list[str] = []

#     while stack:
#         current: str = stack.pop()
#         if current not in visited:
#             result.append(current)
#             stack.extend(graph[current][::-1])
#             visited.add(current)
#         elif (current in visited) and (current not in visited2):
#             visited2.append(current)
#             while current not in visited:
#                 visited.pop()
#             for elem in visited:
#                 if elem in visited2:
#                     continue
#                 result.append(elem)
#             return result
#     return None


if __name__ == '__main__':
    print(has_cycle('A', {
        'A': ['B'],
        'B': ['A']
    }))

    print(has_cycle(
        'A', {
            'A': ['B'],
            'B': ['A', 'C'],
            'C': ['B']
        })
    )

    print(has_cycle(
        'A', {
            'A': ['B', 'C'],
            'B': ['A', 'C'],
            'C': ['A', 'B']
        }))
