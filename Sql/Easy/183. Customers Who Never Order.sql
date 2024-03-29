-- Suppose that a website contains two tables, 
-- the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

-- Table: Customers.

-- +----+-------+
-- | Id | Name  |
-- +----+-------+
-- | 1  | Joe   |
-- | 2  | Henry |
-- | 3  | Sam   |
-- | 4  | Max   |
-- +----+-------+
-- Table: Orders.

-- +----+------------+
-- | Id | CustomerId |
-- +----+------------+
-- | 1  | 3          |
-- | 2  | 1          |
-- +----+------------+
-- Using the above tables as example, return the following:

-- +-----------+
-- | Customers |
-- +-----------+
-- | Henry     |
-- | Max       |
-- +-----------+


-- Solution

SELECT t1.name AS 'Customers'
FROM customers t1
left join
(
    SELECT customerid FROM orders
) t2
on t1.id = t2.customerid
where t2.customerid is null

/*
Select Name as Customers
from Customers
where id != All(select c.id
                from Customers c, Orders o
                where c.id = o.Customerid) 
*/