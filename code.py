# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)
data.rename(columns = {'Total' : 'Total_Medals'}, inplace = True)
data.head(10)

# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer',np.where(data['Total_Summer'] < data['Total_Winter'],'Winter','Both'))
better_event = data['Better_Event'].value_counts().index.values[0]
print(better_event)
# Top 10
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries.head(-1)

def top_ten(df,col):
    '''
    This function returns a list of top 10 countries based on parameters in the column provided

    Input : 
    df - Dataframe
    col - Parameter column

    return :
    country_list - list of top 10 countries
    '''
    country_list = []
    df_top_10 = df.nlargest(10,col)
    country_list = list(df_top_10['Country_Name'])

    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common = [i for i in top_10_summer if (i in top_10_winter and i in top_10)]

# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(x = 'Country_Name',y = 'Total_Summer',kind = 'bar')
plt.title('Top 10 in Summer Olympics')
plt.xlabel('Country Name')
plt.ylabel('Total Medals in Summer Olympics')
plt.show()
winter_df.plot(x = 'Country_Name',y = 'Total_Winter',kind = 'bar')
plt.title('Top 10 in Winter Olympics')
plt.xlabel('Country Name')
plt.ylabel('Total Medals in Winter Olympics')
plt.show()
top_df.plot(x = 'Country_Name',y = 'Total_Medals', kind = 'bar')
plt.title('Top 10 combined')
plt.xlabel('Country Name')
plt.ylabel('Total Medals in Olympics')
plt.show()

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']


print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

print(top_country_gold)
# Best in the world 
data_1 = data.head(-1)
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

# Plotting the best
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked = 'True')
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)
plt.show()



