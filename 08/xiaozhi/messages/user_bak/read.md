创建userlist表
create table userlist(
	id int primary key auto_increment,
    username varchar(512) NOT NULL default '',
    password varchar(521) NOT NULL default '',
    age int(11),
    tel int(128),
    create_date datetime
) engine=innodb default charset=utf8;

插入一条数据
insert into userlist(username, password, age, tel, create_date) values('xiaozhi','123456',29, '123456', now());

安装pymysql 库
pip3 install pymysql