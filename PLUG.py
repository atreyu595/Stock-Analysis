# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:53:25 2021
@author: Atreyu Jasper Laxa Cortez

Technical Analysis of Plug Power Inc. 

Question: Is Plug Power still a buy after recent drops in prices? 

Business Fundamentals: Very Good
 - Recent partnership with SK group, 10% stake in company (1.5 Billion USD), 
 Hydorgen power expansion in Asia
 - Joint Venture with Renault to expand Hydorgen-powered vehicles and energy
 into Europe.
 - Recent joint venture with Acciona for expansion in Iberian Peninsula 
 - Use of Hydrogen-powered vehicles in distribution and mobility-movement vehicles
 in Walmart and Amazon warehouses
 - Speculation on Hydrogen-powered generators to power Microsoft and Amazon 
 Data centres 
 - 100+ Hydrogen Fueling Stations worldwide
 - South Korea plans to have 450 refueling stations by 2025 using Plug products
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

data = pd.read_csv('PLUG.csv')

print(data.head(15))

dataAdj = pd.DataFrame()
dataAdj['Adjusted Close Price'] = data['Adj Close']
plt.figure(figsize = (12.5, 4.5))
plt.plot(dataAdj['Adjusted Close Price'])
plt.xlabel('Adjusted Close Price ($USD)', fontsize = 20)
plt.ylabel('19-12-2019 to 19-2-2021', fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.title('Adjusted Close Price History $PLUG', fontsize = '30')

data['SMA30'] = data['Adj Close'].rolling(20).mean()
plt.figure(figsize = (12.5, 4.5))
print(data['SMA30'])
dataAdj['SMA30'] = data['SMA30']
plt.plot(data['SMA30'])

plt.figure(figsize = (12.5, 4.5))
dataAdj['SMA50'] = data['Adj Close'].rolling(50).mean()
plt.plot(dataAdj['SMA50'])

plt.figure(figsize = (12.5, 4.5))
plt.plot(dataAdj['Adjusted Close Price'])
plt.plot(data['SMA30'])
plt.plot(dataAdj['SMA50'])
plt.ylabel('Adjusted Close Price ($USD)', fontsize = 20)
plt.xlabel('19-12-2019 to 19-2-2021', fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.title('Adjusted Close Price History $PLUG', fontsize = '30')

def buySellSig(data):
    buySigPrice = []
    sellSigPrice = []
    flag = -1
    
    for i in range(len(dataAdj['Adjusted Close Price'])):
        if dataAdj['SMA30'][i] > dataAdj['SMA50'][i]:
            if flag != 1:
                buySigPrice.append(dataAdj['Adjusted Close Price'][i])
                sellSigPrice.append(np.nan)
                flag = 1
            else:
                buySigPrice.append(np.nan)
                sellSigPrice.append(np.nan)
        elif dataAdj['SMA30'][i] < dataAdj['SMA50'][i]:
            if flag != 0:
                buySigPrice.append(np.nan)
                sellSigPrice.append(dataAdj['Adjusted Close Price'][i])
                flag = 0
            else:
                buySigPrice.append(np.nan)
                sellSigPrice.append(np.nan)
        else:
             buySigPrice.append(np.nan)
             sellSigPrice.append(np.nan)
    return (buySigPrice, sellSigPrice)

buy_sell = buySellSig(dataAdj)
dataAdj['buySig'] = buy_sell[0]
dataAdj['sellSig'] = buy_sell[1]

print(dataAdj)

plt.figure(figsize = (12.5, 12.5))
plt.plot(dataAdj['Adjusted Close Price'])
plt.plot(dataAdj['SMA30'], alpha = 0.35)
plt.plot(dataAdj['SMA50'], alpha = 0.35)
plt.scatter(dataAdj.index, dataAdj['buySig'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(dataAdj.index, dataAdj['sellSig'],label = 'Sell', marker = 'v', color = 'red')
            
"""
Analysis: 
-Recent drwabacks and corrections in price have stemmed from Texas power outages.
-Also, with Norway planning to build the first Hydrogen-producing "Gigafactory",
many investor fears begin to speculate whether Plug products would still be requested 
and ordered in Europe (major market since EU is planning to shift to Green)
-50 to 100 SMA remain as support indicators during it's 1000% increase in price
since last year, indicating large volumes of buying than selling
-After market close (20th Feb 2021), Plug has finished Green, up 11.27% from previous close
-Recent analysis shows huge Buying opportunity in Plug at a discounted price of $10!!!
-Nothing has changed fundementally in their business
-Speculation of market manipulation by the big boys of Wall Street?
-Overall, the Fuel Cell sector was hit hard especially Plug due to Norway News,
other Fuel Cell Companies such as Bloom Energy and FuelCell Energy went down after their
meteroic rise in recent months due the Biden Administration promising a renewable energy shift.
Due to Plug having better business fundaementals than FCEL and BE, many investors begin to 
speculate whether its time to invest in other sectors of the renewable energy market i.e. PLUG POWER

Judgement: Plug at this point in time is still a buy, the future looks bright for this company,
with a market cap of 27 Billion USD, it's hard to see such huge sell offs, and with recent partnerships
with Acciona, should've been a "Green" week in the market. The price as of today (20th Feb 2021) is at $55.89,
up 11.27% from Thursday, but still at a discount. 

BUY BUY BUY!!!
"""