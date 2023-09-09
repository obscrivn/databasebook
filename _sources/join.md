# Join Types

<small>Source: https://www.geeksforgeeks.org/difference-between-natural-join-and-inner-join-in-sql/ </small>

## Natural Join

> Natural Join joins two tables based on same attribute name and datatypes. The resulting table will contain all the attributes of both the table but keep only one copy of each common column. 

```sql
SELECT * 
FROM table1 NATURAL JOIN table2; 
```

## Inner Join

> Inner Join joins two table on the basis of the column which is explicitly specified in the ON clause. The resulting table will contain all the attributes from both the tables including common column also 

- Only those records will return which exists in both the tables
- The resulting table will contain all the attribute of both the tables including duplicate columns also


```sql
SELECT * 
FROM table1 INNER JOIN table2 ON table1.Column_Name = table2.Column_Name; 
```

```{note}
The Natural Joins are not supported in the SQL Server
```
