-- Database Export for Cloud Migration

DROP TABLE IF EXISTS order_details;
CREATE TABLE `order_details` (
  `order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` double NOT NULL,
  `total_price` double NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `fk_product_id_idx` (`product_id`),
  CONSTRAINT `fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON UPDATE RESTRICT,
  CONSTRAINT `fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO order_details VALUES
(1, 1, 2.0, 60.0),
(2, 1, 1.0, 100.0);

DROP TABLE IF EXISTS orders;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(100) NOT NULL,
  `total_price` double NOT NULL,
  `date_time` datetime NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO orders VALUES
(1, 'ankush', 3000.0, '2026-02-16 00:00:00'),
(2, 'Test User', 100.0, '2026-02-17 02:39:40');

DROP TABLE IF EXISTS products;
CREATE TABLE `products` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `uom_id` int NOT NULL,
  `price_per_unit` double NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `fk_uom_id_idx` (`uom_id`),
  CONSTRAINT `fk_uom_id` FOREIGN KEY (`uom_id`) REFERENCES `uom` (`uom_id`) ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO products VALUES
(1, 'toothpaste', 1, 30.0),
(2, 'spinach', 1, 34.5),
(6, 'bread', 1, 10.0),
(7, 'potato', 1, 20.0),
(8, 'bread', 1, 10.0);

DROP TABLE IF EXISTS uom;
CREATE TABLE `uom` (
  `uom_id` int NOT NULL AUTO_INCREMENT,
  `uom_name` varchar(45) NOT NULL,
  PRIMARY KEY (`uom_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO uom VALUES
(1, 'each');

