from .regressor import Regressor
from data import DataLoader


class Predictor:
    AVERAGE = "AVERAGE"
    LINEAR = "LINEAR"

    def __init__(self, folder_path:str, regressor_type: str):
        self.regressor_type = regressor_type

        dataLoader = DataLoader()
        self.datasets = dataLoader.load_data(folder_path)

        if regressor_type == Predictor.AVERAGE:
            self.regressors = [Re]

    
