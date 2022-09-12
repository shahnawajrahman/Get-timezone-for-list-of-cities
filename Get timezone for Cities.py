#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime
from datetime import datetime as dt
from pytz import country_timezones, timezone

#pip install timezonefinder
#pip install geopy

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

print ('imported')


# In[2]:


geolocator = Nominatim(user_agent="geoapiExercises")
my_func = TimezoneFinder().timezone_at


# In[3]:


task = pd.read_excel('Task_ Shah.xlsx')
task


# In[4]:


task['Location'] = task.City + ", " + task.Country
task


# In[5]:


#task = task.head(10)


# In[6]:


locations = task['Location'].unique()
lat = dict(zip(locations, pd.Series(locations).apply(lambda x: geolocator.geocode(x).latitude if geolocator.geocode(x) != None else 'Not Found')))
long = dict(zip(locations, pd.Series(locations).apply(lambda x: geolocator.geocode(x).longitude if geolocator.geocode(x) != None else 'Not Found')))


# In[7]:


task['latitude'] = task['Location'].map(lat)
task['longitude'] = task['Location'].map(long)


# In[8]:


notask = task[(task.longitude == 'Not Found') | (task.latitude == 'Not Found')]
notask['Airport timezone'] = 'Not Found'
notask


# In[9]:


donetask = task[(task.longitude != 'Not Found') & (task.latitude != 'Not Found')]
donetask['Airport timezone'] = donetask.apply(lambda x: my_func(lng=x['longitude'], lat=x['latitude']),axis=1)
donetask


# In[10]:


result = pd.concat([donetask, notask])


# In[11]:


result


# In[12]:


result[['Country', 'City', 'Airport name', 'Airport code (IATA)',
       'Airport timezone']].to_excel('Task_Complete.xlsx',index = False)


# In[ ]:




