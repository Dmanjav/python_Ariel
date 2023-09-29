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


def perms(s: list[C], k: int) -> list[list[C]]:
    if k == 0 or len(s) == 0:
        return [[]]
    else:
        r = perms(s, k-1)

        return r + [t + [j] for j in s for t in r]


def permutations_with_repetition(s: list[C], k: int) -> list[list[C]]:
    if len(s) == 0 or k == 0:
        return []
    res = []
    for perm in perms(s, k):
        if len(perm) == k:
            res.append(perm)
    return res


def combinations_with_repetition(s: list[C], k: int) -> list[list[C]]:
    if len(s) == 0 or k == 0:
        return []
    res = []
    for perm in perms(s, k):
        if len(perm) == k and sorted(perm) not in res:
            res.append(sorted(perm))
    return res


if __name__ == '__main__':
    from pprint import pprint
    # permutations_with_repetition([1, 2, 3, 4], 1)
