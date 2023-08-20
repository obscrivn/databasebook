#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import sys
import pandas as pd
import numpy as np
from operator import itemgetter
import redis


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


get_ipython().system('pip install redis')


# In[4]:


r = redis.Redis(host='127.0.0.1', port=6379, db=0) #the object r is created
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
r.get("Bahamas")


# In[5]:


import csv
import sys
import pandas as pd
import numpy as np
from operator import itemgetter
import random


# In[6]:


random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}


# In[7]:


r = redis.Redis(db=1)


# In[8]:


with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        pipe.hmset(h_id, hat)
    pipe.execute()


# In[25]:


r.bgsave()


# In[26]:


print(r.hgetall("hat:56854717"))


# In[28]:


#The first thing that we want to simulate is what happens when a user clicks Purchase. If the item is in stock, increase its npurchased by 1 and decrease its quantity (inventory) by 1. You can use .hincrby() to do this:

r.hincrby("hat:56854717", "quantity", -1)
r.hget("hat:56854717", "quantity")
r.hincrby("hat:56854717", "npurchased", 1)


# In[14]:


import logging


# In[27]:


logging.basicConfig()

class OutOfStockError(Exception):
    """Raised when PyHats.com is all out of today's hottest hat"""

def buyitem(r: redis.Redis, itemid: int) -> None:
    with r.pipeline() as pipe:
        error_count = 0
        while True:
            try:
                # Get available inventory, watching for changes
                # related to this itemid before the transaction
                pipe.watch(itemid)
                nleft: bytes = r.hget(itemid, "quantity")
                if nleft > b"0":
                    pipe.multi()
                    pipe.hincrby(itemid, "quantity", -1)
                    pipe.hincrby(itemid, "npurchased", 1)
                    pipe.execute()
                    break
                else:
                    # Stop watching the itemid and raise to break out
                    pipe.unwatch()
                    raise OutOfStockError(
                        f"Sorry, {itemid} is out of stock!"
                    )
            except redis.WatchError:
                # Log total num. of errors by this user to buy this item,
                # then try the same process again of WATCH/HGET/MULTI/EXEC
                error_count += 1
                logging.warning(
                    "WatchError #%d: %s; retrying",
                    error_count, itemid
                )
    return None


# In[18]:


buyitem(r, "hat:56854717")
buyitem(r, "hat:56854717")
buyitem(r, "hat:56854717")
r.hmget("hat:56854717", "quantity", "npurchased")


# In[19]:


# Buy remaining 196 hats for item 56854717 and deplete stock to 0
for _ in range(196):
    buyitem(r, "hat:56854717")
r.hmget("hat:56854717", "quantity", "npurchased")


# In[20]:


buyitem(r, "hat:56854717")


# In[9]:


for _ in range(196):
    buyitem(r, "hat:56854717")
r.hmget("hat:56854717", "quantity", "npurchased")


# In[36]:


r.set("Bahamas", "Nassau")


# In[37]:


r.get("Bahamas")


# In[40]:


r.set("Bahamas", "Nassau")
r.get("Bahamas")


# In[42]:


r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
r.get("Bahamas")


# In[43]:


r.exists("Norway")


# In[46]:


r.hset("realpython", "url", "https://realpython.com/")


# In[49]:


r.hgetall("realpython")


# In[51]:


r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
r.get("Bahamas")


# In[ ]:




