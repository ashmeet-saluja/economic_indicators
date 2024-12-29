#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load your dataset
data = pd.read_csv('economic_indicators_dataset_2010_2023.csv')

# Display the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Check data types
print(data.info())


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('economic_indicators_dataset_2010_2023.csv')

# Preview the dataset
print(data.head())

# Check for null values and basic info
print(data.info())
print(data.isnull().sum())


# In[4]:


# Plot time series for each indicator
plt.figure(figsize=(12, 6))

# Plotting Inflation, GDP Growth, and Unemployment Rates
plt.plot(data['Date'], data['Inflation Rate (%)'], label='Inflation Rate (%)')
plt.plot(data['Date'], data['GDP Growth Rate (%)'], label='GDP Growth Rate (%)')
plt.plot(data['Date'], data['Unemployment Rate (%)'], label='Unemployment Rate (%)')

# Customize the plot
plt.title('Macroeconomic Indicators Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()



# In[5]:


# Filter for a specific country (e.g., USA)
usa_data = data[data['Country'] == 'USA']

# Plot GDP Growth and Stock Index for USA
plt.figure(figsize=(12, 6))
plt.plot(usa_data['Date'], usa_data['GDP Growth Rate (%)'], label='GDP Growth Rate (%)')
plt.plot(usa_data['Date'], usa_data['Stock Index Value'], label='Stock Index Value')

# Customize the plot
plt.title('USA: GDP Growth vs Stock Index', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()


# In[6]:


# Compute correlation matrix
correlation_matrix = data[['Inflation Rate (%)', 'GDP Growth Rate (%)',
                           'Unemployment Rate (%)', 'Interest Rate (%)',
                           'Stock Index Value']].corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# Customize the plot
plt.title('Correlation Matrix of Macroeconomic Indicators', fontsize=16)
plt.show()


# In[7]:


# Select relevant columns for pairplot
columns_to_plot = ['Inflation Rate (%)', 'GDP Growth Rate (%)',
                   'Unemployment Rate (%)', 'Stock Index Value']

sns.pairplot(data[columns_to_plot], diag_kind='kde', kind='scatter', markers='o')

# Show the plot
plt.show()


# In[ ]:




