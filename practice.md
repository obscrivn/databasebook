# Practice

## Follow Along

In this tutorial, we will be createing a database and re-designing it so that it supports all the three Normal Forms.
<small>Reference: https://www.sqlservercentral.com/articles/database-normalization-in-sql-with-examples</small>

- Create a table Projects
   - Create ID column as a primary key and generate IDs automatically and by incrementation
   - Specify VARCHAR values
```sql
CREATE TABLE Projects (
ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(100),
Value DECIMAL(5,2),
StartDate DATE,
EndDate DATE
);
```
- Create a table `Employees`
  - `ID` is a primary key and will be created automatically
```sql
CREATE TABLE Employees (
ID INT PRIMARY KEY AUTO_INCREMENT,
FirstName VARCHAR(50),
LastName VARCHAR(50),
HourlyWage DECIMAL(5,2),
HireDate DATE
);
```
- Create a table `ProjectEmployees`
    - Add a foreign key constraint called `FK_ProjectEmployees_Projects` to the `ProjectID` column
   - Referential integrity between "ProjectEmployees" table and the "Projects" table based on the `ProjectID` column
    - Add a foreign key constraint called `FK_ProjectEmployees_Projects` to the `ProjectID` column
   - Referential integrity between "ProjectEmployees" table and the "JobOrders" table based on the `EmployeeID` column
```sql
CREATE TABLE ProjectEmployees (
ID INT PRIMARY KEY AUTO_INCREMENT,
ProjectID INT,
EmployeeID INT,
Hours DECIMAL(5,2),
CONSTRAINT FK_ProjectEmployees_Projects FOREIGN KEY (ProjectID) REFERENCES  Projects (ID),
CONSTRAINT FK_ProjectEmployees_Employees FOREIGN KEY (EmployeeID) REFERENCES  Employees (ID)
);
```
- Create a table `JobOrders`
    - Create a foreign key between tables `JobOrders` and `Projects` on `ProjectID`
    - Create a foreign key between tables `JobOrders` and `Employees` on `EmployeeID`
```sql
CREATE TABLE JobOrders (
ID INT PRIMARY KEY AUTO_INCREMENT,
EmployeeID INT,
ProjectID INT,
Description TEXT,
OrderDateTime DATETIME,
Quantity INT,
Price DECIMAL(5,2),
CONSTRAINT FK_JobOrders_Projects FOREIGN KEY (ProjectID) REFERENCES  Projects (ID),
CONSTRAINT FK_JobOrders_Employees FOREIGN KEY (EmployeeID) REFERENCES  Employees (ID)
);
```
- Create a table `Customers`
    - Notice the various use of datatypes: TEXT, INT, VARCHAR
```sql
CREATE TABLE Customers (
    Name VARCHAR(100),
    Industry VARCHAR(100),
    Project1_ID INT,
    Project1_Feedback TEXT,
    Project2_ID INT,
    Project2_Feedback TEXT,
    ContactPersonID INT,
    ContactPersonAndRole VARCHAR(255),
    PhoneNumber VARCHAR(12),
    Address VARCHAR(255),
    City VARCHAR(255),
    Zip VARCHAR(5)
  )
```

<img src="_static/project_schema.png" alt="project schema" width = 250 />

Q1: Do you see which table violates the Normalization Form and why?

> The Customers table violates all the three rules of the first normal form:

- No Primary Key in the table
- The data is not found in its most reduced form. For example, the column ContactPersonAndRole can be divided further into two individual columns - ContactPerson and ContactPersonRole
- There are two repeating groups of columns in this table - (Project1_ID, Project1_FeedBack) and (Project2_ID, Project2_Feedback). We need to get these removed from this table.

### How to Fix 1NF

- The first thing that we need to do is to add a **primary key** to this table using `ALTER TABLE` and `ADD`
- We can add a new column ID with datatype as INT and also automatically increment values

```sql
ALTER TABLE Customers
ADD ID INT AUTO_INCREMENT PRIMARY KEY;
```

- We need to split the column ContactPersonAndRole into two individual columnsRename and add a new column

  - Rename the original column from ContactPersonAndRole to ContactPerson
  - Add a new column for ContactPersonRole

```sql
ALTER TABLE Customers 
CHANGE ContactPersonAndRole ContactPerson VARCHAR(255),
ADD ContactPersonRole VARCHAR(20);
```

- We need to move the columns Project1_ID, Project1_Feedback, Project2_ID, and Project2_Feedback into a new table using `DROP COLUMN`
```sql
ALTER TABLE Customers
DROP COLUMN Project1_ID;

ALTER TABLE Customers
DROP COLUMN Project1_Feedback;

ALTER TABLE Customers
DROP COLUMN Project2_ID;
```

- In the new table we have Project and Customer ids and foreign key constraints on Projects and Customers ids
```sql
CREATE TABLE ProjectFeedback (
ID INT PRIMARY KEY AUTO_INCREMENT,
ProjectID INT,
CustomerID INT,
Feedback TEXT,
CONSTRAINT FK_ProjectFeedbacks_Projects FOREIGN KEY (ProjectID) REFERENCES  Projects (ID),
CONSTRAINT FK_ProjectFeedbacks_Customers FOREIGN KEY (CustomerID) REFERENCES  Customers (ID)
);
```

### How to Fix 2NF
> the ContactPerson, ContactPersonRole and the PhoneNumber do not directly relate to the ID of the Customers table. That is because the primary key refers to a customer
- we need to remove these three columns from the Customers table and put them in a separate table. This table should contain data that is related only to the contact person and not the customer


```sql
ALTER TABLE Customers
DROP COLUMN ContactPerson;

ALTER TABLE Customers
DROP COLUMN ContactPersonRole;

ALTER TABLE Customers
DROP COLUMN PhoneNumber;
```

```sql
CREATE TABLE ContactPersons (
ID INT PRIMARY KEY AUTO_INCREMENT,
ContactPerson VARCHAR(100),
ContactPersonRole VARCHAR(20),
PhoneNumber VARCHAR(12)
);
```
- We also need to add a foreign key constraint to Customers
```sql
ALTER TABLE Customers
ADD CONSTRAINT FK_Customers_ContactPersons FOREIGN KEY (ContactPersonID)
REFERENCES ContactPersons(ID);
```

### How to Fix 3NF

> If ColumnA relies on the primary key and also on the ColumnB, then ColumnA is known to be transitively dependent on the primary key and it violates the third normal form.
<center>
<img src="_static/customers.png" alt="customer" width = 350 />
</center>
> The transitive dependent relationship is between the columns - City and Zip. The city in which a customer is situated relates to the primary key of the customer, so this satisfies the second normal form. However, the city also depends on the zip code.

- Remove the City from the Customers table
- Create a new table ZipCodes to store the Zip and City
- Add a foreign key relation
```sql
ALTER TABLE Customers
DROP COLUMN City;
```

```sql
CREATE TABLE ZipCodes (
ZipID VARCHAR(5) PRIMARY KEY,
City VARCHAR(255)
);
```

```sql
ALTER TABLE Customers
ADD CONSTRAINT FK_Customers_ZipCodes FOREIGN KEY (Zip)
REFERENCES ZipCodes(ZipID);
```