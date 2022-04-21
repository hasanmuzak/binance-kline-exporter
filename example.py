from helper import fetch_binance_data

'''
Available params can be found here : https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data
'''

data = fetch_binance_data(interval="1h",
 symbol="ETHUSDT", 
 total_data=500, 
 reverse_data=True, 
 endTime=None, 
 limit=1000, 
 export_as_csv=True,
 export_as_json=True,
 return_as_dataframe=True
)

print(data)

'''
example output:
                    Date     Open     High      Low    Close      Volume
0    2022-04-01 06:00:00  3225.93  3250.61  3218.59  3250.29  19171.7963
1    2022-04-01 07:00:00  3250.29  3258.76  3246.75  3247.33  15446.2725
2    2022-04-01 08:00:00  3247.33  3265.82  3242.95  3251.01  12539.2029
3    2022-04-01 09:00:00  3251.01  3265.27  3245.00  3263.33  14058.8521
4    2022-04-01 10:00:00  3263.32  3282.13  3261.49  3279.41  15127.0016
..                   ...      ...      ...      ...      ...         ...
495  2022-04-21 21:00:00  3065.92  3072.73  3055.02  3058.80  16176.8639
496  2022-04-21 22:00:00  3058.79  3068.62  3021.74  3026.23  30136.5605
497  2022-04-21 23:00:00  3026.23  3034.23  2993.72  3001.08  45452.6284
498  2022-04-22 00:00:00  3001.08  3017.04  2998.55  3002.25  18791.0404
499  2022-04-22 01:00:00  3002.25  3012.95  2942.31  2989.65  44608.0636
'''