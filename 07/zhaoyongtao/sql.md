```
# 创建数据库
mysql> create database user;

# 选择数据库
mysql> use user;

# 创建表
mysql> create table tb_user (
    -> id int primary key auto_increment not null,
    -> username varchar(16) not null,
    -> age tinyint(4) not null,
    -> tel varchar(20) not null,
    -> password varchar(512) not null
    -> ) engine=innodb default charset=utf8;

# 查看表结构
mysql> desc tb_user;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| username | varchar(16)  | NO   |     | NULL    |                |
| age      | tinyint(4)   | NO   |     | NULL    |                |
| tel      | varchar(20)  | NO   |     | NULL    |                |
| password | varchar(512) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+


# 插入数据
mysql> insert into tb_user(username,age,tel,password) value('kk',22,'15688886666','123456');
Query OK, 1 row affected, 1 warning (0.00 sec)

mysql> insert into tb_user(username,age,tel,password) value('kk2',18,'15866668888','123456');
Query OK, 1 row affected, 1 warning (0.00 sec)

# 查询
mysql> select * from tb_user;
+----+----------+-----+-------------+----------+
| id | username | age | tel         | password |
+----+----------+-----+-------------+----------+
|  1 | kk       |  22 | 15688886666 | 123456   |
|  2 | kk2      |  18 | 15866668888 | 123456   |
+----+----------+-----+-------------+----------+
2 rows in set (0.00 sec)

# 按条件查询
mysql> select * from tb_user where id=1;
+----+----------+-----+-------------+----------+
| id | username | age | tel         | password |
+----+----------+-----+-------------+----------+
|  1 | kk       |  22 | 15688886666 | 123456   |
+----+----------+-----+-------------+----------+
1 row in set (0.00 sec)

# 修改
mysql> update tb_user set age=119 where id=2;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from tb_user;
+----+----------+-----+-------------+----------+
| id | username | age | tel         | password |
+----+----------+-----+-------------+----------+
|  1 | kk       |  22 | 15688886666 | 123456   |
|  2 | kk2      | 119 | 15866668888 | 123456   |
+----+----------+-----+-------------+----------+
2 rows in set (0.00 sec)


# 删除
mysql> delete from tb_user where id=2;
Query OK, 1 row affected (0.00 sec)

mysql> select * from tb_user;
+----+----------+-----+-------------+----------+
| id | username | age | tel         | password |
+----+----------+-----+-------------+----------+
|  1 | kk       |  22 | 15688886666 | 123456   |
+----+----------+-----+-------------+----------+
1 row in set (0.00 sec)

```
