import random

class Market:

    def __init__(self, name, period, duration):
        """
        Constructor for Market class
        The market class contains all the data for the market for a particular stock such as OHLC data, volume, etc., for a given period of time.
        name: Name of the stock
        period: List of periods for which the data is to be generated (e.g., ['1min', '5min', '15min', '30min', '1hr', '1day'])
        duration (int): Duration in months for which the data is to be generated (e.g., 1, 3, 6, 12)
        """
        self.name = name
        self.period = period if isinstance(period, list) else [period]
        self.duration = duration

    def generate_market_data(self):
        """
        Generates market data for all specified periods and durations.
        Returns:
            dict: A dictionary containing market data for each period.
        """
        return {p: self.__generate_period_data() for p in self.period}

    def __generate_period_data(self):
        return {d: self.__generate_duration_data() for d in range(1, self.duration + 1)}

    def __generate_duration_data(self):
        """
        Generates data for a specific duration.
        Returns:
            dict: A dictionary containing OHLC data.
        """
        return {i: self.__generate_ohlc_data() for i in range(3)}

    def __generate_ohlc_data(self):
        """
        Generates OHLC data with random variations.
        Returns:
            dict: A dictionary containing OHLC and volume data.
        """
        return {
            'open': round(100 * (1 + random.uniform(-0.01, 0.01)), 2),
            'high': round(105 * (1 + random.uniform(-0.01, 0.01)), 2),
            'low': round(95 * (1 + random.uniform(-0.01, 0.01)), 2),
            'close': round(100 * (1 + random.uniform(-0.01, 0.01)), 2),
            'volume': int(100000 * (1 + random.uniform(-0.01, 0.01)))
        }