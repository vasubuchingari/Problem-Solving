#SQL

select distinct country from customers;

select count(distinct country) from customers;
(or)
select count(*) as distinctcountries from(select distinct country from customers);


select * from customers where country="Mexico";
select * from customers where customerID=1;

selct * from customers where city in ("mexico","brazil");

selct * from customers where city like "s%";

select * from customers where country ="germany" and city="berlin";

select * from customers where country ="germany" or city="berlin";

selct * from customers where not country="germany";

select * from customers where country="germany" and (city="nlr" or city="rtm");

select * from customers where not country="germany" and country="USA";


select * from customers order by country;
select * from customers order by country desc;
select * from customers order by country,customername;
select * from customers order by country asc,customername desc;


insert into customers(name,contact,address,city,country)
values("bvs",7356,"14th avenue","NLR","IND");


select customername,contact,address from customers where address is null;
select customername,contact,address from customers where address is not null;


update customers set contactname="helbigs",city="bloomberg" where customerID=1;
update customers set contactname="juan" where country ="mexico";


delete from customers where customername="kalki";
delete from customers;#deletes every rows


select top 3 * from customers;#sql server/MS Access
select * from customers limit 3;#mysql
select * from customers fetch first 3 rows only;#oracle

select top 50 percent * from customers;#ms
select * from customers fetch first 50 percent rows only;#oracle
selct top 6 * from customers where country="germany";
select * from customers where country="germany" limit 3;
select * from customers where country="germany" fetch first 3 rows only;


select min(price) as minprice from product;
select max(price) as maxprice from products;

select count(productid) from products;
select avg(price) from products;
select sum(quantity) from products;


select * from customers where customername like "a%";
select * from customers where customername like "%a";
select * from customers where customername like "%or%";
select * from customers where customername like "_r%";
select * from customers where customername like "a___%";
select * from customers where customername like "a%o";
select * from customers where customername not like "a%";


bl* or bl%   blue,black,blob
h?t   hut,hit,hot
h[oa]t  hot,hat #any single charecter
h[!oa]t or h[^oa]t  hit,hut
c[a-d]t  cat,cbt,cct
1#3   143,123,153,163,173,183


selct * from customers where city like "ber%";
SELECT * FROM Customers WHERE City LIKE '%es%';
select * from customers where city like "l_o_n";
select * from customers where city like "[bsp]%";
select * from customers where city like "[a-c]%";
select * from customers where city like "[!bsp]%";
select * fom customers where city not like "[]bsp%";


select * from customers where country in ("germany","france","UK");
select * from customers where country not in ("germany","france","UK");
select * from customers where country in (select country from suppliers);

select * from products where price between 10 and 20;
select * from products where price not between 10 and 20;
select * from products where price between 10 and 20 and categoryid not in(1,2,3);
select * from products where productname between "abd" and "zxc" order by productname;
select * from orders where orderdate between #07/01/1996# and #07/31/1996#;
select * from orders where orderdate between "1996-07-01" and "1996-07-31";


select customerid as id,customername as customer from customers;
select customerid as id,customername as [cust name] from customers;
select customername,address + "," + postalcode + "," + city + "," + country as address from customers;
select customername,concat(Address,', ',PostalCode,', ',City,', ',Country) as address from customers;#mysql
SELECT CustomerName, (Address || ', ' || PostalCode || ' ' || City || ', ' || Country) AS Address
FROM Customers;

select o.orderid,o.orderdate,c.customername from customers as c,orders as o where c.customername="ankit" and c.customerid=o.customerid;

select orders.orderid,customers.customername,orders.orderdate from orders inner join customers on orders.customerid=costomers.customerid;

select orders.orderid,customers.customername,shippers.shippername from((orders 
inner join customers on orders.customerid=customers.customerid)
inner join shippers on orders.shipperid=shippers.shipperid);

select customers.customername,orders.ordersid from customers 
left join orders on customers.customerid=orders.customerid
order by customers.customername;


select orders.orderid,employees.lastname,employees.firstname
from orders
right join employees on orders.employeeid=employees.employeeid
order by orders.orderid;

select customers.customername,orders.orderid from customers
full outer join orders on customers.customerid=orders.customerid
order by customers.customername;


select a.customername as customername1,b.customername as customername2,a.city
from customers a,customers b
where a.customerid<>b.customerid
and a.city=b.city
order by a.city;


select city from customers 
union all
select city from suppliers order by city;

select city,country from customers where country="germany" 
union
selct city,country from suppliers
where country="germany"
order by city;


select "customers" as type,contactname,city,country from customers
union 
select "supplier",contactname,city,country
from suppliers;

select count(customerID),country
from customers
group by country;

select count(customerid),country
from customers
group by country
order by count(customerid) desc;

select count(customerid) ,country
from customers
group by country
order by count(customerid) desc;

select shippers.shippername,count(orders.orderid) as number of orders
from orders left join shippers
on orders.shipperid=shippers.shipperid
group by shippername;

select count(customerid),country
from customers
group by country
having count(customerid) >5;

select count(customerid),country
from customers
gropu by country
having count(customerid)>5
order by count(customerdid) desc;

select employees.lastname,count(orders.orderid) as numberoforders
from orders
inner join employees on orders.employeeid=employees.employeeid
where lastname="davalio"or lastnaqme="fuller"
group by lastname
having count(orders.ordersid)>25;


select suppliersname
from suppliers
where exists(select productname from products where products.productid=suppliers.supplierid and price<20);

select suppliername
from suppliers
where exists(select productname from products where products.supplierid=suppliers.supplierid and price=22);


select productname
from products
where productid=any
(select productid from orderdetails where quantity =10);

select productname
from products
where productid=all
(select orderdetails where quantity=10);

offset is used to exclude above records
limit to retrieve number of cells
SELECT CONCAT(EmpFname, ' ', EmpLname) AS 'FullName' FROM EmployeeInfo;
SELECT * FROM EmployeeInfo WHERE EmpFname NOT IN ('Sanjay','Sonia')

  
SELECT * FROM employee;
//retrieves the employee table

SELECT * FROM employee ORDER BY age DESC;
//retrieves employee table and orders by descending

SELECT e.id, e.name, e.email, e.age, d.name AS department, p.title AS position
FROM employee e
INNER JOIN department d ON e.department_id = d.id
INNER JOIN positions p ON e.position_id = p.id;
//employee with dept,position details

SELECT * FROM employee WHERE department_id = 1;
//

SELECT e.id, e.name, SUM(s.amount) AS total_salary
FROM employee e
LEFT JOIN salary s ON e.id = s.employee_id
GROUP BY e.id, e.name;

SELECT d.name AS department, COUNT(e.id) AS num_employees
FROM department d
LEFT JOIN employee e ON d.id = e.department_id
GROUP BY d.name;

SELECT e.id, e.name
FROM employee e
LEFT JOIN leaves l ON e.id = l.employee_id
WHERE l.id IS NULL;


SELECT e.id, e.name, l.start_date, l.end_date
FROM employee e
INNER JOIN leaves l ON e.id = l.employee_id
WHERE l.start_date <= CURDATE() AND l.end_date >= CURDATE();


SELECT * FROM employee WHERE is_manager = 1;

SELECT e.id, e.name, MAX(s.amount) AS highest_salary
FROM employee e
LEFT JOIN salary s ON e.id = s.employee_id
GROUP BY e.id, e.name;




