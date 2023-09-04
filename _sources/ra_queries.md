## SQL Examples

-- Projection example
```
SELECT DISTINCT member_id FROM borrow;
SELECT DISTINCT member_id,book_id FROM borrow;
```
-- Selection example
```
SELECT * FROM member WHERE date_of_birth='1997-10-21';
```
-- Rename example
```
SELECT name AS firstName  FROM member; 
```

-- Cross product example
```
SELECT * FROM member,borrow;
```
-- Natural join example
```
SELECT * FROM member NATURAL JOIN borrow;
```

-- Union example
```
SELECT book_id FROM member natural join borrow where name='Charlie' UNION
SELECT book_id FROM member natural join borrow where name='Mike';
```

-- Intersection example

```
SELECT borrow.member_id FROM borrow 
JOIN book ON book.book_id = borrow.book_id 
WHERE name IN ('Fences','Inheritance')
GROUP BY member_id;
```












