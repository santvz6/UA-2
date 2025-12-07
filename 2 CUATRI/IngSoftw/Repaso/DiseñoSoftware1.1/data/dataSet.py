class DataSet:
    def __init__(self, provider: str):
        self.provider = provider
        self.data = list(list())

    def __iter__(self):
        pass

    def __len__(self) -> int:
        count = 0
        for row in self.data:
            for item in row:
                count += 1
        return count
    
    def __str__(self) -> str:
        return "Something"
    
    def add_entry(self, entry: list[float]) -> None:
        self.data.append(entry)
    
    def get_features_and_labels() -> tuple[list[list[float]], list[float]]:
        pass
