import json 
import requests
import pandas as pd
from typing import Dict,Callable, Any, Optional
from functools import wraps
class Connector:
    

    def __init__(self,output):
        self.output = output 

    def request_data(self, url: str, params: Optional[Dict[str, Any]] = None) -> Any:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def save_to_file(self, data: Any, filename: str) -> None:
        return data


    def api_connector(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            data = func(self, *args, **kwargs)
            filename = f"output.{self.output}"
            self.save_to_file(data, filename)
            return data
        return wrapper