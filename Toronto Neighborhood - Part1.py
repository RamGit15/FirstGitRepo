#!/usr/bin/env python
# coding: utf-8

# # Toronto Neighborhood - Clustering
# 
# ## Part 1 - Scrapping the information from Wiki

# In[10]:


get_ipython().system(' pip install requests')
import requests

URL = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
page = requests.get(URL)
page


# In[20]:


page.encoding = 'utf-8' # Optional: requests infers this internally
page.headers


# In[21]:


import requests
from bs4 import BeautifulSoup


# In[155]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[157]:


#print(soup.prettify())
#soup.find(id='bodyContent').prettify()
toronto_list = soup.find_all('table', class_='wikitable')


templist = str(toronto_list).split('\n')
#print(templist)

#Get the heading for the table
header_list = []
for value in templist:
    new_value = str(value)
    if '<th>' in new_value :
        tlist = new_value.split('<th>')
        #print(tlist)
        header_list.append(tlist[-1])
        
print(header_list)


# In[158]:


import pandas as pd
#initialize the dataframe
toronto_df = pd.DataFrame(columns = header_list)
toronto_df


# In[159]:


#Get the items for the table
item_list = []
i = 0
n = 0
for value in templist: 
    new_value = str(value)
    if '<td>' in new_value :
        tlist = new_value.split('<td>')        
        item_list.append(tlist[-1])
        #print(i) 
        
        i=i+1
        if i == 3:
            #print(item_list)
            df_length = len(toronto_df)
            toronto_df.loc[df_length] = item_list
            i = 0
            #print(toronto_df)
            item_list = []
        
toronto_df


# In[160]:


toronto_df1 = toronto_df[toronto_df['Borough']!='Not assigned']
toronto_df1


# In[161]:


toronto_df1.reset_index(drop=True, inplace=True)
toronto_df1.replace(to_replace=r'/', value=',', regex=True)


# In[163]:


toronto_df1.shape

