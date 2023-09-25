from comparable import C


def power_set(s: list[C]) -> list[list[C]]:
    if s:
        r = power_set(s[:-1])
        return r + [t + [s[-1]] for t in r]
    else:
        return [[]]


def sorted_nicely(s: list[list[C]]) -> list[list[C]]:

    def size_and_content(t: list[C]) -> tuple[int, list[C]]:
        return (len(t), t)

    return sorted(s, key=size_and_content)


def combinations(s: list[C], k: int) -> list[list[C]]:
    return [t for t in power_set(s) if len(t) == k]


def insert(x: C, s: list[C], i: int) -> list[C]:
    return s[:i] + [x] + s[i:]


def insert_everywhere(x: C, s: list[C]) -> list[list[C]]:
    return [insert(x, s, i) for i in range(len(s) + 1)]


def permute(s: list[C]) -> list[list[C]]:
    if s:
        return sum([insert_everywhere(s[0], t)
                    for t in permute(s[1:])],
                   [])
    else:
        return [[]]


def permutations(s: list[C], k: int) -> list[list[C]]:
    return sum([permute(t)
                for t in combinations(s, k)],
               [])

def permutations_with_repetition(s: list[C], k: int) -> list[list[C]]:
    if k == 0:
        return [[]]
    else:
        return sum([insert_everywhere(s[0], t)
                    for t in permutations_with_repetition(s, k - 1)],
                   [])
        
def combinations_with_repetition(s: list[C], k: int) -> list[list[C]]:
    if k == 0:
        return [[]]
    else:
        return sum([insert_everywhere(s[0], t)
                    for t in combinations_with_repetition(s, k - 1)],
                   [])

if __name__ == '__main__':
    from pprint import pprint
    # pprint(sorted_nicely(power_set([1, 2, 3, 4])))
    # print()
    # pprint(sorted_nicely(power_set(['a', 'b', 'c'])))
    # pprint(sorted_nicely(combinations(['a', 'b', 'c', 'd'], 3)))
    # pprint(insert_everywhere('a', ['b', 'c', 'd', 'e']))
    pprint(sorted_nicely(permutations(['a', 'b', 'c', 'd'], 3)))
    #pprint(sorted_nicely(permutations_with_repetition(['a', 'b', 'c', 'd'], 3)))