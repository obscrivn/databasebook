# Normalization

## Review of Normalization Forms
> Database Normalization is a set of rules that are applied to a database, such that the schema of the database ensures that all the rules are being followed. 

These rules are also known as **Normal Forms** and are widely used while designing database solutions.

The database normalization process can be divided into following types:

- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)
- Boyce-Codd Normal Form or Fourth Normal Form (BCNF of 4NF)

### First Normal Form (1NF)
- Data is stored in tables with rows that can be uniquely identified by a Primary Key
- Data within each table is stored in individual columns in its most reduced form
- There are no repeating groups.
### Second Normal Form (2NF)
- All the rules from 1NF must be satisfied
- Only data that relates to a table’s primary key is stored in each table
### Third Normal Form (3NF)
- All the rules from 2NF must be satisfied.
- There should be no intra-table dependencies between the columns in each table