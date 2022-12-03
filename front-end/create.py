import streamlit as st
from database import *


def create_delivery_details():
    col1, col2 = st.columns(2)
    with col1:
        delivery_id = st.text_input("Delivery id:")
        delivery_address = st.text_input("delivery_address:")
        delivery_status = st.selectbox("delivery_status", ["Delivered","Preparing","Picked-up"])
    
    if st.button("Add Data"):
        add_data_delivery_details(delivery_id,delivery_address,delivery_status)
        st.success("Successfully added Delivery_id: {}".format(delivery_id))
        
         
def create_admin():
    col1, col2 = st.columns(2)
    with col1:
        admin_id = st.text_input("Admin id:")
        admin_name = st.text_input("admin name:")
        admin_password = st.text_input("admin password:")
    
    if st.button("Add Data"):
        add_data_admin(admin_id,admin_name,admin_password)
        st.success("Successfully added Admin: {}".format(admin_id))

def create_category():
    col1, col2 = st.columns(2)
    with col1:
        category_id = st.text_input("Category id:")
        category_name = st.text_input("category name:")
        restaurant_id = st.text_input("restaurant id:")
    
    if st.button("Add Data"):
        add_data_category(category_id,category_name,restaurant_id)
        st.success("Successfully added Category: {}".format(category_name))

def create_customer():
    col1, col2 = st.columns(2)
    with col1:
        customer_id = st.text_input("Customer id:")
        customer_firstname = st.text_input("customer_firstname:")
        customer_lastname = st.text_input("customer_lastname:")
        customer_password = st.text_input("customer_password:")
    with col2:
        customer_phoneno = st.text_input("customer_phoneno:")
        customer_address = st.text_input("customer_address:")
        customer_email = st.text_input("customer_email:")
        Admin_id = st.text_input("Admin_id:")

    if st.button("Add Data"):
        add_data_customer(customer_id,customer_firstname,customer_lastname,customer_password,customer_phoneno,customer_address,customer_email,Admin_id)
        st.success("Successfully added Customer: {}".format(customer_id))

def create_menu_items():
    col1, col2 = st.columns(2)
    with col1:
        item_code = st.text_input("item_code:")
        item_name = st.text_input("item_name:")
        price = st.text_input("price:")
        category_id = st.text_input("category_id:")    
    if st.button("Add Data"):
        add_data_menu_items(item_code,item_name,price,category_id)
        st.success("Successfully added Menu item: {}".format(item_name))

def create_orders():
    col1, col2 = st.columns(2)
    with col1:
        quantity = st.text_input("quantity:")
        Order_id = st.text_input("order id:")
        item_code = st.text_input("order code:")
    if st.button("Add Data"):
        add_data_orders(quantity,Order_id,item_code)
        st.success("Successfully added Order: {}".format(Order_id))

def create_order_details():
    col1, col2 = st.columns(2)
    with col1:
        Order_timestamp	 = st.text_input("order timestamp:")
        Order_amount = st.text_input("order amount:")
        Order_status = st.text_input("order status:")
        customer_id= st.text_input("customer id:")
        delivery_id = st.text_input("delivery id:")
        payment_id  = st.text_input("payment id:")
        Order_id  = st.text_input("order id:")

    if st.button("Add Data"):
        add_data_order_details(Order_timestamp,Order_amount,Order_status,customer_id,delivery_id,payment_id,Order_id)
        st.success("Successfully added Order: {}".format(delivery_id))

def create_payment_details():
    col1, col2 = st.columns(2)
    with col1:
        payment_id = st.text_input("payment id:")
        payment_mode = st.text_input("payment mode:")
        payment_timestamp = st.text_input("payment timestamp:")
        tax = st.text_input("tax:")
    if st.button("Add Data"):
        add_data_payment_details(payment_id,payment_mode,payment_timestamp,tax)
        st.success("Successfully added Payment: {}".format(payment_id))

def create_rating():
    col1, col2 = st.columns(2)
    with col1:
        ratings = st.text_input("rating:")
        customer_id = st.text_input("customer id:")
        restaurant_id = st.text_input("restaurant id:")
        rating_id = st.text_input("rating id:")
    if st.button("Add Data"):
        add_data_rating(ratings,customer_id,restaurant_id,rating_id)
        st.success("Successfully added Rating: {}".format(ratings))

def create_restaurant():
    col1, col2 = st.columns(2)
    with col1:
        restaurant_id = st.text_input("restaurant id:")
        restaurant_name = st.text_input("restaurant name:")
        restaurant_address = st.text_input("restaurant address:")
        restaurant_password = st.text_input("restaurant password:")
        restaurant_phoneno = st.text_input("restaurant phoneno:")
        Admin_id = st.text_input("Admin id:")
    if st.button("Add Data"):
        add_data_restaurant(restaurant_id,restaurant_name,restaurant_address,restaurant_password,restaurant_phoneno,Admin_id)
        st.success("Successfully added Restaurant: {}".format(restaurant_id))