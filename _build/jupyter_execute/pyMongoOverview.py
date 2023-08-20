#!/usr/bin/env python
# coding: utf-8

# # Mongo DB Cluster
# 
# Adapted from Workshop: https://github.com/geoffswc/MongoDB-Python-Workshop

# ## Section 1: Covid-19 Data Johns Hopkins Overview
# 
# This notebook section  will demo how to connect to remote client and work with mongoDB database.

# ### Modules

# In[1]:


#!pip install pymongo
#!pip install dnspython


# In[2]:


import pymongo
from pymongo import MongoClient


# ### Connect to the MongoDB server
# 
# Connect to the published URL for the Johns Hopkins covid-19 dataset hosted on Atlas.

# In[3]:


mongodb_url = "mongodb+srv://readonly:readonly@covid-19.hip2i.mongodb.net/covid19"
client = MongoClient(mongodb_url)


# ### List the databases and collections
# 
# Now that we have a connection to the server, we can
# 
# 1. list the available databases
# 2. select a database
# 3. list the available collections within that database
# 4. select a collection to query

# #### List the available databases

# In[4]:


client.list_database_names()


# #### Select a database

# In[5]:


covid19_db = client.get_database("covid19")


# In[6]:


type(covid19_db)


# #### List database collections

# In[7]:


covid19_db.list_collection_names()


# #### Select Collection

# In[8]:


countries_summary_cl = covid19_db['countries_summary']


# In[9]:


countries_summary_cl


# ### Queries

# #### Single Record Query
# 
# To inspect just one record from the countries_summary collection, we can use the `find_one()` command.

# In[10]:


countries_summary_cl.find_one()


# #### Multiple Record Query
# 
# To find multiple records, you can use the `find()` command along with the limit() method

# In[11]:


for r in countries_summary_cl.find().limit(5):
    print(r['country'], r['confirmed'])
    print(r)


# ### Counting all documents in a collection

# In[12]:


countries_summary_cl.count_documents({})


# ### Projecting
# 
# The next two cells show examples of choosing which fields to display. By default, all values in the records returned from a query will display. To limit the number of them that are displayed, specify fields names.
# 
# Note that once you specify a field to return, only those fields you project will be included in the results. The exception is the "\_id" field, which will project by default unless you suppress it. 

# In[13]:


for r in countries_summary_cl.find({},{'country':1, 'confirmed': 1}).limit(10):
    print(r)


# In[14]:


for r in countries_summary_cl.find({},{'_id': 0, 'country': 1, 'confirmed': 1}).limit(10):
    print(r)


# ### Filtering
# 
# The next cells will query based on a
# 
# 1. single value
# 2. multiple values joined by AND
# 3. multiple values joined by OR
# 3. query based on date

# #### Single Value Filter

# In[15]:


for r in countries_summary_cl.find({'country': 'Ireland'}, {'country':1, 'confirmed': 1}).limit(5):
    print(r)


# #### Boolean OR query

# In[16]:


for r in countries_summary_cl.find({ '$or' : [ { 'country' : 'Ireland' }, { 'country' : 'India' } ] }).limit(25):
    print(r['country'], r['confirmed'])


# #### Using IN

# In[17]:


for r in countries_summary_cl.find({'country': { '$in': [ "Ireland", "India" ] } }).limit(5):
    print(r)


# #### Using AND

# In[18]:


# this is analagous to the query in Compass: 
# { "date": new Date('2020-01-22')}
# and
# { '$and' : [{ 'country' : 'Ireland' }, { "date": new Date('2020-01-22')} ] }

import datetime

for r in countries_summary_cl.find({ '$and' : [ 
        { 'country' : 'Ireland' }, 
        { 'date' : datetime.datetime(2020, 1, 23, 0, 0) } ] }):
    print(r)


# ### Distinct Values

# In[19]:


countries_summary_cl.distinct("country")[:5]


# ### Regular Expressions
# 
# To partially match text, you can use a regular expression. Note that this is a computationally expensive operation and may be too slow to be effective on large text fields in large collections.
# 
# For more information: https://docs.mongodb.com/manual/reference/operator/query/regex/

# In[20]:


for r in countries_summary_cl.find({'country':{ '$regex': 'land$' } }).limit(2):
    print(r)


