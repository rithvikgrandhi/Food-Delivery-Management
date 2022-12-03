-- get customer_id, Order_amount, delivery_status
SELECT order_details.order_id, order_details.Order_amount,delivery_details.delivery_status
FROM order_details
JOIN delivery_details
ON order_details.delivery_id = delivery_details.delivery_id;


--get names and addresses of all restaurants with 5 star rating

SELECT restaurant.restaurant_name, restaurant.restaurant_address
FROM restaurant
JOIN rating
ON restaurant.restaurant_id = rating.restaurant_id
WHERE rating.ratings = 5;

--get all the dishes in north_indian and south_indian categories

SELECT menu_items.item_name,category.category_name
FROM menu_items
JOIN category
ON menu_items.category_id = category.category_id
WHERE category.category_name = 'NORTH-INDIAN' OR category.category_name = 'SOUTH-INDIAN';

-- get names of customers who gave a 4 and above rating to a restaurant

SELECT customer.customer_firstname, customer.customer_lastname, rating.ratings
FROM customer
JOIN rating
ON customer.customer_id = rating.customer_id
WHERE rating.ratings >= 4;


--aggregate functions

1) SELECT COUNT(Order_id) FROM order_details WHERE Order_amount>1000;

2) SELECT category_id,avg(Price) FROM menu_items GROUP BY category_id;

3) select payment_mode, COUNT(payment_mode) AS MOST_FREQUENT from payment_details GROUP BY payment_mode ORDER BY COUNT(payment_mode) DESC;

4) SELECT sum(order_amount) FROM order_details;

5) SELECT customer_id, COUNT(customer_id) AS MOST_FREQUENT from order_details GROUP BY customer_id ORDER BY COUNT(customer_id) DESC;


--set operations

1) SELECT restaurant_id,ratings FROM rating WHERE rating.ratings = 5 UNION SELECT restaurant_id,ratings FROM rating WHERE rating.ratings = 3;

2) select customer_id from customer except select customer_id from rating;

3) select * from delivery_details except select * from delivery_details where delivery_status = 'Delivered'

4) select * from order_details except select * from order_details where order_amount > 1000;

-- --functions
-- --set a random admin for each new customer
-- CREATE FUNCTION random_admin()
-- RETURNS VARCHAR(20)
-- BEGIN
-- DECLARE admin int;
-- SET admin = (SELECT admin_id FROM admin WHERE admin_id = FLOOR(1 + RAND()*2));

-- RETURN admin;
-- END;



-- --procedure
-- delimiter $$
-- Create Procedure UpdateAdmin (cust_id int)
-- begin 
-- update customer set admin_id= FLOOR(RAND()+1) where customer.customer_id=cust_id;
-- END$$
-- DELIMITER ;

-- -- -- procedure extra
-- -- delimiter $$
-- -- create procedure add_tax(in delivery_id int,in Order_amount int)
-- -- begin
-- -- declare new_tax float;
-- -- set new_tax=0.18*Order_amount;
-- -- update order_details set tax=new_tax where delivery_id=delivery_id;
-- -- end$$
-- -- delimiter ;

-- -- --procedure for choosing a random admin
delimiter $$
create procedure random_admin(in customer_id int)
begin
declare admin int;
set admin = FLOOR(1 + RAND()*2);
update customer set admin_id=admin where customer_id=customer.customer_id;
end$$


-- --trigger
-- delimiter $$
-- create trigger add_tax
-- after insert on order_details
-- for each row
-- begin
-- update payment_details
-- set tax = 0.18*order_details.order_amount;
-- end$$
-- delimiter ;


-- --try 2
-- CREATE TRIGGER add_tax2
--     BEFORE UPDATE  Order_amount ON order_details
--     FOR EACH ROW
-- BEGIN
--    UPDATE payment_details pd
--    set pd.tax = order_details.Order_amount*0.18
--    WHERE pd.payment_id = order_details.payment_id;
-- END;


delimiter //
create procedure random_admin(in customer_id int)
begin
declare admin int;
set admin = FLOOR(1 + RAND()*2);
set admin_id = admin where customer.customer_id = customer_id;
END //  
DELIMITER ;

--procedure

-- delimiter $$
-- create procedure random_admin(in customer_id int)
-- begin
-- declare admin int;
-- set admin = FLOOR(1 + RAND()*2);
-- update customer set admin_id=admin where customer_id=customer_id;
-- end$$
-- delimiter ;

-- --trigger

-- delimiter $$
-- create trigger add_tax
-- after insert on order_details
-- for each row
-- begin
-- update payment_details
-- set tax = 0.18*order_details.order_amount;
-- end$$
-- delimiter ;

-- --trigger to add data to payment details when order_details is updated

