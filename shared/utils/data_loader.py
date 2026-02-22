import pandas as pd 
import numpy as np 
import os

class CustomDataLoader:
    def __init__(self):
        pass
    
    def _check_file_exists(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")

    def _check_file_type(self, file_path: str, file_type: str) -> bool:
        return file_path.split('.')[-1] == file_type

    def load_csv(self, file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)

    def load_json(self, file_path: str) -> pd.DataFrame:
        return pd.read_json(file_path)
    
    def load_excel(self, file_path: str) -> pd.DataFrame:
        return pd.read_excel(file_path)

    def load_data(self, file_path: str) -> pd.DataFrame:
        self._check_file_exists(file_path)
        file_type = file_path.split('.')[-1]
        if file_type == 'csv':
            return self.load_csv(file_path)
        elif file_type == 'json':
            return self.load_json(file_path)
        elif file_type == 'xlsx':
            return self.load_excel(file_path)
        else:
            raise ValueError(f"File type is not supported: {file_type}")