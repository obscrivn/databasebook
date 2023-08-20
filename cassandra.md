# Introduction to Cassandra

## Definition
>"Distributed", "High performance" and "High availability" are the key factors why developers consider Cassandra; whereas "Sql", "Free" and "Easy" are the primary reasons why MySQL is favored.
<small>https://stackshare.io/stackups/cassandra-vs-mysql</small>


> "Originally open-sourced in 2008 by Facebook, Cassandra combines the distributed systems technologies from the Amazon Dynamo key-value store and Google’s BigTable column-based data model. With Cassandra’s decentralized architecture, there is no single point of failure in a cluster and its performance is able to scale linearly with the addition of nodes.""
<small> Source: https://www.credera.com/insights/cassandra-explained-5-minutes-less </small>

- Cassandra is able to easily scale across multiple data centers. 

Companies like Netflix use Cassandra’s decentralized model and replication strategy to make their data more resilient against outage such as the AWS Outage on Oct. 22, 2012.

## Use Cases

**Time Series Data Model** 

- Due to the data model and log-structured storage engine, Cassandra is well suited to store and analyze sequential data.

- Rows in a column are determined by the application, not a predefined schema. Each row in a column family can contain a different number of columns, and there is no requirement for the column names to match.

**Key-Value Data**

- Reddit and Digg have chosen to use Cassandra as a persistent cache for their data. As their traffic increases, Cassandra is able to scale linearly and without downtime as they add new nodes to their cluster.


## Installation

- 