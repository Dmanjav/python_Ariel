#----------------------------------------------------------
# Lab #1: Ordered Set Class
#
# Date: 20-Sep-2023
# Authors:
#           A01747433 Carlos Alberto Sánchez Calderón
#           A01753486 Diego Manjarrez Viveros
#----------------------------------------------------------

from __future__ import annotations
from typing import Generic, TypeVar
from collections.abc import Iterator, Iterable

T = TypeVar('T')
I = TypeVar('I')


class OrderedSet(Generic[T]):

    class __Iterator(Generic[I]):

        __data: list[I]
        __current: int

        def __init__(self, values: list[I]) -> None:
            self.__data = values
            self.__current = 0

        def __iter__(self) -> Iterator[I]:
            return self

        def __next__(self) -> I:
            if self.__current < len(self.__data):
                result = self.__data[self.__current]
                self.__current += 1
                return result
            else:
                raise StopIteration

    __data: list[T]

    def __init__(self, values: Iterable[T] = []) -> None:
        self.__data = []
        for elem in values:
            self.add(elem)

    def add(self, value: T) -> None:
        if value not in self.__data:
            self.__data.append(value)

    def __repr__(self) -> str:
        return f'OrderedSet({"" if len(self) == 0 else self.__data})'

    def __len__(self) -> int:
        return len(self.__data)

    def __contains__(self, value: T) -> bool:
        return value in self.__data

    def __iter__(self) -> Iterator[T]:
        return OrderedSet.__Iterator(self.__data)

    def discard(self, value: T) -> None:
        for (index, elem) in enumerate(self):
            if elem == value:
                del self.__data[index]
                return

    def remove(self, value: T) -> None:
        for (index, elem) in enumerate(self):
            if elem == value:
                del self.__data[index]
                return
        raise KeyError

    def __eq__(self, other: object) -> bool:
        if isinstance(other, OrderedSet) and len(self) == len(other):
            for elem in self:
                if elem not in other:
                    return False
            return True

        else:
            return False

    def __le__(self, other: OrderedSet[T]) -> bool:

        for elem in self:
            if elem not in other:
                return False
        return True

    def __lt__(self, other: OrderedSet[T]) -> bool:

        if len(self) >= len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    def __ge__(self, other: OrderedSet[T]) -> bool:
        return other <= self

    def __gt__(self, other: OrderedSet[T]) -> bool:
        return other < self

    def isdisjoint(self, other: OrderedSet[T]) -> bool:
        for elem in self:
            if elem in other:
                return False
        return True

    def __and__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    def __or__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet(self)
        for elem in other:
            result.add(elem)
        return result

    def __sub__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet(self)
        for elem in other:
            result.discard(elem)
        return result

    def __xor__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        tempA: OrderedSet[T] = self - other
        tempB: OrderedSet[T] = other - self
        return tempA | tempB

    def clear(self) -> None:
        num: int = len(self)
        for x in range(num):
            del self.__data[0]

    def pop(self) -> T:
        if len(self) == 0:
            raise KeyError
        temp = self.__data[len(self) - 1]
        self.discard(temp)
        return temp


if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet()
    a.add(5)
    a.add(7)
    a.add(5)
    print(f'{a = }')
    print(f'{len(a) = }')
    b: OrderedSet[str] = OrderedSet(['a', 'b', 'c', 'a'])
    print(f'{b = }')
    print(f'{len(b) = }')
    print(f'{5 in a = }')
    print(f'{10 in a = }')
    print(f'{"b" in b = }')
    print(f'{"x" in b = }')

    it = iter([4, 8, 15, 16, 23, 42])
    print(f'{it = }')
    try:
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
        print(f'{next(it) = }')
    except StopIteration:
        print('No more elements to iterate over')

    b_it = iter(b)
    try:
        print(f'{next(b_it) = }')
        print(f'{next(b_it) = }')
        print(f'{next(b_it) = }')
        print(f'{next(b_it) = }')
    except StopIteration:
        print('stop')

    for x in b:
        print(f'{x = }')

    print()

    new_iter = iter(b)
    try:
        while True:
            x = next(new_iter)
            print(f'{x = }')
    except StopIteration:
        ...

    d = OrderedSet(b)
    e = OrderedSet('hello')
    print(f'{d = }')
    print(f'{e = }')
