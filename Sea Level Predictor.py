#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


df=pd.read_csv('epa-sea-level.csv')
df


# In[12]:


x_values = df['Year']
y_values = df['CSIRO Adjusted Sea Level']


# In[10]:


plt.scatter(x_values, y_values)


# In[15]:


from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)
# Extend x values to 2050
years_extended = pd.Series(range(df["Year"].min(), 2051))
line_fit = intercept + slope * years_extended

# Plot line of best fit
plt.plot(years_extended, line_fit, 'r', label="Line of Best Fit")

# Labels & Title
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()


# In[16]:


df_recent = df[df["Year"] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
years_recent = pd.Series(range(2000, 2051))
line_fit_recent = intercept_recent + slope_recent * years_recent
plt.plot(years_recent, line_fit_recent, 'g', label="From 2000 Fit")

# Labels & Title
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()

