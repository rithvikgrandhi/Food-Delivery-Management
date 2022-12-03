-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 03, 2022 at 11:55 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `food_delivery_management`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `backup` ()   BEGIN
      DECLARE done INT DEFAULT 0;
      DECLARE Order_timestamp,Order_amount,Order_status,customer_id,delivery_id,payment_id,Order_id VARCHAR(30);
      DECLARE cur CURSOR FOR SELECT * FROM order_details;
      DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
      OPEN cur;
      label: LOOP
      FETCH cur INTO Order_timestamp,Order_amount,Order_status,customer_id,delivery_id,payment_id,Order_id	;
      INSERT INTO payment_backup VALUES(Order_timestamp,Order_amount,Order_status,customer_id,delivery_id,payment_id,Order_id);
      IF done = 1 THEN LEAVE label;
      END IF;
      END LOOP;
      CLOSE cur;
   END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `beverages` ()   BEGIN
    select * from menu_items
    where category_id = 207;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `chinese` ()   BEGIN
    select * from menu_items
    where category_id = 204;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `desserts` ()   BEGIN
    select * from menu_items
    where category_id = 208;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `fullname` (IN `cus_id` INT, INOUT `fullList` VARCHAR(4000))   BEGIN
  DECLARE finished INTEGER DEFAULT 0;
  DECLARE full varchar(100) DEFAULT "";
   #Cursor declaration
      DECLARE curName
        CURSOR FOR
             SELECT concat(customer_firstname ,' ' , customer_lastname) FROM customer where customer_id=cus_id;
               #declare NOT FOUND handler
               DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
    #Open cursor
               OPEN curName;
    #fetch records
               getName: LOOP
                              FETCH curName INTO full;
                              IF finished = 1 THEN LEAVE getName;
                              END IF;
                              SET fullList = CONCAT(full," ",fullList);
               END LOOP getName;
               CLOSE curName;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `italian` ()   BEGIN
    select * from menu_items
    where category_id = 203;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `north_indian` ()   BEGIN
    select * from menu_items
    where category_id = 202;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `random_admin` (IN `customer_id` INT)   begin
declare admin int;
set admin = FLOOR(1 + RAND()*2);
update customer set admin_id=admin where customer_id=customer.customer_id;
end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `snacks` ()   BEGIN
    select * from menu_items
    where category_id = 206;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `south_indian` ()   BEGIN
    select * from menu_items
    where category_id = 201;
END$$

--
-- Functions
--
CREATE DEFINER=`root`@`localhost` FUNCTION `check_strength` (`Admin_password` VARCHAR(16)) RETURNS VARCHAR(20) CHARSET utf8mb4 DETERMINISTIC BEGIN
DECLARE STRENGTH VARCHAR(20);
IF LENGTH(Admin_password) >= 8 THEN
SET STRENGTH = 'STRONG';
ELSEIF LENGTH(Admin_password) < 8 THEN
SET STRENGTH = 'WEAK';
END IF;
RETURN (STRENGTH);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Admin_id` int(11) NOT NULL,
  `Admin_name` varchar(15) NOT NULL,
  `Admin_password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Admin_id`, `Admin_name`, `Admin_password`) VALUES
(1, 'Rithvik Grandhi', 'Rithvik@123'),
(2, 'Admin2', 'Admin2@123'),
(3, 'test', 'test@12');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(15) NOT NULL,
  `resturant_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`category_id`, `category_name`, `resturant_id`) VALUES