-- delimiter $$
-- create trigger add_tax2
-- after update on order_details
-- for each row
-- begin
-- update payment_details
-- set tax = 0.18*order_details.order_amount;
-- end$$
-- delimiter ;

delimiter $$
CREATE TRIGGER phone_warn BEFORE INSERT
ON customer
FOR EACH ROW
BEGIN
IF NEW.customer_phoneno <1000000000 or NEW.customer_phoneno>9999999999
THEN 
signal sqlstate '45000' set message_text = 'Invalid phone number';
END IF;
END; $$
delimiter ;



--procedure

DELIMITER $$
CREATE PROCEDURE south_indian()
BEGIN
    select * from menu_items
    where category_id = 201;
END$$
DELIMITER ;

--

DELIMITER $$
CREATE PROCEDURE north_indian()
BEGIN
    select * from menu_items
    where category_id = 202;
END$$
DELIMITER ;

--

DELIMITER $$
CREATE PROCEDURE chinese()
BEGIN
    select * from menu_items
    where category_id = 204;
END$$
DELIMITER ;

--

DELIMITER $$
CREATE PROCEDURE italian()
BEGIN
    select * from menu_items
    where category_id = 203;
END$$
DELIMITER ;

--

DELIMITER $$
CREATE PROCEDURE desserts()
BEGIN
    select * from menu_items
    where category_id = 208;
END$$
DELIMITER ;

--

DELIMITER $$
CREATE PROCEDURE beverages()
BEGIN
    select * from menu_items
    where category_id = 207;
END$$
DELIMITER ;




--function try 5
-- DELIMITER $$
-- CREATE FUNCTION rating1(C_ID int) 
-- RETURNS VARCHAR(20)
-- DETERMINISTIC
-- BEGIN
--     DECLARE customerLevel VARCHAR(20);
--     DECLARE credit float;
--     SELECT sum(O.O_Amount) INTO credit
--     FROM ORDERS AS O
--     WHERE O.C_ID = C_ID
--     GROUP BY O.C_ID;


--     IF credit > 25000 THEN
--         SET customerLevel = 'PLATINUM';
--     ELSEIF (credit >= 21000 AND 
--             credit <= 25000) THEN
--         SET customerLevel = 'GOLD';
--     ELSEIF credit < 20000 THEN
--         SET customerLevel = 'SILVER';
--     ELSE
--         SET customerLevel = 'BRONZE';
--     END IF;
--     -- Return the customer level
--     RETURN (customerLevel);
-- END$$
-- DELIMITER ;



--view

CREATE VIEW user_details AS
SELECT customer.customer_id,customer.customer_firstname,customer.customer_lastname,customer.customer_phoneno,order_details.order_amount,payment_details.payment_id,payment_details.tax
FROM customer
join order_details
on customer.customer_id=order_details.customer_id
join payment_details
on order_details.payment_id=payment_details.payment_id;



--cursor to update tax in payment details after ta

DELIMITER $$
CREATE PROCEDURE update_tax(in taxper int)
BEGIN
DECLARE done INT DEFAULT 0;
DECLARE delivery_id INT;
DECLARE tax float;
DECLARE cur1 CURSOR FOR SELECT delivery_id FROM order_details;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
OPEN cur1;
read_loop: LOOP
FETCH cur1 INTO delivery_id;
IF done THEN
LEAVE read_loop;
END IF;
set tax=taxper*order_details.order_amount;
update payment_details set tax=tax where order_details.payment_id=payment_details.payment_id;
END LOOP;
CLOSE cur1;
END$$
DELIMITER ;


--cursor to update tax in payment details after taking order_amount from order_details

-- DELIMITER $$
-- CREATE PROCEDURE update_tax(in taxper int)
-- BEGIN
-- DECLARE done INT DEFAULT 0;
-- DECLARE delivery_id INT;
-- DECLARE tax1 float;
-- DECLARE mul int;
-- DECLARE value cursor for select order_amount from order_details;
-- DECLARE cur1 CURSOR FOR SELECT delivery_id FROM order_details;
-- DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
-- OPEN cur1;
-- OPEN value;
-- read_loop: LOOP
-- FETCH cur1 INTO delivery_id;
-- FETCH value INTO mul;
-- IF done THEN
-- LEAVE read_loop;
-- END IF;
-- set tax1=taxper*mul*0.01;
-- UPDATE order_details,payment_details SET tax = tax1 WHERE order_details.payment_id = payment_details.payment_id;
-- END LOOP;
-- CLOSE cur1;
-- CLOSE value;
-- END$$
-- DELIMITER;




update payment_details set tax=tax1 from order_details, payment_details on order_details.payment_id=payment_details.payment_id;



CREATE VIEW tax_stuff as 
select 


--create cursor to calculate tax and show it along with order_amount

-- DELIMITER $$
-- CREATE PROCEDURE update_tax(in taxper int)
-- BEGIN
-- DECLARE done INT DEFAULT 0;
-- DECLARE delivery_id INT;
-- DECLARE tax1 float;
-- DECLARE mul int;
-- DECLARE value cursor for select order_amount from order_details;
-- DECLARE cur1 CURSOR FOR SELECT delivery_id FROM order_details;
-- DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
-- OPEN cur1;
-- OPEN value;
-- read_loop: LOOP
-- FETCH cur1 INTO delivery_id;
-- FETCH value INTO mul;
-- IF done THEN
-- LEAVE read_loop;
-- END IF;
-- set tax1=taxper*mul*0.01;
-- UPDATE order_details,payment_details SET tax = tax1 WHERE order_details.payment_id = payment_details.payment_id;
-- END LOOP;
-- CLOSE cur1;
-- CLOSE value;
-- END$$
-- DELIMITER;


--try 100

-- DELIMITER //
-- CREATE PROCEDURE update_tax()
--    BEGIN
--       DECLARE done INT DEFAULT 0;
--       DECLARE tax,p_id int;
--       DECLARE cur CURSOR FOR SELECT order_amount,payment_id FROM order_details;
--       DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
--       OPEN cur;
--       label: LOOP
--       FETCH cur INTO p_id,tax;
--       UPDATE payment_details
--       SET tax = cur*0.18
--       WHERE payment_details.payment_id = p_id;
--       IF done = 1 THEN LEAVE label;
--       END IF;
--       END LOOP;
--       CLOSE cur;
--    END//
-- DELIMITER ;

Order_timestamp,Order_amount,Order_status,customer_id,delivery_id,payment_id,Order_id	

create table payment_backup(Order_timestamp varchar(225),Order_amount int,Order_status varchar(20),customer_id int,delivery_id int,payment_id int,Order_id int,PRIMARY KEY (payment_id))

DELIMITER //
CREATE PROCEDURE backup()
   BEGIN
      DECLARE done INT DEFAULT 0;
      DECLARE Order_timestamp,Order_amount,Order_status,customer_id,delivery_id,payment_id,Order_id VARCHAR(30);
      DECLARE cur CURSOR FOR SELECT * FROM payment_details;
      DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
      OPEN cur;
      label: LOOP
      FETCH cur INTO Order_timestamp,Order_amount,Order_status,customer_id,delivery_id,payment_id,Order_id	;
      INSERT INTO student_backup VALUES(Order_timestamp,Order_amount,Order_status,customer_id,delivery_id,payment_id,Order_id);
      IF done = 1 THEN LEAVE label;
      END IF;
      END LOOP;
      CLOSE cur;
   END//
DELIMITER ;



--function

DELIMITER //
CREATE FUNCTION check_strength(Admin_password varchar(16))
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
DECLARE STRENGTH VARCHAR(20);
IF LENGTH(Admin_password) >= 8 THEN
SET STRENGTH = 'STRONG';
ELSEIF LENGTH(Admin_password) < 8 THEN
SET STRENGTH = 'WEAK';
END IF;
RETURN (STRENGTH);
END; //
DELIMITER ;

select Admin_id, Admin_name, check_strength(Admin_password) from admin;




--concat

DELIMITER $$
CREATE or replace PROCEDURE fullname (IN cus_id INT, INOUT fullList varchar(4000))
BEGIN
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
DELIMITER ;

SET @fullList = "";

CALL fullname(101, @fullList);

SELECT @fullList;


--pi chart

# Graph (Pie Chart in Sidebar)
df_target = df[['id', 'target']].groupby('target').count() / len(df)
fig_target = go.Figure(data=[go.Pie(labels=df_target.index,
                                    values=df_target['id'],
                                    hole=.3)])
fig_target.update_layout(showlegend=False,height=200,margin={'l': 20, 'r': 60, 't': 0, 'b': 0})
fig_target.update_traces(textposition='inside', textinfo='label+percent')

# Layout (Sidebar)
st.markdown("## Settings")
cat_selected = st.selectbox('Categorical Variables', vars_cat)
cont_selected = st.selectbox('Continuous Variables', vars_cont)
cont_multi_selected = st.multiselect('Correlation Matrix', vars_cont,
                                     default=vars_cont)
st.markdown("## Target Variables")
st.plotly_chart(fig_target, use_container_width=True)



--- 
import matplotlib.pyplot as plt
import numpy as np
df = pd.DataFrame(result, columns=['delivery_id','delivery_address','delivery_status'])
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 
