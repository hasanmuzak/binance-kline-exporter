from binance import Client
import datetime
import math
import csv
import os, pathlib
import pandas as pd
import json

client = Client()

def fetch_binance_data(interval: str,
 symbol: str, 
 total_data: int, 
 reverse_data: bool, 
 endTime: int = None, 
 limit: int = 500, 
 export_as_csv: bool = True, 
 export_as_json: bool = False,
 return_as_dataframe: bool = False,
 set_date_as_index: bool = False
 ):
    if total_data < limit:
        limit = total_data
    pre_data = []
    endTime = None

    iterator_number = math.ceil(total_data / limit)
    for i in range(0, iterator_number):
        if not limit == 0 or not limit < 0:
            if not endTime:
                data = client.get_klines(symbol=symbol, interval=interval, limit=limit)
            if endTime:
                data = client.get_klines(symbol=symbol, interval=interval, limit=limit, endTime=endTime)
            if len(data) == 0:
                break
            if data and len(data) > 0:
                endTime = (int(data[0][0] / 1000) - 100) * 1000
            
                for i in data[::-1]:
                    temp_obj = {
                        "Date": str(datetime.datetime.fromtimestamp(int(i[0] / 1000))),
                        "Open": float(i[1]),
                        "High": float(i[2]),
                        "Low": float(i[3]),
                        "Close": float(i[4]),
                        "Volume": float(i[5])
                    }
                    pre_data.append(temp_obj)
                
                total_data = total_data - limit
                if total_data < limit:
                    limit = total_data

    pre_data = pre_data[::-1] if reverse_data else pre_data
    
    if export_as_csv:
        current_path = (pathlib.Path(__file__).parent / "csv").resolve()

        if not os.path.exists(current_path):
            os.makedirs(current_path)
        keys = pre_data[0].keys()
        with open(f"csv/{symbol}-{interval}.csv", "w", newline="") as output:
            dict_writer = csv.DictWriter(output, keys)
            dict_writer.writeheader()
            dict_writer.writerows(pre_data)
    
    if export_as_json:
        current_path = (pathlib.Path(__file__).parent / "json").resolve()

        if not os.path.exists(current_path):
            os.makedirs(current_path)
        
        with open(f"json/{symbol}-{interval}.json", 'w') as f:
            json.dump(pre_data, f, ensure_ascii=False)

    return pd.DataFrame(pre_data) if return_as_dataframe else pre_data