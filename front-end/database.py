# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="food_delivery_management"
)
c = mydb.cursor()
   

##############################################################################
##############################################################################
##############################################################################
##############################################################################

#                               ADD DATA
    
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################


def add_data_delivery_details(delivery_id,delivery_address,delivery_status):
    c.execute('INSERT INTO delivery_details VALUES (%s,%s,%s)',(delivery_id,delivery_address,delivery_status))
    mydb.commit()

def add_data_admin(admin_id,admin_name,admin_password):
    c.execute('INSERT INTO admin VALUES (%s,%s,%s)',(admin_id,admin_name,admin_password))
    mydb.commit()

def add_data_category(category_id,category_name,restaurant_id):
    c.execute('INSERT INTO category VALUES (%s,%s,%s)',(category_id,category_name,restaurant_id))
    mydb.commit()
    
def add_data_customer(customer_id, customer_firstname,customer_lastname,customer_password,customer_phoneno,customer_address,customer_email,Admin_id):
    c.execute('INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(customer_id, customer_firstname,customer_lastname,customer_password,customer_phoneno,customer_address,customer_email,Admin_id))
    mydb.commit()

def add_data_menu_items(item_code,item_name,price,category_id):
    c.execute('INSERT INTO menu_items VALUES (%s,%s,%s,%s)',(item_code,item_name,price,category_id))
    mydb.commit()

def add_data_orders(quantity,order_id,item_code):
    c.execute('INSERT INTO orders VALUES (%s,%s,%s)',(quantity,order_id,item_code))
    mydb.commit()

def add_data_order_details(order_timestamp,order_amount,order_status,customer_id,delivery_id,payment_id,order_id):
    c.execute('INSERT INTO order_details VALUES (%s,%s,%s,%s,%s,%s,%s)',(order_timestamp,order_amount,order_status,customer_id,delivery_id,payment_id,order_id))
    mydb.commit()

def add_data_payment_details(payment_id,payment_mode,payment_timestamp,tax):
    c.execute('INSERT INTO payment_details VALUES (%s,%s,%s,%s)',(payment_id,payment_mode,payment_timestamp,tax))
    mydb.commit()

def add_data_rating(ratings,customer_id,restaurant_id,rating_id):
    c.execute('INSERT INTO rating VALUES (%s,%s,%s,%s)',(ratings,customer_id,restaurant_id,rating_id))
    mydb.commit()

def add_data_restaurant(restaurant_id,restaurant_name,restaurant_address,restaunrant_password,restaurant_phoneno,admin_id):
    c.execute('INSERT INTO restaurant VALUES (%s,%s,%s,%s,%s,%s)',(restaurant_id,restaurant_name,restaurant_address,restaunrant_password,restaurant_phoneno,admin_id))
    mydb.commit()

##############################################################################
##############################################################################
##############################################################################
##############################################################################

#                               GET STATUS
    
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################



def get_status_admin(admin_id):
    c.execute('SELECT * FROM admin WHERE admin_id="{}"'.format(admin_id))
    data = c.fetchall()
    return data

def get_status_category(category_id):
    c.execute('SELECT * FROM category WHERE category_id="{}"'.format(category_id))
    data = c.fetchall()
    return data

def get_status_customer(customer_id):
    c.execute('SELECT * FROM customer WHERE customer_id="{}"'.format(customer_id))
    data = c.fetchall()
    return data

def get_status_delivery_details(delivery_id):
    c.execute('SELECT * FROM delivery_details WHERE delivery_id="{}"'.format(delivery_id))
    data = c.fetchall()
    return data

def get_status_menu_items(item_code):
    c.execute('SELECT * FROM menu_items WHERE item_code="{}"'.format(item_code))
    data = c.fetchall()
    return data

def get_status_orders(order_id):
    c.execute('SELECT * FROM orders WHERE order_id="{}"'.format(order_id))
    data = c.fetchall()
    return data

def get_status_order_details(delivery_id):
    c.execute('SELECT * FROM order_details WHERE order_id="{}"'.format(delivery_id))
    data = c.fetchall()
    return data

def get_status_payment_details(payment_id):
    c.execute('SELECT * FROM payment_details WHERE payment_id="{}"'.format(payment_id))
    data = c.fetchall()
    return data

def get_status_rating(rating_id):
    c.execute('SELECT * FROM rating WHERE restaurant_id="{}"'.format(rating_id))
    data = c.fetchall()
    return data

def get_status_restaurant(restaurant_id):
    c.execute('SELECT * FROM restaurant WHERE restaurant_id="{}"'.format(restaurant_id))
    data = c.fetchall()
    return data




##############################################################################
##############################################################################
##############################################################################
##############################################################################

#                               EDIT TABLES
    
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################

def edit_delivery_details(new_delivery_id,new_delivery_address,new_delivery_status, delivery_id,delivery_address,delivery_status):
    c.execute("UPDATE delivery_details SET delivery_id=%s, delivery_address=%s, delivery_status=%s WHERE delivery_id=%s and delivery_address=%s and delivery_status=%s", (new_delivery_id,new_delivery_address,new_delivery_status, delivery_id,delivery_address,delivery_status))
    mydb.commit()
    data = c.fetchmany()
    return data

def edit_admin(new_admin_id,new_admin_name,new_admin_password, admin_id,admin_name,admin_password):
    c.execute("UPDATE admin SET admin_id=%s, admin_name=%s, admin_password=%s WHERE admin_id=%s and admin_name=%s and admin_password=%s", (new_admin_id,new_admin_name,new_admin_password, admin_id,admin_name,admin_password))
    mydb.commit()
    data = c.fetchmany()
    return data

def edit_category(new_category_id,new_category_name,new_restaurant_id, category_id,category_name,restaurant_id):
    c.execute("UPDATE category SET category_id=%s, category_name=%s,restaurant_id=%s WHERE category_id=%s and category_name=%s and restaurant_id=%s", (new_category_id,new_category_name,new_restaurant_id, category_id,category_name,restaurant_id))
    mydb.commit()
    data = c.fetchmany()
    return data

def edit_customer(new_customer_id,new_customer_firstname,new_customer_lastname,new_customer_password,new_customer_phoneno,new_customer_address,new_customer_email,new_admin_id, customer_id,customer_firstname,customer_lastname,customer_password,customer_phoneno,customer_address,customer_email,admin_id):
    c.execute("UPDATE customer SET customer_id=%s, customer_firstname=%s, customer_lastname=%s, customer_password=%s, customer_phoneno=%s, customer_address=%s, customer_email=%s, admin_id=%s WHERE customer_id=%s and customer_firstname=%s and customer_lastname=%s and customer_password=%s and customer_phoneno=%s and customer_address=%s and customer_email=%s and admin_id=%s", (new_customer_id,new_customer_firstname,new_customer_lastname,new_customer_password,new_customer_phoneno,new_customer_address,new_customer_email,new_admin_id, customer_id,customer_firstname,customer_lastname,customer_password,customer_phoneno,customer_address,customer_email,admin_id))
    mydb.commit()
    data = c.fetchmany()
    return data


def  edit_menu_items(new_item_code,new_item_name,new_price,new_category_id, item_code,item_name,price,category_id):
    c.execute("UPDATE menu_items SET item_code=%s, item_name=%s, price=%s, category_id=%s WHERE item_code=%s and item_name=%s and price=%s and category_id=%s", (new_item_code,new_item_name,new_price,new_category_id, item_code,item_name,price,category_id))
    mydb.commit()
    data = c.fetchmany()
    return data

def edit_orders(new_quantitiy,new_order_id,new_item_code,quantity,order_id,item_code):
    c.execute("UPDATE orders SET quantity=%s, order_id=%s, item_code=%s WHERE quantity=%s and order_id=%s and item_code=%s", (new_quantitiy,new_order_id,new_item_code,quantity,order_id,item_code))
    mydb.commit()
    data = c.fetchmany()
    return data

def edit_order_details(new_order_timestamp,new_order_amount,new_order_status,new_customer_id,new_delivery_id,new_payment_id,new_order_id,order_timestamp,order_amount,order_status,customer_id,delivery_id,payment_id,order_id):
    c.execute("UPDATE order_details SET order_timestamp=%s, order_amount=%s, order_status=%s, customer_id=%s, delivery_id=%s, payment_id=%s WHERE order_timestamp=%s and order_amount=%s and order_status=%s and customer_id=%s and delivery_id=%s and payment_id=%s and order_id=%s", (new_order_timestamp,new_order_amount,new_order_status,new_customer_id,new_delivery_id,new_payment_id,new_order_id,order_timestamp,order_amount,order_status,customer_id,delivery_id,payment_id,order_id))
    mydb.commit()
    data = c.fetchmany()
    return data

def edit_payment_details(new_payment_id,new_payment_mode,new_payment_timestamp,new_tax,payment_id,payment_mode,payment_timestamp,tax):
    c.execute("UPDATE payment_details SET payment_id=%s, payment_mode=%s, payment_timestamp=%s, tax=%s WHERE payment_id=%s and payment_mode=%s and payment_timestamp=%s and tax=%s", (new_payment_id,new_payment_mode,new_payment_timestamp,new_tax,payment_id,payment_mode,payment_timestamp,tax))
    mydb.commit()
    data = c.fetchmany()
    return data

def edit_rating(new_ratings,new_customer_id,new_restaurant_id,new_rating_id, ratings,customer_id,restaurant_id,rating_id):
    c.execute("UPDATE rating SET ratings=%s, customer_id=%s, restaurant_id=%s WHERE ratings=%s and customer_id=%s and restaurant_id=%s and rating_id=%s", (new_ratings,new_customer_id,new_restaurant_id,new_rating_id, ratings,customer_id,restaurant_id,rating_id))
    mydb.commit()
    data = c.fetchmany()
    return data

def edit_restaurant(new_restaurant_id,new_restaurant_name,new_restaurant_address,new_restaurant_password,new_restaurant_phonenno,new_admin_id, restaurant_id,restaurant_name,restaurant_address,restaurant_password,restaurant_phonenno,admin_id):
    c.execute("UPDATE restaurant SET restaurant_id=%s, restaurant_name=%s, restaurant_address=%s, restaurant_password=%s, restaurant_phonenno=%s, admin_id=%s WHERE restaurant_id=%s and restaurant_name=%s and restaurant_address=%s and restaurant_password=%s and restaurant_phonenno=%s and admin_id=%s", (new_restaurant_id,new_restaurant_name,new_restaurant_address,new_restaurant_password,new_restaurant_phonenno,new_admin_id, restaurant_id,restaurant_name,restaurant_address,restaurant_password,restaurant_phonenno,admin_id))
    mydb.commit()
    data = c.fetchmany()
    return data


##############################################################################
##############################################################################
##############################################################################
##############################################################################

#                               DELETE TABLES
    
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################

#view tables

def view_delivery_id():
    c.execute('SELECT * FROM delivery_details')
    data = c.fetchall()
    return data

def view_payment_details_id():
    c.execute('SELECT * FROM payment_details')
    data = c.fetchall()
    return data

def view_admin_id():
    c.execute('SELECT * FROM admin')
    data = c.fetchall()
    return data

def view_category_id():
    c.execute('SELECT * FROM category')
    data = c.fetchall()
    return data

def view_customer_id():
    c.execute('SELECT * FROM customer')
    data = c.fetchall()
    return data

def view_restaurant_id():
    c.execute('SELECT * FROM restaurant')
    data = c.fetchall()
    return data

def view_menu_items_id():
    c.execute('SELECT * FROM menu_items')
    data = c.fetchall()
    return data

def view_order_id():
    c.execute('SELECT * FROM orders')
    data = c.fetchall()
    return data

def view_payment_id():
    c.execute('SELECT * FROM payment_details')
    data = c.fetchall()
    return data

def view_rating_id():
    c.execute('SELECT * FROM rating')
    data = c.fetchall()
    return data

def view_order_details_id():
    c.execute('SELECT * FROM order_details')
    data = c.fetchall()
    return data


#acutal deleting

def delete_delivery_id(delivery_id):
    c.execute('DELETE FROM delivery_details WHERE delivery_id="{}"'.format(delivery_id))
    mydb.commit()

def delete_admin_id(Admin_id):
    c.execute('DELETE FROM admin WHERE admin_id="{}"'.format(Admin_id))
    mydb.commit()

def delete_category_id(category_id):
    c.execute('DELETE FROM category WHERE category_id="{}"'.format(category_id))
    mydb.commit()

def delete_customer_id(customer_id):
    c.execute('DELETE FROM customer WHERE customer_id="{}"'.format(customer_id))
    mydb.commit()

def delete_menu_items_id(item_code):
    c.execute('DELETE FROM menu_items WHERE item_code="{}"'.format(item_code))
    mydb.commit()

def delete_orders_id(Order_id):
    c.execute('DELETE FROM orders WHERE order_id="{}"'.format(Order_id))
    mydb.commit()

def delete_order_details_id(delivery_id):
    c.execute('DELETE FROM order_details WHERE delivery_id="{}"'.format(delivery_id))
    mydb.commit()

def delete_payment_details_id(payment_id):
    c.execute('DELETE FROM payment_details WHERE payment_id="{}"'.format(payment_id))
    mydb.commit()

def delete_rating_id(rating_id):
    c.execute('DELETE FROM rating WHERE rating_id="{}"'.format(rating_id))
    mydb.commit()

def delete_restaurant_id(restaurant_id):
    c.execute('DELETE FROM restaurant WHERE restaurant_id="{}"'.format(restaurant_id))
    mydb.commit()


    
    

##############################################################################
##############################################################################
##############################################################################
##############################################################################

#                               VIEW TABLES
    
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################

def view_delivery_details():
    c.execute('SELECT * FROM delivery_details')
    data = c.fetchall()
    return data

def view_admin():
    c.execute('SELECT * FROM admin')
    data = c.fetchall()
    return data

def view_category():
    c.execute('SELECT * FROM category')
    data = c.fetchall()
    return data

def view_customer():
    c.execute('SELECT * FROM customer')
    data = c.fetchall()
    return data

def view_menu_items():
    c.execute('SELECT * FROM menu_items')
    data = c.fetchall()
    return data

def view_orders():
    c.execute('SELECT * FROM orders')
    data = c.fetchall()
    return data

def view_order_details():
    c.execute('SELECT * FROM order_details')
    data = c.fetchall()
    return data

def view_payment_details():
    c.execute('SELECT * FROM payment_details')
    data = c.fetchall()
    return data

def view_rating():
    c.execute('SELECT * FROM rating')
    data = c.fetchall()
    return data

def view_restaurant():
    c.execute('SELECT * FROM restaurant')
    data = c.fetchall()
    return data