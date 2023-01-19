#!/usr/bin/env python
# coding: utf-8

# In[7]:





# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


filename = 'data/table_i702t60.csv'
df = pd.read_csv('table_i702t60.csv')


# In[5]:


df.head()


# In[6]:


#Checking to make sure we dont have nans in our dataframe
#it is difficult to make plot if we have nans
df.info()


# In[7]:


#lets do a graph month number in X-axis
#Interest paid and principal paid in Y axis
#for doing that we need to do numpy arrays
#We will use lock operator

month_number = df.loc [:,'month'].values
interest_paid = df.loc[:,'interest_paid'].values
principal_paid = df.loc[:,'principal_paid'].values


# In[8]:


month_number


# In[9]:


#The value attribute convert a column of values into a numpy array
type(month_number)


# In[10]:


help(plt.plot)


# In[11]:


plt.plot(month_number,interest_paid) 


# In[12]:


plt.plot(month_number,interest_paid) 
plt.plot(month_number,principal_paid) 


# In[13]:


#For asthetic style of our graphs
plt.style.available


# In[14]:


plt.style.use('classic')
plt.plot(month_number,interest_paid) 
plt.plot(month_number,principal_paid) 


# In[15]:


plt.style.use('Solarize_Light2')
plt.plot(month_number,interest_paid) 
plt.plot(month_number,principal_paid) 


# In[16]:


plt.style.use('fivethirtyeight')
plt.plot(month_number,interest_paid) 
plt.plot(month_number,principal_paid) 


# In[17]:


plt.style.use('ggplot')

plt.plot(month_number,interest_paid) 
plt.plot(month_number,principal_paid) 


# In[19]:


#Matplotlibrary has two different types of syntax

#Matlab-style
#A scripted interface designed to feel like MATLAB whereas 
#Matplotlib maintains a pointer to active figure

#Object oriented syntax
#Used in situations when you want more control over your figure

#IMPORTANT NOTE 
#You can and often will have plots that will be created through a combination of Matlab style and object oriented syntax

#MATLAB STYLE

plt.style.use('seaborn')
plt.plot(month_number, interest_paid, c='k')
plt.plot(month_number, principal_paid,c='b')

Here,The black one is c='k'


# In[20]:


OBJECT oriented syntax
#tuple unpacking 
(x,y) = (3,9)
fig,axes = plt.subplots(nrows = 1,ncols = 1)
axes.plot(month_number, interest_paid, c='k');
axes.plot(month_number, principal_paid,c='b');


# In[26]:


#Combination

fig,axes = plt.subplots(nrows = 1,ncols = 1)
plt.plot(month_number, interest_paid, c='k')
axes.plot(month_number, principal_paid,c='b')


# In[27]:


#Setting titles,tables and limits
#Set xlim and ylim
plt.plot(month_number, interest_paid, c='k')
plt.plot(month_number, principal_paid,c='b')
plt.xlim(left=1,right=70)
plt.ylim(bottom=0,top=1000)

#this isn't the most practical use of ylim


# In[28]:


#SetLABEL

plt.plot(month_number, interest_paid, c='k')
plt.plot(month_number, principal_paid,c='b')
plt.xlabel('month')
plt.ylabel('dollars')


# In[30]:


#setTITLE

plt.plot(month_number, interest_paid, c='k')
plt.plot(month_number, principal_paid,c='b')
plt.xlabel('month')
plt.ylabel('dollars')
plt.title('Interest and principal paid each month')


# In[1]:


sum = 0

 i = 10

 while i < 1: 6


sum

= sum + i sum = sum* 2

i -= 1

print(sum)


# In[4]:


# function returns index of first matching
# element in an array
def first_index_of_element_in_array(element, 
   for i, array_element in enumerate(array):

   #MISSING CODE

  return -1


# In[16]:





# In[17]:


def _(func,items):
    i = 0
    for items in items:
        if func(item):
            items[i] = item
            i +=1
            del items[i:]
            
        


# In[27]:


def _(arr):
    temp = 0
    for x in arr:
        if x % 2 ==1:
            temp += 1
            
        else :
                temp = 0
        if temp == 3:
                return True
            
    return False


# In[ ]:





# In[ ]:




