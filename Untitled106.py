#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Q1. Load the flight price dataset and examine its dimensions. How many rows and columns does the
dataset have?"""


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_excel('flight_price.xlsx')
df.head(2)
    


# In[3]:


df.info()


# In[4]:


df.columns


# In[5]:


df.shape  ## 10683 rows and 11 columns


# In[6]:


df.describe() ## here only price column is numerical feature here


# In[19]:


"""Q2. What is the distribution of flight prices in the dataset? Create a histogram to visualize the
distribution."""


# In[7]:


df.describe()


# In[8]:


## plotting hist plot for the price column
plt.hist(x='Price',bins=30,color='g')
plt.xlabel('Flight Prices')
plt.ylabel('Frequency')
plt.title('Distribution of Flight Prices')
plt.show()
plt.show()


# In[31]:


"""Q3. What is the range of prices in the dataset? What is the minimum and maximum price?"""


# In[9]:


df['Price'].max()


# In[10]:


df['Price'].min()


# In[36]:


df.describe()


# In[37]:


"""Q4. How does the price of flights vary by airline? Create a boxplot to compare the prices of different
airlines."""


# In[39]:


##first we have to make airline as numerical category by using one hot incoding
df.head(2)


# In[27]:


from sklearn.preprocessing import OneHotEncoder


# In[30]:


##creating instance
encoder = OneHotEncoder()
encoder.fit_transform(df[['Airline','Source','Destination']]).toarray()


# In[33]:


pd.DataFrame(encoder.fit_transform(df[['Airline','Source','Destination']]).toarray().astype(int),columns=encoder.get_feature_names_out())


# In[35]:


df.info()


# In[30]:


airline_feature_names = encoder.get_feature_names_out(['Airline'])


# In[31]:


airline_feature_names


# In[36]:


encoded_df = pd.DataFrame(encoded_Airline, columns=airline_feature_names)

# Concatenate the encoded DataFrame with the original DataFrame
df_encoded = pd.concat([df, encoded_df], axis=1)

# Drop the original 'Airline' column if needed
df_encoded.drop(['Airline'], axis=1, inplace=True)


# In[39]:


df.head(2)


# In[40]:


## plotting fifure
plt.figure(figsize=(10,6))
sns.boxplot(data=df,x='Price',y='Airline',color='g')
plt.show()


# In[41]:


"""Q5. Are there any outliers in the dataset? Identify any potential outliers using a boxplot and describe how
they may impact your analysis."""


# In[43]:


df.isnull().sum() # we can use mode to handle outliers 


# In[44]:


df['Total_Stops'].unique()


# In[48]:


df.drop('Route',axis=1,inplace=True)


# In[49]:


df.head(2)


# In[50]:


##ploting boxplot fro  the price and see which one is the outliers
plt.figure(figsize=(8,6))
sns.boxplot(x=df['Price'],color='r')
plt.show()


# In[51]:


"""here 80,000 is the outlier Impact on Analysis:

Outliers can potentially have a significant impact on your analysis. They might skew summary statistics like the mean and standard deviation, leading to misleading conclusions. It's important to consider whether these outliers represent genuine data points or if they are errors or anomalies that need to be addressed."""


# In[52]:


"""Q6. You are working for a travel agency, and your boss has asked you to analyze the Flight Price dataset
to identify the peak travel season. What features would you analyze to identify the peak season, and how
would you present your findings to your boss?"""


# In[4]:


##rest our index to seperate day,date &year

df['day'] = df['Date_of_Journey'].str.split('/').str[0]
df['month'] = df['Date_of_Journey'].str.split('/').str[1]
df['year'] = df['Date_of_Journey'].str.split('/').str[2]


# In[8]:


df['day'].astype(int)
df['month'].astype(int)
df['year'].astype(int)


# In[7]:


df.head(2)


# In[9]:


df.tail(2)


# In[12]:


plt.figure(figsize=(8,4))
sns.barplot(data=df,x='month',y='Price',color='r')
plt.show()


# In[15]:


plt.figure(figsize=(8,6))
custom_palette = ['blue', 'green', 'red', 'purple', 'orange']


sns.set_palette(custom_palette)

sns.scatterplot(data=df,x='month',y='Price')
plt.title('peak travel season')
plt.xlabel('month')
plt.ylabel('Price')
plt.show()


# In[16]:


"""observation :
    on 3rd month most of the flight prices are inflated and 6th and 4th month have the same inflated price and copareteply low price when compared to month 3rd"""


# In[18]:


pivot_df = df.pivot_table(index='month', columns='day', values='Price', aggfunc='mean')
plt.figure(figsize=(10,8))
sns.heatmap(pivot_df,cmap='YlGnBu')
plt.title('Price by Month and Day')
plt.xlabel('Day')
plt.ylabel('Month')
plt.show()


# In[19]:


"""Q7. You are a data analyst for a flight booking website, and you have been asked to analyze the Flight
Price dataset to identify any trends in flight prices. What features would you analyze to identify these
trends, and what visualizations would you use to present your findings to your team?"""


# In[20]:


df.head(2)


# In[21]:


pivot_df = df.pivot_table(index='month', columns='day', values='Price', aggfunc='mean')
plt.figure(figsize=(8,6))
sns.heatmap(pivot_df,cmap='plasma')
plt.title('Price by Month and Day')
plt.xlabel('Day')
plt.ylabel('Month')
plt.show()


# In[22]:


"""observation/finding:1: in the 3rd month (march)and day 1st & 3rd is most inflated from this data set.
2:in month 4th(april) from 3rd to 27th day the price is lowest and affordable for many people
3:majority os the price in 3rd month is above 10,000k
4:on the 6th month(june)between 17th to 23rd the price is 6000k
5:in 5th month(may)price is  batwenn 10000k to 6000k"""


# In[23]:


"""Q8. You are a data scientist working for an airline company, and you have been asked to analyze the
Flight Price dataset to identify the factors that affect flight prices. What features would you analyze to
identify these factors, and how would you present your findings to the management team?"""


# In[37]:


df['Source'].unique()


# In[36]:


df['Destination'].unique()


# In[38]:


pivot_df = df.pivot_table(index='Source', columns='Destination', values='Price', aggfunc='mean')
plt.figure(figsize=(10,8))
sns.heatmap(pivot_df,cmap='Set1')
plt.title('price vs source nad destination')
plt.xlabel('destination')
plt.ylabel('source')
plt.show()


# In[41]:


"""observation : 
    1: the most expensive flight is from bagalore to delhi in march month 
    2:the most chepest flight is from mumbai to hyderabad 
    3:cochin to delhi flight is also expensive"""


# In[39]:


pivot_df = df.pivot_table(index='month', columns='day', values='Price', aggfunc='mean')
plt.figure(figsize=(10,8))
sns.heatmap(pivot_df,cmap='Set1')
plt.title('Price by Month and Day')
plt.xlabel('Day')
plt.ylabel('Month')
plt.show()


# In[ ]:





# In[ ]:





# In[40]:


"""observation/finding:1: in the 3rd month (march)and day 1st & 3rd is most inflated from this data set.
2:in month 4th(april) from 3rd to 27th day the price is lowest and affordable for many people
3:majority os the price in 3rd month is above 10,000k
4:on the 6th month(june)between 17th to 23rd the price is 6000k
5:in 5th month(may)price is  batwenn 10000k to 6000k"""


# In[ ]:




