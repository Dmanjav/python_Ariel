def depth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    stack: deque[str] = deque()
    visited: set[str] = set()
    stack.append(start)
    while stack:
        current: str = stack.pop()
        if current not in visited:
            yield current
            stack.extend(graph[current][::-1])
            visited.add(current)