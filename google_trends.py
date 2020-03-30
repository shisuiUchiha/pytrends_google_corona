from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='en-US', tz=360)

country_code=['CN','US','IN','IT']
labelling=['china','USA','india','italy']

kw_list = ["corona"]
i=0
for code in country_code:
	pytrends.build_payload(kw_list,cat=0,timeframe='today 3-m',geo=code,gprop='')
	df=pytrends.interest_over_time()
	df=df.reset_index()
	plt.plot(df['date'],df['corona'],label=labelling[i])
	i=i+1
	print(df)
plt.xlabel('Timeline')
plt.ylabel('Corona Google Trends - Normalised')
plt.legend()
plt.show()


#pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='CN', gprop='')
#df_india_time.reset_index().plot(x='date',y='corona',figsize=(120, 10),kind ='line')

#plt.show()
