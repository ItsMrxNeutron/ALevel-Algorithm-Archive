
from abc import ABC, abstractmethod



class Graph(ABC):
    
    # enforce string representation
    @abstractmethod
    def __str__(self):
        ...

