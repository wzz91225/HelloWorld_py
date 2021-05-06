CREATE DATABASE IF NOT EXISTS project;
use project;
create table patient (
`id` int NOT NULL AUTO_INCREMENT,
`name` varchar(30) DEFAULT NULL,
`sex` varchar(10) DEFAULT NULL,
`birth_year` int DEFAULT NULL,
`Covid19` int DEFAULT NULL,
`result` double DEFAULT NULL,
`datacolume1` MEDIUMTEXT DEFAULT NULL,
`datacolume2` MEDIUMTEXT DEFAULT NULL,
`datacolume3` MEDIUMTEXT DEFAULT NULL,
PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
