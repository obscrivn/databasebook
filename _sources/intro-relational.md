# 1.2 Relational Databases and SQL

```{note}
**Big idea:** A relational database is a structured way to store data so that records, relationships, and rules are clear.

SQL is the language people use to work with that data.
```

This chapter gives you the practical foundation you need before you start querying a database.

We will keep the focus narrow and useful:

- what a relational database is
- what SQL is
- how relational systems differ from one another
- how database tools and database servers are not the same thing

## 1. What is a relational database?

A relational database stores data in tables.

A table is made of:

- **rows**: one record or one instance of something
- **columns**: the fields or attributes for those records
- **keys**: identifiers that connect related data
- **schema**: the structure of the table and its rules

A simple example:

| student_id | first_name | last_name | major |
| --- | --- | --- | --- |
| 1001 | Maya | Patel | Data Science |
| 1002 | Luis | Gomez | Information Systems |

This table stores student records in a structured way.

Each row represents one student.

Each column stores one type of information.

The `student_id` helps identify each row and may also link to other tables.

### Core relational ideas

- **Entity**: a person, place, event, or thing we care about
- **Attribute**: a property of that entity
- **Relationship**: a connection between entities
- **Table**: the storage structure for rows and columns
- **Key**: a way to identify and connect records

## 2. What is SQL?

**SQL** stands for Structured Query Language.

It is the standard language used to:

- define database structure
- insert new data
- update data
- delete data
- ask questions about data

A few basic examples:

```sql
SELECT first_name, last_name
FROM students;
```

This asks for names from the `students` table.

```sql
INSERT INTO students (student_id, first_name, last_name, major)
VALUES (1003, 'Aisha', 'Nguyen', 'Database Systems');
```

This adds a new row.

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    major VARCHAR(50)
);
```

This creates a table with its structure.

```{important}
SQL is not a single database product.

SQL is a language standard. Different database systems implement it in slightly different ways.
```

## 3. SQL is a standard, databases are products

This is one of the most important ideas in the course.

- **SQL** = the language
- **MySQL, PostgreSQL, SQLite, SQL Server, Oracle** = database systems that implement SQL

The language is transferable.

The products are not identical.

Each database system may differ in:

- features
- performance characteristics
- storage and indexing options
- tooling
- deployment model
- ecosystem support

This means you should learn the ideas behind SQL and relational design, not only the buttons or interface of one product.

## 4. Common relational database systems

Here are a few of the most common systems you will hear about:

| System | Helpful student-level distinction |
| --- | --- |
| SQLite | A small, file-based SQL database often used locally and in embedded applications |
| MySQL | A popular client/server relational database system used in many web applications |
| PostgreSQL | A powerful open-source relational database with strong SQL support and features |
| SQL Server | Microsoft’s relational database platform |
| Oracle Database | A major enterprise relational database platform |

```{note}
SQLite is especially useful to distinguish because it is a serverless SQL engine that stores data in a database file.

MySQL and PostgreSQL are usually run as database servers that clients connect to over a network or local connection.
```

This matters because it is easy to assume that every database is the same kind of system.

## 5. Local database vs database server

A beginner often confuses these two models.

### SQLite

```text
Application → database file
```

SQLite stores data in a single file on the local machine.

This makes it easy for small projects, local development, and lightweight tools.

### MySQL or PostgreSQL

```text
Application → database server → database
```

In a client/server database system:

- the database server manages the database
- the application connects to the server
- the server handles queries, transactions, and access

This setup is common for multi-user systems and web applications.

## 6. Database server vs database tool

This distinction is important.

> **MySQL Server** is the database management system.

> **MySQL Workbench** is a graphical client used to connect to and work with that server.

The same pattern is true for many tools:

- the **server** stores and manages the database
- the **client or tool** helps you connect, query, and inspect it

You should not confuse the tool with the database itself.

This is why database concepts, server setup, credentials, ports, and connections matter so much in real software work.

## 7. Databases can run locally or in the cloud

Relational databases are not limited to a laptop.

```text
Local machine
Application → SQLite or local MySQL/PostgreSQL
```

```text
Cloud / managed service
Application → managed database service → relational database
```

A modern example is Google Cloud SQL.

It provides managed relational database services for MySQL, PostgreSQL, and SQL Server.

The important idea is simple:

> The relational model does not change just because the database is hosted in the cloud.

What changes is the deployment and management model.

## 9. What comes next?

```{note}
**Next: See a database in action**

In the Coding Practice, you will use SQLite and interact with a relational database.
```

## References

- PostgreSQL Documentation: [https://www.postgresql.org/docs/current/intro-whatis.html](https://www.postgresql.org/docs/current/intro-whatis.html)
- SQLite Documentation: [https://www.sqlite.org/docs.html](https://www.sqlite.org/docs.html)
- MySQL Documentation: [https://dev.mysql.com/doc/](https://dev.mysql.com/doc/)
- Oracle Database Concepts: [https://docs.oracle.com/en/database/oracle/oracle-database/](https://docs.oracle.com/en/database/oracle/oracle-database/)
- Microsoft SQL Server Documentation: [https://learn.microsoft.com/en-us/sql/sql-server](https://learn.microsoft.com/en-us/sql/sql-server)

