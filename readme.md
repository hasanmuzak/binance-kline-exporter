# What is this repository for?
This repository includes a piece of code that helps to fetch kline/candlestick data from Binance API as a pandas dataframe, CSV or JSON.
https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

It can be useful with libraries such as pandas_ta for technical analysis.

## Why Binance API instead of Yfinance?
Because Binance has an official API service, more request limit and more flexible data. Binance API might be more useful if you are collecting data for Machine Learning.

## Parameters

 - interval: String (1m, 5m, 15m, 30m, 1h...)
 - symbol: String (BTCUSDT, ETHUSDT...)
 - total_data: int (How many records would you want to have... Ex: 100000)
 - reverse_data: bool (To order by date)
 - endTime: LONG (Ex: 1650586105000)
 - limit: int (Limit parameter to send request to API. Default is 500)
 - export_as_csv: bool (Default: True)
 - export_as_json: bool (Default: False)
 - return_as_dataframe: bool (Default: False)