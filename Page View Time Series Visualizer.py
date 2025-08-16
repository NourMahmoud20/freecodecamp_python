#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


df=pd.read_csv('fcc-forum-pageviews.csv')
df=df.set_index('date')
df


# In[17]:


#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
# Calculate lower and upper bounds

lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

df=df[(df['value']>lower_bound) & (df['value']<upper_bound)]
df


# In[28]:


#Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png".
#The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019.
#The label on the x axis should be Date and the label on the y axis should be Page Views.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Ensure index is datetime
df.index = pd.to_datetime(df.index)

# Filter date range
mask = (df.index >= '2016-05-01') & (df.index <= '2019-12-31')
df_daily = df.loc[mask]

# Prepare X and Y
x = df_daily.index
y = df_daily['value']

# Plot
plt.figure(figsize=(12, 6))
plt.plot(x, y, color='red', linewidth=1)

# Labels and title
plt.xlabel("Date")
plt.ylabel("Page Views")
plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

# Rotate date labels for readability
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# In[30]:


#Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png".
#It should show average daily page views for each month grouped by year. 
#The legend should show month labels and have a title of Months.
#On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
def year_month(date):
    datetime=pd.to_datetime(date)
    month = datetime.month
    year = datetime.year
    return f'{month}-{year}'






# In[37]:


df_daily['date']=df_daily.index
df_daily['month-year']=df_daily['date'].apply(year_month)


# In[31]:


print(year_month('2025-04-03'))


# In[38]:


df_daily


# In[51]:



df_daily['month-year']=pd.to_datetime(df_daily['month-year'])
df_month_year=df_daily.groupby('month-year')['value'].mean()
df_month_year=df_month_year.to_frame().sort_values(by='month-year')
df_month_year


# In[55]:


import calendar
# Extract year and month
df_month_year['year'] = df_month_year.index.year
df_month_year['month'] = df_month_year.index.month

# Pivot for plotting
df_pivot = df_month_year.pivot(index='year', columns='month', values='value')

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
df_pivot.plot(kind='bar', ax=ax)

# Labels
ax.set_xlabel('Years')
ax.set_ylabel('Average Page Views')

# Legend with month names
month_names = [calendar.month_name[m] for m in df_pivot.columns]
handles, _ = ax.get_legend_handles_labels()
ax.legend(handles=handles, labels=month_names, title='Months')

fig.tight_layout()
fig.savefig('bar_plot.png')


# In[60]:


def draw_box_plot():
    import matplotlib.pyplot as plt
    import seaborn as sns

       # Copy data for plotting
    df_box = df_daily.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month

    # Set up figure
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].set_xticklabels(
        ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    )

    plt.tight_layout()
    return fig


# In[61]:


draw_box_plot()
plt.show()