# You can compile a regular expression with python `re` module

# In[21]:


import re
regx = re.compile("ireland", re.IGNORECASE)
for r in countries_summary_cl.find({'country': { '$regex': regx } }).limit(1):
    print(r)


# ### Aggregations
# 
# Count: https://docs.mongodb.com/manual/reference/operator/aggregation/count/
#         
# Sum: https://docs.mongodb.com/manual/reference/operator/aggregation/sum/
# 

# In[22]:


global_and_us_cln = covid19_db['global_and_us']


# In[23]:


for agg in global_and_us_cln.aggregate([
    {'$group':{'_id':'$country','count':{'$sum': 1}}},
    {'$limit' : 5 }
]):
    print(agg)


# #### Sorting
# 
# To sort in an aggregation pipeline, use the $sort operator. This query will count the number of documents for each country in the collection, sorted in descending order of count, then in ascending order by ID in case of a tie. 
# 
# https://docs.mongodb.com/manual/reference/operator/aggregation/sort/

# In[24]:


for agg in global_and_us_cln.aggregate([
        {'$group':{'_id':'$country','count':{'$sum': 1}}},
        {'$sort' : { 'count' : -1, '_id': 1 } },
        {'$limit' : 5 }
    ]):
    print(agg)


# ### Sorting
# 
# To sort results by a field value, you use the $orderby operator. This query will return results sorted first by date, then by country. To reverse the ordering, use -1. 
# 
# https://docs.mongodb.com/manual/reference/operator/meta/orderby/
# 
# Note that this has been replaced by .sort() at the mongo shell

# In[25]:


for r in global_and_us_cln.find( {'$query': {}, '$orderby': { 'date' : 1 , 'country': 1} }).limit(5):
    print(r['date'], r['country'])


# #### Aggregations across several records

# In[26]:


for agg in global_and_us_cln.aggregate([
        {'$group':{'_id':'$country','recovered':{'$sum': '$recovered'}}},{'$limit' : 5 }
    ]):
    print(agg)


# ### Pandas dataframes
# 
# You may at some point want to convert your results to pandas dataframes. 
# 
# Pandas provides a relatively straighforward method to convert mongodb results (as well as other types of JSON or dictionary-based data) into a dataframe. However, keep in mind that you may be cramming a nested, tree-like structure into a tabular data format.

# In[27]:


import pandas as pd


# In[28]:


df = pd.DataFrame.from_records(global_and_us_cln.find({'country': 'Ireland'}))


# The results of this query show how nested data such as dictionaries or lists gets placed into columns. This may or may not be a problem for you, though ther esult it is not a normalized table and may not be amenable to SQL or pandas operations that would work on fields in first normal form (i.e., with single, indivisible values).  

# In[29]:


df.head()


# For example, the "loc" column contains a dictionary with two keys, 'type' and 'Point' - where 'Point' maps to a list of coordinates

# In[30]:


df.iloc[0]['loc']


# ## Section 2. Upload Data
# 
# You will work with the coronavirus research dataset from the Semantic Scholar team at the Allen Institute:
# 
# - Go to:
# https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html
# 
# - Download a subset of this data: cord-19_2020-03-13.tar.gz (0.3 GB)
# 
# - Untar it, you should get a folder named: 2020-13-13, within this folder, expand the noncomm-use-subset
# 
# - Create a new database (see [mongodb Client](mongosetup.md)) and upload dataset
# 

# In[31]:


import json
import glob


# Replace MDB_URL with your mongodb connection string

# In[32]:


MDB_URL = 'mongodb+srv://user:password@cluster0.movwmkq.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(MDB_URL)


# Replace path with your own directory path

# In[33]:


json_files = []
path = '/Users/olgascrivner/Documents/IU-DataScience/Database/Summer2022/Week7/2020-03-13/noncomm_use_subset/*.json'
for file_path in glob.glob(path):
    with open(file_path) as f:
        json_files.append(json.load(f))        
        


# In[34]:


db = client['Covid-19'] # database name .coronavirus


# Uncomment below to insert json files. If you ar egetting authentification error, make sure you have the correct user (with write and read) and password 

# In[35]:


# db['coronavirus'].insert_many(json_files[100:200]) # subset


# In[36]:


for r in db['coronavirus'].find().limit(1):
    print(r)