(201, 'SOUTH-INDIAN', 112),
(202, 'NORTH-INDIAN', 111),
(203, 'ITALIAN', 121),
(204, 'CHINESE', 113),
(206, 'SNACKS', 118),
(207, 'BEVERAGES', 119),
(208, 'DESSERTS', 120);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `customer_firstname` varchar(30) NOT NULL,
  `customer_lastname` varchar(30) NOT NULL,
  `customer_password` varchar(16) NOT NULL,
  `customer_phoneno` varchar(10) NOT NULL,
  `customer_address` varchar(50) NOT NULL,
  `customer_email` varchar(20) NOT NULL,
  `Admin_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `customer_firstname`, `customer_lastname`, `customer_password`, `customer_phoneno`, `customer_address`, `customer_email`, `Admin_id`) VALUES
(101, 'Rishikesh', 'Sastri', 'gomma@123', '9348736640', 'Akshya Nagar 1st Block 1st Cross,Rammurthy\r\nnagar,', 'chad@gmail.com', 2),
(102, 'Jainam', 'Shah', 'Jainu@123', '9924567892', '117, Examiner Bldg, Nagindas Master Road,\r\nFort,Mu', 'jainam33@gmail.com', 2),
(103, 'Aman', 'Pandya', 'Aman@123', '7834578923', 'L 69 Sector 11,Delhi,Uttar Pradesh201301', 'aman@gmail.com', 2),
(104, 'Heer', 'Madia', 'Her@123', '8902345789', 'Bee House 138, Kodambakkam High Road,\r\nNungambakka', 'heer1723@gmail.com', 1),
(105, 'Akanksha', 'Yadav', 'Akayad@123', '9934654001', '295 Aj-kauser Road:10, West\r\nMarredpally,Hydrebad,', 'akuu@gmail.com', 2),
(106, 'Karan', 'Punjabi', 'karpun@123', '9934688001', 'Shopno1, Nirmal House, Tembhi Naka, Opp\r\nJain Mand', 'karan12@gmail.com', 1),
(107, 'Divya', 'Mulchandani', 'divmul@123', '9874688001', 'A/3, Tejpal Indl Estate, Andheri Kurla\r\nRoad, Andh', 'div3421@gmail.com', 1),
(108, 'Celia', 'Anthony', 'Celia@123', '7834654881', '134/135,shopno 12,14, Ground Floor\r\nNagarathpet Ma', 'Celia44@gmail.com', 2),
(109, 'Johnson', 'Thomas', 'Jthomas@123', '9931888912', ' A/108, A/108 1st, Doctor House,\r\nPaldi,Ahmeadabad', 'jthomas550@gmail.com', 1),
(110, 'Dhara', 'Bhatt', 'Dhara@123', '9875678001', '66 Sector 24 Mujessar, Ram Swaroop\r\nColony,Delhi,H', 'dbhatt45@gmail.com', 2),
(123, 'BHARGAVI', '', '123', '1234567890', '', '', 1),
(1929, 'adjlsll', 'sdaklj', 'dwasldj', '8888888888', 'jlkasfjsa', 'jsadklj', 1);

--
-- Triggers `customer`
--
DELIMITER $$
CREATE TRIGGER `phone_warn` BEFORE INSERT ON `customer` FOR EACH ROW BEGIN
IF NEW.customer_phoneno <1000000000 or NEW.customer_phoneno>9999999999
THEN 
signal sqlstate '45000' set message_text = 'Invalid phone number';
END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `delivery_details`
--

CREATE TABLE `delivery_details` (
  `delivery_id` int(11) NOT NULL,
  `delivery_address` varchar(50) NOT NULL,
  `delivery_status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `delivery_details`
--

INSERT INTO `delivery_details` (`delivery_id`, `delivery_address`, `delivery_status`) VALUES
(12, 'A082', 'Preparing'),
(401, 'Akshya Nagar 1st Block 1st Cross,Rammurthy nagar,B', 'Delivered'),
(402, 'Shopno1, Nirmal House, Tembhi Naka, Opp Jain Mandi', 'Delivered'),
(403, 'L 69 Sector 11,Delhi,Uttar Pradesh-201301', 'Preparing'),
(404, 'Bee House 138, Kodambakkam High Road, Nungambakkam', 'Picked-up'),
(405, '295 Aj-kauser Road:10, West Marredpally,Hydrebad,A', 'Delivered'),
(406, '117, Examiner Bldg, Nagindas Master Road, Fort,Mum', 'Preparing'),
(407, 'A/3, Tejpal Indl Estate, Andheri Kurla Road, Andhe', 'Preparing'),
(408, '134/135,shopno 12,14, Ground Floor Nagarathpet Mai', 'Delivered'),
(409, '66 Sector 24 Mujessar, Ram Swaroop Colony,Delhi,Ha', 'Picked-up'),
(410, 'rahul\'s house, bangalore', 'Delivered');

