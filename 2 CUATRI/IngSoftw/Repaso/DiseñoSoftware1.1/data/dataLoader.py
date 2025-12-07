from .dataSet import DataSet # DataSet es privado
from .util import Util


class DataLoader:
    def __init__(self, separator: str):
        self.separator = separator

    def load_data(self, folder_path:str) -> list[DataSet]:
        #Util.parse_line()
        pass