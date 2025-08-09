#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv('medical_examination.csv')
df


# In[21]:


#Add an overweight column to the data. 
#To determine if a person is overweight,
#first calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
#If that value is > 25 then the person is overweight.
#Use the value 0 for NOT overweight and the value 1 for overweight.
df['BMI']=(df['weight']/(df['height']/100)**2)
#df
df['overweight']=(df['BMI']).apply(lambda x: '1' if x > 25 else '0')
df


# In[23]:


#Normalize data by making 0 always good and 1 always bad.
#If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol']=df['cholesterol'].apply(lambda x: '1' if x>1 else '0')
df['gluc']=df['gluc'].apply(lambda x: '1' if x>1 else '0')
df


# In[38]:


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt`
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )

    # Group and reformat data to split it by cardio and show counts
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draw the catplot
    fig = sns.catplot(
        x="variable", y="total", hue="value", col="cardio",
        data=df_cat, kind="bar"
    ).fig

    return fig


# --------------------------
# Function to draw heat map
# --------------------------
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, cmap="coolwarm")

    return fig


# In[39]:


draw_cat_plot()


# In[40]:


draw_heat_map()

