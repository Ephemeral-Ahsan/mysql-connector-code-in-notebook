#!/usr/bin/env python
# coding: utf-8

# In[22]:


import os
import pandas as pd
import mysql.connector


# In[24]:


connection=mysql.connector.connect(host='localhost',
                                  user='root',
                                  passwd='Ephemeral#4085',
                                  db='sales')


# In[25]:


connection


# In[26]:


sales_tables= pd.read_sql_query('show tables from sales',connection)
sales_tables


# In[27]:


tables= sales_tables['Tables_in_sales']

for table in tables:
    output=pd.read_sql_query('describe {}'.format(table),connection)
    print(table)
    print(output,'\n')


# In[ ]:




