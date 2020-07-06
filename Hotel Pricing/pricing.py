import requests
from datetime import datetime,timedelta
import pandas as pd

#new comment
def cost(hotel_key):
    url = "https://data.xotelo.com/api/rates?hotel_key="+hotel_key+"&chk_in=" + dateString + "&chk_out="+((date+timedelta(days=1)).strftime("%Y-%m-%d"))
    res = requests.get(url)

    data = res.json()['result']['rates']
    minCost  = min(data, key=(lambda site: site['rate']))
    minCost = minCost['rate'] +minCost['tax']
    return int(minCost)

    #!use res for testing as res.json
    # with open('Hotel Pricing/res.json') as f:
    #     data = json.load(f)['result']['rates']

date = (datetime.today())
df = pd.read_csv('Hotel Pricing/prices.csv',delimiter=',')
dateString = date.strftime("%Y-%m-%d")
df[dateString]=" "

for index, row in df.iterrows():
    df.loc[index,dateString] = cost(row['hotel code'])
    print(row['Hotel'], row['hotel code'])

print(df)
df.to_csv("Hotel Pricing/prices.csv", index=False)









