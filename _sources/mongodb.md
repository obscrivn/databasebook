# MongoDB Client

## What is MongoDB Client?

> The MongoClient() class for the PyMongo driver library for MongoDB creates client instances. Its main function is to enable you to connect to the MongoDB database efficiently and effortlessly.

- Install pymongo: See https://pymongo.readthedocs.io/en/stable/installation.html

```{note}
- $ python3 -m pip install pymongo
- !pip install pymongo
```
- Create MongoClient

![](_static/m1.png)

You can specify the client:
```
mongodb_url = "mongodb+srv://readonly:readonly@covid-19.hip2i.mongodb.net/covid19"

client = MongoClient(mongodb_url)
```

## Create Connection with MongoDB Compass

<object data="_static/MongoDB-Python-workshop.pdf" width="950" height="650" type='application/pdf'/></object>
