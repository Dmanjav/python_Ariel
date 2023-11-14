# ----------------------------------------------------------
# Lab #7: Dijkstra’s Shortest-Path Tree
#
# Date: 17-Nov-2023
# Authors:
#           A01747433 Carlos Alberto Sánchez Calderón
#           A01753486 Diego Manjarrez Viveros
# ----------------------------------------------------------

import heapq

WeightedGraph = dict[str, set[tuple[str, float]]]


def dijkstra_spt(
        initial: str,
        graph: WeightedGraph) -> tuple[dict[str, float], WeightedGraph]:
    unvisited_nodes = list(graph.keys())
    shortest_distances: dict[str, float] = {initial: 0}
    previous_nodes: dict[str, str] = {}
    max_value = float('inf')  # Assign the infinity value to max_value

    for node in unvisited_nodes:
        if node != initial:
            shortest_distances[node] = max_value
    shortest_distances[initial] = 0
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if node in shortest_distances:
                if current_min_node is None:
                    current_min_node = node
                elif (shortest_distances[node]
                      < shortest_distances[current_min_node]):
                    current_min_node = node

        # Get the neighbors of the current node
        neighbors = graph[current_min_node]
        for neighbor in neighbors:
            distance = shortest_distances[current_min_node] + neighbor[1]
            if (neighbor[0] not in shortest_distances or
                    distance < shortest_distances[neighbor[0]]):
                shortest_distances[neighbor[0]] = distance
                previous_nodes[neighbor[0]] = current_min_node
        unvisited_nodes.remove(current_min_node)
    return shortest_distances, previous_nodes


if __name__ == '__main__':
    print('Dijkstra’s Shortest-Path Tree')
    print('-------------------------------')
    print('Graph: ')
    print('A: {(B, 5), (C, 10), (E, 6)')
    print('B: {(A, 5), (D, 2)}')
    print('C: {(A, 10), (D, 1), (E, 3)}')
    print('D: {(B, 2), (C, 1), (E, 4)}')
    print('E: {(A, 6), (C, 3), (D, 4)}')
    print('-------------------------------')
    graph = {'A': {('B', 5), ('C', 10), ('E', 6)},
             'B': {('A', 5), ('D', 2)},
             'C': {('A', 10), ('D', 1), ('E', 3)},
             'D': {('B', 2), ('C', 1), ('E', 4)},
             'E': {('A', 6), ('C', 3), ('D', 4)},
             }
    print(dijkstra_spt('A', graph))
