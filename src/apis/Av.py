from .Connector import Connector

class AV(Connector):
    """
        AV class is used to connect project with Alpha Vantage API
    """
    
    def __init__(self,params={},endpoint="TIME_SERIES_INTRADAY",key=None):
        """
            Initialize AV class with params"
            params: dict (default: {}) - parameters for the API
            KEY: str (default: None) - API key that might be generated from API provider    
            endpoint: str (default: 'TIME_SERIES_INTRADAY') - endpoint for the API
         """
        super().__init__(output="xlsx")
        self.params = params
        self.key = key
        self.API_url = 'https://www.alphavantage.co/query?function=' + endpoint

    @Connector.api_connector
    def send_request(self):
        """
            Send request to the API and returns the response
        """
        return self.request_data(self.API_url, self.params)




    #That's not necesseary
