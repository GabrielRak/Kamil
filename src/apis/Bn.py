from .Connector import Connector
import pandas as pd
class BN(Connector):
    """
        BN class is used to connect project with Binance API
    """


    def __init__(self,params={},key=None):
        """
            Initialize BN class with params"
            params: dict (default: {}) - parameters for the API
            KEY: str (default: None) - API key that might be generated from API provider    
            endpoint: str (default: 'ping') - endpoint for the API
         """
        super().__init__(output="xlsx")
        self.params = params
        self.key = key
        self.API_url = 'https://api.binance.com/api/v3/'

    @Connector.api_connector
    def send_request(self,endpoint):
        """
            Send request to the API and returns the response
        """
        if endpoint == 'klines': return self._transform_klines(self.request_data(self.API_url + endpoint, self.params))
        else: return self.request_data(self.API_url + endpoint, self.params)
    

    def _transform_klines(self,data):
        """
            Transform klines data, inot pandas DataFrame to make it easier
            to save it to xlsx file
        """
        df = pd.DataFrame(data)
        df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore']
        