import apikey
import json
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint 
import matplotlib.pyplot as plt

ts = TimeSeries(key=apikey.API_KEY, output_format="pandas")
data, meta_data = ts.get_intraday(symbol="^GSPC", interval="1min",outputsize="full")

# with open('data.json', 'w+') as outfile:
# 	json.dump(data, outfile)

print data[0::(2*8)]

data["4. close"].plot()
plt.xticks(range(len(data))[0::(2*8)])
plt.title('Intraday Times Series for the S&P500 (1 min intervals)')
plt.show()