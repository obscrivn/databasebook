# Practice

## Follow Along

In this tutorial, we will be createing a database and re-designing it so that it supports all the three Normal Forms.

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
- Create a table Employees
```sql
CREATE TABLE Employees (
ID INT PRIMARY KEY AUTO_INCREMENT,
FirstName VARCHAR(50),
LastName VARCHAR(50),
HourlyWage DECIMAL(5,2),
HireDate DATE
);
```
- Create a table ProjectEmployees
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
!()[_static/project_schema.png]
