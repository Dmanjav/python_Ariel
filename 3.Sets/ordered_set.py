
from typing import Generic, TypeVar

T = TypeVar('T')

class OrdeeredSet(Generic[T]):
    
    __data: list[T]
    
    def __init__(self, values: list[T] | None = None) -> None:
        if values is None:
            self.__data = []
        else:
            self.__data = values[::]
        
    def add(self, value: T) -> None:
        if value not in self.__data:
            self.__data.append(value)
            
    def __repr__(self) -> str:
        return f'OrderedSet({self.__data})'
    
    def __len__(self) -> int:
        return len(self.__data)
    
if __name__ == '__main__':
    a: OrdeeredSet[int] = OrdeeredSet()
    a.add(5)
    a.add(7)
    a.add(5)
    print(a)