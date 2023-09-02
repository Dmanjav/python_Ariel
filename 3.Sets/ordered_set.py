
from typing import Generic, TypeVar

T = TypeVar('T')
I = TypeVar('I')

class OrderedSet(Generic[T]):
    
    class __Iterator(Generic[I]):
        
        __data: list[I]
        __current: int 
        
        def __init__(self, values: list[I]) -> None:
            self.__data = values
            self.__current = 0
        
        def __iter__(self) -> Iterator:
            return self
        
        def __next__(self) -> I:
            result = self.__data[self.__current]
            self.__current += 1
    
    __data: list[T]
    
    def __init__(self, values: list[T] = []) -> None:
       self.__data = []
       for elem in values:
           self.add(elem)
        
    def add(self, value: T) -> None:
        if value not in self.__data:
            self.__data.append(value)
            
    def __repr__(self) -> str:
        return f'OrderedSet({self.__data})'
    
    def __len__(self) -> int:
        return len(self.__data)
    
    def __contains__(self, value: T) -> bool:
        return value in self.__data
    
if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet()
    a.add(5)
    a.add(7)
    a.add(5)
    print(f'{a = }')
    print(f'{len(a) = }')
    b = OrderedSet(["a", "b", "c", "a"])
    print(b)
    print(f'{len(b) = }')
    print(f'{5 in a = }')
    print(f'{10.2 in a = }')
    
    