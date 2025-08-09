#!/usr/bin/env python
# coding: utf-8

# In[82]:


#How many people of each race are represented in this dataset? 
#This should be a Pandas series with race names as the index labels
import pandas as pd
df=pd.read_csv("adult.data.csv")
df


# In[83]:


s=df['race'].value_counts()
#.reset_index(name='count').rename(columns={'index': 'race'})

s


# In[84]:


#What is the average age of men?
df_men_age=df.groupby('sex')['age'].mean()
df_men_age.loc['Male']


# In[85]:


#What is the percentage of people who have a Bachelor's degree?
df_bach=df['education'].value_counts()
#df_bach
df_bach.loc['Bachelors']
#df_bach.loc('Bachelors')
#df_bach=df_bach.get_index('bachelor\'s')
df_ed_prc=df_bach.loc['Bachelors']/df_bach.sum()
df_ed_prc*100


# In[86]:


#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

list_ed=['Bachelors','Masters','Doctorate']

df_ed=df[df['education'].isin(list_ed)]

df_more50=df_ed[df_ed['salary']=='>50K']

(df_more50.shape[0]/df_ed.shape[0])*100

#df_sal=df.groupby('education')['salary'].count()
#df_sal


# In[89]:


#What percentage of people without advanced education make more than 50K
df_ned=df[~(df['education'].isin(list_ed))]
df_ned
df_ned_more50=df_ned[df_ned['salary']=='>50K']
(df_ned_more50.shape[0]/df_ned.shape[0])*100


# In[91]:


#What is the minimum number of hours a person works per week?
min_hrs_week=df['hours-per-week'].min()
min_hrs_week


# In[107]:


#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
trg=(df[(df['hours-per-week']==min_hrs_week) & (df['salary']=='>50K') ].shape[0])
tot=df[(df['hours-per-week']==min_hrs_week)].shape[0]
perc=(trg/(df[(df['hours-per-week']==min_hrs_week)].shape[0]))*100
perc


# In[126]:


#What country has the highest percentage of people that earn >50K and what is that percentage?
df_country=df[df['salary']=='>50K'].groupby('native-country')['salary'].value_counts()
df_country
#df_country.max()
#df_country.idxmax()[0]
##df_country.sum()
df_country.max()/(df_country.sum())


# In[135]:


#Identify the most popular occupation for those who earn >50K in India.
df_india=df[(df['native-country']=='India') & (df['salary']=='>50K')]
df_india=df_india.groupby('occupation')['salary'].value_counts()
df_india.idxmax()[0]

