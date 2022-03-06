#!/bin/sh
echo "select employee data"
empname=`mysql -u root -p scott<<EOFMYSQL
select ename from emp;
EOFMYSQL`
python a5.py $empname