-- --------------------------------------------------------

--
-- Table structure for table `menu_items`
--

CREATE TABLE `menu_items` (
  `item_code` int(11) NOT NULL,
  `item_name` varchar(20) NOT NULL,
  `Price` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `menu_items`
--

INSERT INTO `menu_items` (`item_code`, `item_name`, `Price`, `category_id`) VALUES
(301, 'White Pasta', 230, 203),
(302, 'Arabita Pasta', 200, 203),
(303, 'Magherita pizza', 400, 203),
(304, 'gotala dosa', 300, 201),
(305, 'uttampam', 115, 201),
(306, 'idli-sambhar', 120, 201),
(307, 'aloo-cheese paratha', 120, 202),
(308, 'Paneer paratha', 250, 202),
(309, 'chole kulche', 100, 202),
(310, 'Dry manchrian', 200, 204),
(311, 'chinese bhel', 150, 204),
(312, 'Fried rice', 210, 204),
(316, 'waffle', 220, 208),
(317, 'chocolate brownie', 115, 208),
(318, 'pancakes', 120, 208),
(319, 'burger', 55, 206),
(320, 'french fries', 100, 206),
(321, 'muskabun', 25, 206),
(322, 'peach mojito ', 180, 207),
(323, 'hazlenut coffee', 135, 207),
(324, 'kewi juice', 90, 207);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `quantity` int(11) NOT NULL,
  `Order_id` int(11) NOT NULL,
  `item_code` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`quantity`, `Order_id`, `item_code`) VALUES
(1, 12344, 301),
(2, 12345, 302),
(2, 12346, 303),
(4, 12347, 304),
(1, 12348, 305),
(2, 12349, 306),
(3, 12350, 307),
(1, 12351, 308),
(2, 12352, 309),
(8, 12353, 310),
(2, 12354, 311),
(13, 421442, 13455);

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE `order_details` (
  `Order_timestamp` varchar(255) NOT NULL,
  `Order_amount` int(11) NOT NULL,
  `Order_status` varchar(20) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `delivery_id` int(11) NOT NULL,
  `payment_id` int(11) NOT NULL,
  `Order_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_details`
--

INSERT INTO `order_details` (`Order_timestamp`, `Order_amount`, `Order_status`, `customer_id`, `delivery_id`, `payment_id`, `Order_id`) VALUES
('09:15:00', 2200, 'Ready', 102, 402, 502, 12345),
('11:25:00', 200, 'Preparing', 103, 403, 503, 12346),
('15:55:00', 1200, 'Delayed', 104, 404, 504, 12347),
('13:05:00', 2100, 'Preparing', 105, 405, 505, 12348),
('13:05:00', 500, 'Ready', 106, 406, 506, 12349),
('13:05:00', 2555, 'Preparing', 108, 408, 508, 12351),
('13:05:00', 2100, 'Preparing', 109, 409, 509, 12352),
('12:12:00', 1070, 'Preparing', 107, 407, 507, 12359);

-- --------------------------------------------------------

--
-- Table structure for table `payment_backup`
--

CREATE TABLE `payment_backup` (
  `Order_timestamp` varchar(225) DEFAULT NULL,
  `Order_amount` int(11) DEFAULT NULL,
  `Order_status` varchar(20) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `delivery_id` int(11) DEFAULT NULL,
  `payment_id` int(11) NOT NULL,
  `Order_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment_backup`
--

INSERT INTO `payment_backup` (`Order_timestamp`, `Order_amount`, `Order_status`, `customer_id`, `delivery_id`, `payment_id`, `Order_id`) VALUES
('07:33:77', 2950, 'Preparing', 101, 401, 501, 12344),
('09:15:00', 2200, 'Ready', 102, 402, 502, 12345),
('11:25:00', 200, 'Preparing', 103, 403, 503, 12346),
('15:55:00', 1200, 'Delayed', 104, 404, 504, 12347),
('13:05:00', 2100, 'Preparing', 105, 405, 505, 12348),
('13:05:00', 500, 'Ready', 106, 406, 506, 12349),
('12:12:00', 1070, 'Preparing', 107, 407, 507, 12359),
('13:05:00', 2555, 'Preparing', 108, 408, 508, 12351),
('13:05:00', 2100, 'Preparing', 109, 409, 509, 12352);

-- --------------------------------------------------------

--
-- Table structure for table `payment_details`
--

CREATE TABLE `payment_details` (
  `payment_id` int(11) NOT NULL,
  `payment_mode` varchar(15) NOT NULL,
  `payment_timestamp` varchar(255) NOT NULL,
  `tax` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment_details`
--

INSERT INTO `payment_details` (`payment_id`, `payment_mode`, `payment_timestamp`, `tax`) VALUES
(502, 'COD', '11:13:43', 20),
(503, 'CARD', '13:12:28', 20),
(504, 'COD', '15:12:03', 20),
(505, 'Online', '14:12:12', 20),
(506, 'COD', '01:13:13', 20),
(507, 'CARD', '09:08:48', 20),
(508, 'COD', '00:07:53', 20),
(509, 'Online', '17:17:37', 20),
(510, 'CARD', '19:19:22', 20),
(511, 'CARD', '10:30:00', 53);

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `ratings` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `restaurant_id` int(11) DEFAULT NULL,
  `rating_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rating`
--

INSERT INTO `rating` (`ratings`, `customer_id`, `restaurant_id`, `rating_id`) VALUES
(5, 103, 113, 1),
(4, 101, 114, 2),
(2, 102, 115, 3),
(4, 104, 116, 4),
(1, 105, 117, 5),
(3, 106, 118, 6),
(5, 107, 119, 7),
(5, 102, 119, 8),
(4, 103, 119, 9),
(2, 106, 119, 10),
(5, 101, 119, 11),
(1, 103, 119, 12),
(2, 108, 119, 13),
(4, 102, 119, 15),
(5, 104, 119, 16),
(2, 107, 119, 17);

-- --------------------------------------------------------

--
-- Table structure for table `restaurant`
--

CREATE TABLE `restaurant` (
  `restaurant_id` int(11) NOT NULL,
  `restaurant_name` varchar(20) NOT NULL,
  `restaurant_address` varchar(50) NOT NULL,
  `restaurant_password` varchar(16) NOT NULL,
  `restaurant_phoneno` varchar(10) NOT NULL,
  `Admin_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `restaurant`
--

INSERT INTO `restaurant` (`restaurant_id`, `restaurant_name`, `restaurant_address`, `restaurant_password`, `restaurant_phoneno`, `Admin_id`) VALUES
(111, 'Karavalli', 'Vivanta Bengaluru, 66, Residency Rd, Bengaluru, Ka', 'Kara@123', '8066604545', 1),
(112, 'Hatch Malleshwaram', '3rd Floor 30, 1st, Sampige Rd, Malleswara, Bengalu', 'Maha@123', '8762203148', 2),
(113, 'Spice Terrace', ' 24, JW Marriott Bengaluru, 1, Vittal Mallya Rd, A', 'Spice@123', '8067189999', 1),
(114, 'Yauatcha Mumbai', 'Raheja Tower, Bandra Kurla Complex, Bandra East, M', 'Yach@123', '9222222800', 2),
(115, 'Ummrao', 'C.T.S No 215 Andheri Kurla Road Andheri east, Mumb', 'Umm@123', '9773817937', 2),
(116, 'Masque', 'Masque, Unit G3, Shree Laxmi Woollen Mills, Shakti', 'Mas@123', '9819069222', 1),
(117, 'Tafri Baaz Cafe', ' Vikas Surya Plaza, G-70 & 78 Plot no-18, Sector 3', 'Tf@123', '8586858111', 1),
(118, 'Sorrento', 'Ground Level Shangri-La s - Eros Hotel, 19, Ashoka', 'Sor@123', '1141191040', 2),
(119, 'Varq', 'The Taj Mahal Hotel, No.1, Near, Man Singh Rd, Kha', 'Var@123', '1166566162', 1),
(120, 'AnalakshmiRestaurant', 'No 6 Mayor Ramanathan Salai, Spur Tank road, Chenn', 'Aka@123', '4428368333', 2),
(121, 'Grand Chola Hotel', '63, Anna Salai, Little Mount, Guindy, Chennai, Tam', 'Gra@123', '4222000011', 1),
(122, 'Rajwadu', 'Nr. Jivraj Tolnaka, Behind Ambaji Temple, Malav Ta', 'Raj@123', '7926643839', 2),
(123, 'Vishalla', 'Vasna Rd, Opp. Tol Naka, Rehnuma Society, Sanklit ', 'Vish@123', '8889323457', 1),
(124, 'Tomatos', 'Mardia Plaza, Ground Floor, 1, 2, 3, Chimanlal Gir', 'Toma@123', '7926461998', 1);

-- --------------------------------------------------------

--
-- Stand-in structure for view `user_details`
-- (See below for the actual view)
--
CREATE TABLE `user_details` (
`customer_id` int(11)
,`customer_firstname` varchar(30)
,`customer_lastname` varchar(30)
,`customer_phoneno` varchar(10)
,`order_amount` int(11)
,`payment_id` int(11)
,`tax` float
);

-- --------------------------------------------------------

--
-- Structure for view `user_details`
--
DROP TABLE IF EXISTS `user_details`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `user_details`  AS SELECT `customer`.`customer_id` AS `customer_id`, `customer`.`customer_firstname` AS `customer_firstname`, `customer`.`customer_lastname` AS `customer_lastname`, `customer`.`customer_phoneno` AS `customer_phoneno`, `order_details`.`Order_amount` AS `order_amount`, `payment_details`.`payment_id` AS `payment_id`, `payment_details`.`tax` AS `tax` FROM ((`customer` join `order_details` on(`customer`.`customer_id` = `order_details`.`customer_id`)) join `payment_details` on(`order_details`.`payment_id` = `payment_details`.`payment_id`))  ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Admin_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`category_id`),
  ADD KEY `resturant_id` (`resturant_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD KEY `Admin_id` (`Admin_id`);

--
-- Indexes for table `delivery_details`
--
ALTER TABLE `delivery_details`
  ADD PRIMARY KEY (`delivery_id`);

--
-- Indexes for table `menu_items`
--
ALTER TABLE `menu_items`
  ADD PRIMARY KEY (`item_code`),
  ADD KEY `category_id` (`category_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`Order_id`);

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`Order_id`),
  ADD KEY `delivery_id` (`delivery_id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `payment_id` (`payment_id`);

--
-- Indexes for table `payment_backup`
--
ALTER TABLE `payment_backup`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `payment_details`
--
ALTER TABLE `payment_details`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `rating`
--
ALTER TABLE `rating`
  ADD PRIMARY KEY (`rating_id`),
  ADD KEY `customer_id1` (`customer_id`),
  ADD KEY `restaurant_id1` (`restaurant_id`);

--
-- Indexes for table `restaurant`
--
ALTER TABLE `restaurant`
  ADD PRIMARY KEY (`restaurant_id`),
  ADD KEY `Admin_id1` (`Admin_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `category`
--
ALTER TABLE `category`
  ADD CONSTRAINT `resturant_id` FOREIGN KEY (`resturant_id`) REFERENCES `restaurant` (`restaurant_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `Admin_id` FOREIGN KEY (`Admin_id`) REFERENCES `admin` (`Admin_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `menu_items`
--
ALTER TABLE `menu_items`
  ADD CONSTRAINT `category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`category_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `order_details`
--
ALTER TABLE `order_details`
  ADD CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `delivery_id` FOREIGN KEY (`delivery_id`) REFERENCES `delivery_details` (`delivery_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `payment_id` FOREIGN KEY (`payment_id`) REFERENCES `payment_details` (`payment_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `rating`
--
ALTER TABLE `rating`
  ADD CONSTRAINT `customer_id1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `restaurant_id1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`restaurant_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `restaurant`
--
ALTER TABLE `restaurant`
  ADD CONSTRAINT `Admin_id1` FOREIGN KEY (`Admin_id`) REFERENCES `admin` (`Admin_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
