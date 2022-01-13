#!/usr/bin/env python
# coding: utf-8

# # Week 1 Practice

# You will need:
# - Chapter 1 (SQL Cook Book). In this notebook you will be practicing the code provided in the chapter.
# - Download emp.csv and dept.csv from the canvas Week 1 Practice
# 
# ************
# - Step 1-4: You will create a database week1.db
# - Step 5: Practice Chapter 1 code
# - Step 6: Close db connection
# - Step 7: Open db connection using week1.db (you do not need step1-4 aanymore)

# In[1]:


import sqlite3
import pandas as pd


# STEP 1. Create a database named week1. You shsold have a new file week1.db in your local directory.

# In[2]:


conn = sqlite3.connect('week1.db')  
c = conn.cursor()


# STEP 2. Read emp.csv and create a table emp

# In[3]:


read_emp = pd.read_csv(r'emp.csv')
read_emp.to_sql('emp', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'emp' 


# STEP 3. read dept.csv and create a table dept

# In[4]:


read_dept = pd.read_csv(r'dept.csv')
read_dept.to_sql('dept', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'dept' 


# Execution Examples

# SQL statements will be executed with 
# 
# c.execute('''
# SQL code
# ''')

# In[5]:


#Example 1
for row in c.execute('''
select * from emp
'''):
    print(row)


# In[6]:


colnames = c.description
for row in colnames:
    print(row[0])


# To print a table, use fetchall() to collect data and add column names thaht you have selected.

# In[7]:


# Example 2
c.execute('''
select * from emp
''')

df = pd.DataFrame(c.fetchall(), columns=['EMPNO',
'ENAME',
'JOB',
'MGR',
'HIREDATE',
'SAL',
'COMM',
'DEPTNO'])
print(df)


# ### Basics of SQL Queries  
# 
# **SELECT**: Statement used to select rows and columns from a database. 
# 
# **FROM**:  Specifies which table in the database you want to direct your query to.
# 
# **WHERE**: Clause for filtering for specified value(s).
# 
# **GROUP BY**: Aggregating data. Needs to be used in conjunction with SQL aggregating functions like `SUM` and `COUNT`.
# 
# **ORDER BY**: Sorting columns in the database. 
# 
# **JOIN**: Joins are used to combine tables with one another. 
# 
# **UNION**, **INTERSECT/EXCEPT**: Set operations. Unioning in SQL allows one to append tables on top of one another. 

# ### Step 5. Practice Chapter 1

# In[8]:


## Your turn


# ### Step 6. Close the connection

# In[9]:


conn.close()


# ### Step 7. Open connection with your database week1.db

# In[10]:


conn = sqlite3.connect('week1.db')
c = conn.cursor()


# In[11]:


## You can continue working with SQL coding now


# In[ ]:




