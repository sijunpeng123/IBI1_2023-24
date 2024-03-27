import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir (r'C:\Users\14125\Desktop\work\IBI\IBI1_23-24\IBI1_2023-24\practical7')
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
dalys_data.iloc[0:99:10,:]
#This is the code for showing the fourth column (the DALYs) from every 10th row, starting from the rst row, for the rst 100 rows (inclusive).
data_afghanistan=dalys_data['Entity'] == 'Afghanistan'
dalys_data.loc[data_afghanistan,'DALYs']
#Using a Boolean to show DALYs for all rows corresponding to Afghanistan.
china_data=dalys_data.loc[dalys_data['Entity'] == 'China']
china_data.loc[:,'DALYs']
np.mean(china_data.loc[:,'DALYs'])
#Computing the mean DALYs in China which is 30677.694333333337,
china_data.loc[china_data['Year'] ==2019]
# DALYs here is22270.51, the mean is bigger.
plt.plot(china_data['Year'], china_data['DALYs'], 'b+')
plt.show()
plt.clf
#Creating a plot showing the DALYS over time in China.
data_2019=dalys_data.loc[dalys_data['Year']==2019]
plt.figure(figsize=(80,6))
plt.bar(data_2019['Entity'].tolist(),data_2019['DALYs'].tolist())
plt.xlabel('Entity')
plt.ylabel('DALYs')
plt.xticks(rotation=90)
plt.xticks(fontsize=5)
plt.show()