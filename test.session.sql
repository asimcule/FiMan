SHOW TABLES;

-- @block
DROP TABLE registered_users;

-- @block
SELECT * FROM registered_users;

-- @block
DELETE FROM registered_users;

-- @block
SHOW TABLES;

-- @block
CREATE TABLE `registered_users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` text,
  PRIMARY KEY (`id`)
)

-- @block
CREATE TABLE `profile` (
  `id` int NOT NULL,
  `session_id` int DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `savings` int DEFAULT '0',
  `pay_day` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `session_id` (`session_id`),
  CONSTRAINT `profile_ibfk_1` FOREIGN KEY (`session_id`) REFERENCES `registered_users` (`id`)
)


-- @block
-- Table schema for expense
CREATE TABLE `expense` (
  `id` int NOT NULL,
  `session_id` int DEFAULT NULL,
  `product_category` varchar(80) DEFAULT NULL,
  `product_description` text,
  `amount` int DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `session_id` (`session_id`),
  CONSTRAINT `expense_ibfk_1` FOREIGN KEY (`session_id`) REFERENCES `registered_users` (`id`)
)