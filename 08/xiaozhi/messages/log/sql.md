create table access_log(
	id int primary key auto_increment,
    ip varchar(512) NOT NULL default '',
    url varchar(521) NOT NULL default '',
    method varchar(521) NOT NULL default '',
    agreement varchar(521) NOT NULL default '',
    status int(11),
    flux varchar(521) NOT NULL default '',
    access_time varchar(521) NOT NULL default ''
) engine=innodb default charset=utf8;

ip, access_time, method, url, agreement, status, flux