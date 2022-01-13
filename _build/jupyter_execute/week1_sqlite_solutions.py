#!/usr/bin/env python
# coding: utf-8

# ## Solutions

# You will need:
# - Chapter 1 (SQL Cook Book). In this notebook you will be practicing the code provided in the chapter.
# - Download emp.csv and dept.csv
#     - [emp.csv](_static/emp.csv)
#     - [dept.csv](_static/dept.csv)
# 
# ************
# - Step 1-4: You will create a database week1.db
# - Step 5: Practice Chapter 1 code
# - Step 6: Close db connection
# - Step 7: Open db connection using week1.db (you do not need step1-4 anymore)

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


# In[12]:


for row in c.execute('''select * from emp'''):
    print(row)


# In[13]:


for row in c.execute('''select * from emp where deptno=10'''):
    print(row)


# In[14]:


for row in c.execute('''select * from emp where (deptno=10 
or comm is not null
or sal <= 2000) and deptno=20'''):
    print(row)


# ##### Return specific colulmns

# In[15]:


for row in c.execute('''SELECT ename, deptno, sal from emp'''):
    print(row)


# ##### To change the names of the columns using AS keyword. This is known as aliasing. 

# In[16]:


c.execute('''SELECT sal AS salary, comm AS commission FROM emp''')
#     column_name = c.description
#     for cname in column_name:
#         print(cname)
df = pd.DataFrame(c.fetchall(), columns=['SALARY', 'COMMISSION'])    
print(df)


# ##### Problems with referencing the aliased columns in WHERE clause, the WHERE clause gets executed before the SELECT;Thus, the new aliases do not yet exist when the query's WHERE clause is evaluated. The solution is to wrap your query as an inline view. Use fetchall() to collect data

# In[17]:


c.execute('''SELECT * from(SELECT sal AS salary, comm AS commision FROM emp) WHERE salary < 5000''')
df = pd.DataFrame(c.fetchall(), columns=['SALARY', 'COMMISSION'])
print(df)


# ##### Concatenating the coulmn values. The usage is dependent on the DBs. For the DB2, Oracle, PostgreSQl, uses the vertical bars.

# In[18]:


c.execute('''SELECT ename||' WORKS AS A '||job AS msg FROM emp WHERE deptno=10''')
df = pd.DataFrame(c.fetchall())
print(df)


# - MySQL supports a function called CONCAT (sqlite doesn't support CONCAT())
#   - c.execute('''SELECT concat(ename, 'WORKS AS A ',job) AS msg FROM emp WHERE deptno=10''') df = pd.DataFrame(c.fetchall()) print(df)
# - SQL server, Uses the + operator for concatenation.
#   - c.execute('''SELECT ename + ' WORKS AS A ' + job AS msg FROM emp WHERE deptno=10''') df = pd.DataFrame(c.fetchall()) print(df)

# ##### Using conditional logic in a SELECT statement. Use CASE expression to perform conditional logic directly in your SELECT statement

# In[19]:


c.execute('''SELECT ename,sal, CASE when sal <= 2000 then 'UNDERPAID' when sal >= 4000 then 'overpaid' else 'OK' end as status from emp''')
df = pd.DataFrame(c.fetchall(), columns=['ename', 'salary', 'status'])
print(df)


# - The CASE expression allows to perform condition logic on values returned by a query. Also, you can alias the result of the CASE expression. In the above example CASE is aliased as status

# ##### Limit the number of rows returned.
# - Using DB2
#   - c.execute('''SELECT * FROM emp fetch 5 rows only''')

# In[20]:


c.execute('''SELECT * FROM emp limit 5''')
df = pd.DataFrame(c.fetchall())
print(df)


# ##### Returning a random record from a table. Use built-in RANDOM function in conjuction with LIMT and ORDER BY

# In[21]:


c.execute('''SELECT ename,job FROM emp ORDER BY RANDOM() LIMIT 5''')
df = pd.DataFrame(c.fetchall(), columns=['ename','job'])
print(df)


# ##### Finding Null Values. Determine whether the value is null, using IS NULL.

# In[22]:


c.execute('''SELECT * FROM emp WHERE comm IS NULL''')
df = pd.DataFrame(c.fetchall())
print(df)


# - Transforming Null into real values, Use the function COALESCE to sunstitute real values for nulls

# In[23]:


c.execute('''SELECT COALESCE(comm,0) FROM emp''')
df = pd.DataFrame(c.fetchall())
print(df)


# - You can also use the CASE to values

# In[24]:


c.execute('''SELECT CASE
                    WHEN comm IS NOT NULL THEN comm
                    ELSE 0
                    END
            FROM emp''')
df = pd.DataFrame(c.fetchall())
print(df)


# ##### Seraching for a pattern, use the LIKE operator in conjunction with the SQL wildcard operator (%)

# In[25]:


c.execute('''SELECT ename, job FROM emp WHERE deptno in (10, 20) AND (ename LIKE '%I%' OR job LIKE '%ER')''')
df = pd.DataFrame(c.fetchall(), columns=['ename', 'job'])
print(df)


# #### Convert Jupyter to PDF

# In[26]:


get_ipython().system('wget -nc https://raw.githubusercontent.com/brpy/colab-pdf/master/colab_pdf.py')
from colab_pdf import colab_pdf
colab_pdf('week1-sqlite.ipynb')

