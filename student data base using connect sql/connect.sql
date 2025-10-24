use mydb;
create table if not exists students(
id INT AUTO_INCREMENT PRIMARY KEY,
name varchar(20) not null,
age int not null
);

insert into students(name,age)values('elam',20),('virat',35);

select * from students