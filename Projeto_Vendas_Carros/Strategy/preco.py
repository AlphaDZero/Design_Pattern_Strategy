from abc import ABC, abstractmethod

class Interface_Price(ABC):
    
    @abstractmethod
    def valor_final(self, preco):
        raise NotImplementedError