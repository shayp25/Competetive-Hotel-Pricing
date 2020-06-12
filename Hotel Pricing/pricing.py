import requests
from datetime import datetime,timedelta
import pandas as pd


def cost(hotel_key):
    url = "https://data.xotelo.com/api/rates?hotel_key="+hotel_key+"&chk_in=" + date.strftime("%Y-%m-%d") + "&chk_out="+((date+timedelta(days=1)).strftime("%Y-%m-%d"))
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
df[date]=" "

for index, row in df.iterrows():
    df.loc[index,date] = cost(row['hotel code'])
    print(row['Hotel'], row['hotel code'],row['date'])

print(df)
df.to_csv("Hotel Pricing/prices.csv", index=False)









