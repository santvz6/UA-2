from abc import ABC, abstractmethod

class Regressor:
    
    @abstractmethod
    def train(self, X: list[list[float]], y:list[float]) -> None:
        pass

    @abstractmethod
    def predict(x: list[float]) -> float:
        pass
    
