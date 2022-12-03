import pandas as pd
import streamlit as st
from database import *

def update_delivery_details():
    result = view_delivery_details()
    # st.write(result)
    df = pd.DataFrame(result, columns=['delivery_id','delivery_address','delivery_status'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[0] for i in view_delivery_id()]
    # st.write(list_of_ids)
    selected_id = st.selectbox("IDs to Edit", list_of_ids)
    selected_result = get_status_delivery_details(selected_id)
    # st.write(selected_result)
    if selected_result:
        delivery_id = selected_result[0][0]
        delivery_address = selected_result[0][1]
        delivery_status = selected_result[0][2]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_delivery_id = st.text_input("delivery ID:", delivery_id)
            new_delivery_address = st.text_input("delivery Address:", delivery_address)
            new_delivery_status = st.selectbox("delivery_Status", ["Delivered","Preparing","Picked-up"])
        if st.button("Update Data"):
            edit_delivery_details(new_delivery_id,new_delivery_address,new_delivery_status, delivery_id,delivery_address,delivery_status)
            st.success("Successfully updated {} to {}".format(delivery_id, new_delivery_id))

    result2 = view_delivery_details()
    df2 = pd.DataFrame(result2, columns=['delivery_id', 'delivery_address', 'delivery_status'])
    with st.expander("Updated Data"):
        st.dataframe(df2)

def update_admin():
    result = view_admin()
    df = pd.DataFrame(result, columns=['Admin_id','Admin_name','Admin_password'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[0] for i in view_admin_id()]
    # st.write(list_of_ids)

    selected_id = st.selectbox("IDs to Edit", list_of_ids)                                  
    selected_result = get_status_admin(selected_id)
    # st.write(selected_result)
    if selected_result:
        # st.write("entered if")
        Admin_id = selected_result[0][0]
        Admin_name = selected_result[0][1]
        Admin_password = selected_result[0][2]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_Admin_id = st.text_input("admin ID:", Admin_id)
            new_Admin_name = st.text_input("admin Name:", Admin_name)
            new_Admin_password = st.text_input("admin_Password:", Admin_password)
        if st.button("Update Data"):
            edit_admin(new_Admin_id,new_Admin_name,new_Admin_password, Admin_id,Admin_name,Admin_password)
            st.success("Successfully updated {} to {}".format(Admin_id, new_Admin_id))

    result2 = view_admin()
    df2 = pd.DataFrame(result2, columns=['Admin_id', 'Admin_name', 'Admin_password'])
    with st.expander("Updated Data"):
        st.dataframe(df2)

        
def update_category():
    result = view_category()
    df = pd.DataFrame(result, columns=['category_id','category_name','restaurant_id'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[0] for i in view_category_id()]
    selected_id = st.selectbox("IDs to Edit", list_of_ids)
    selected_result = get_status_category(selected_id)
    # st.write(selected_result)
    if selected_result:
        category_id = selected_result[0][0]
        category_name = selected_result[0][1]
        restaurant_id = selected_result[0][2]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_category_id = st.text_input("category ID:", category_id)
            new_category_name = st.text_input("category Name:", category_name)
            new_restaurant_id = st.text_input("restaurant ID:", restaurant_id)
        if st.button("Update Data"):
            edit_category(new_category_id,new_category_name,new_restaurant_id, category_id,category_name,restaurant_id)
            st.success("Successfully updated {} to {}".format(category_id, new_category_id))

    result2 = view_category()
    df2 = pd.DataFrame(result2, columns=['category_id', 'category_name','restaurant_id'])
    with st.expander("Updated Data"):
        st.dataframe(df2)



def update_customer():
    result = view_customer()
    df = pd.DataFrame(result, columns=['customer_id','customer_firstname','customer_lastname','customer_password','customer_phoneno','customer_address','customer_email','Admin_id'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[0] for i in view_customer_id()]
    selected_id = st.selectbox("IDs to Edit", list_of_ids)
    selected_result = get_status_customer(selected_id)
    # st.write(selected_result)
    if selected_result:
        customer_id = selected_result[0][0]
        customer_firstname = selected_result[0][1]
        customer_lastname = selected_result[0][2]
        customer_password = selected_result[0][3]
        customer_phoneno = selected_result[0][4]
        customer_address = selected_result[0][5]
        customer_email = selected_result[0][6]
        Admin_id = selected_result[0][7]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_customer_id = st.text_input("customer ID:", customer_id)
            new_customer_firstname = st.text_input("customer Firstname:", customer_firstname)
            new_customer_lastname = st.text_input("customer Lastname:", customer_lastname)
            new_customer_password = st.text_input("customer Password:", customer_password)
        with col2:
            new_customer_phoneno = st.text_input("customer Phoneno:", customer_phoneno)
            new_customer_address = st.text_input("customer Address:", customer_address)
            new_customer_email = st.text_input("customer Email:", customer_email)
            new_Admin_id = st.text_input("Admin ID:", Admin_id)
                       
        if st.button("Update Data"):
            edit_customer(new_customer_id,new_customer_firstname,new_customer_lastname,new_customer_password,new_customer_phoneno,new_customer_address,new_customer_email,new_Admin_id, customer_id,customer_firstname,customer_lastname,customer_password,customer_phoneno,customer_address,customer_email,Admin_id)
            st.success("Successfully updated {} to {}".format(customer_id, new_customer_id))

    result2 = view_customer()
    df2 = pd.DataFrame(result2, columns=['customer_id', 'customer_firstname','customer_lastname','customer_password','customer_phoneno','customer_address','customer_email','Admin_id'])
    with st.expander("Updated Data"):
        st.dataframe(df2)

def update_menu_items():
    result = view_menu_items()
    df = pd.DataFrame(result, columns=['menu_id','menu_name','menu_price','menu_category_id'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[0] for i in view_menu_items_id()]
    selected_id = st.selectbox("IDs to Edit", list_of_ids)
    selected_result = get_status_menu_items(selected_id)
    # st.write(selected_result)
    if selected_result:
        menu_id = selected_result[0][0]
        menu_name = selected_result[0][1]
        menu_price = selected_result[0][2]
        menu_category_id = selected_result[0][3]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_menu_id = st.text_input("menu ID:", menu_id)
            new_menu_name = st.text_input("menu Name:", menu_name)
            new_menu_price = st.text_input("menu_price:", menu_price)
            new_menu_category_id = st.text_input("menu_category_id:", menu_category_id)
        if st.button("Update Data"):
            edit_menu_items(new_menu_id,new_menu_name,new_menu_price,new_menu_category_id, menu_id,menu_name,menu_price,menu_category_id)
            st.success("Successfully updated {} to {}".format(menu_id, new_menu_id))

    result2 = view_menu_items()
    df2 = pd.DataFrame(result2, columns=['menu_id', 'menu_name', 'menu_price', 'menu_category_id'])
    with st.expander("Updated Data"):
        st.dataframe(df2)


def update_order():
    result = view_orders()
    df = pd.DataFrame(result, columns=['quantity','order_id','item_code'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[1] for i in view_order_id()]
    selected_id = st.selectbox("IDs to Edit", list_of_ids)
    selected_result = get_status_orders(selected_id)
    # st.write(selected_result)
    if selected_result:
        quantity = selected_result[0][0]
        order_id = selected_result[0][1]
        item_code = selected_result[0][2]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_quantity = st.text_input("quantity:", quantity)
            new_order_id = st.text_input("order_id:", order_id)
            new_item_code = st.text_input("item_code:", item_code)
        if st.button("Update Data"):
            edit_orders(new_quantity,new_order_id,new_item_code, quantity,order_id,item_code)
            st.success("Successfully updated {} to {}".format(order_id, new_order_id))

    result2 = view_orders()
    df2 = pd.DataFrame(result2, columns=['quantity','order_id','item_code'])
    with st.expander("Updated Data"):
        st.dataframe(df2)

def update_order_details():
    
    result = view_order_details()
    df = pd.DataFrame(result, columns=['order_timestamp','order_amount','order_status','customer_id','delivery_id','payment_id','order_id'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[4] for i in view_order_details_id()]
    selected_id = st.selectbox("IDs to Edit", list_of_ids)
    selected_result = get_status_order_details(selected_id)
    # st.write(selected_result)
    if selected_result:
        order_timestamp = selected_result[0][0]
        order_amount = selected_result[0][1]
        order_status = selected_result[0][2]
        customer_id = selected_result[0][3]
        delivery_id = selected_result[0][4]
        payment_id = selected_result[0][5]
        order_id = selected_result[0][6]


        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_order_timestamp = st.text_input("order_timestamp:", order_timestamp)
            new_order_amount = st.text_input("order_amount:", order_amount)
            new_order_status = st.text_input("order_status:", order_status)
            new_customer_id = st.text_input("customer_id:", customer_id)
            new_delivery_id = st.text_input("delivery_id:", delivery_id)
            new_payment_id = st.text_input("payment_id:", payment_id)
            new_order_id = st.text_input("order_id:", order_id)

        if st.button("Update Data"):
            edit_order_details(new_order_timestamp,new_order_amount,new_order_status,new_customer_id,new_delivery_id,new_payment_id,new_order_id, order_timestamp,order_amount,order_status,customer_id,delivery_id,payment_id,order_id)
            st.success("Successfully updated {} to {}".format(order_id, new_order_id))

    result2 = view_order_details()
    df2 = pd.DataFrame(result2, columns=['order_timestamp','order_amount','order_status','customer_id','delivery_id','payment_id','order_id'])
    with st.expander("Updated Data"):
        st.dataframe(df2)

def update_payment_details():
        
    result = view_payment_details()
    df = pd.DataFrame(result, columns=['payment_id','payment_date','payment_amount','payment_type','order_id'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[0] for i in view_payment_details_id()]
    selected_id = st.selectbox("IDs to Edit", list_of_ids)
    selected_result = get_status_payment_details(selected_id)
    # st.write(selected_result)
    if selected_result:
        payment_id = selected_result[0][0]
        payment_date = selected_result[0][1]
        payment_amount = selected_result[0][2]
        payment_type = selected_result[0][3]
        order_id = selected_result[0][4]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_payment_id = st.text_input("payment ID:", payment_id)
            new_payment_date = st.text_input("payment Date:", payment_date)
            new_payment_amount = st.text_input("payment Amount:", payment_amount)
            new_payment_type = st.selectbox("payment_Type", ["Cash","Card"])
            new_order_id = st.text_input("order ID:", order_id)
        if st.button("Update Data"):
            edit_payment_details(new_payment_id,new_payment_date,new_payment_amount,new_payment_type,new_order_id, payment_id,payment_date,payment_amount,payment_type,order_id)
            st.success("Successfully updated {} to {}".format(payment_id, new_payment_id))

    result2 = view_payment_details()
    df2 = pd.DataFrame(result2, columns=['payment_id', 'payment_date', 'payment_amount','payment_type','order_id'])
    with st.expander("Updated Data"):
        st.dataframe(df2)


def update_rating():
            
    result = view_rating()
    df = pd.DataFrame(result, columns=['rating_id','rating','customer_id','product_id'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[3] for i in view_rating_id()]
    selected_id = st.selectbox("IDs to Edit", list_of_ids)
    selected_result = get_status_rating(selected_id)
    # st.write(selected_result)
    if selected_result:
        rating_id = selected_result[0][0]
        rating = selected_result[0][1]
        customer_id = selected_result[0][2]
        product_id = selected_result[0][3]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_rating_id = st.text_input("rating ID:", rating_id)
            new_rating = st.text_input("rating:", rating)
            new_customer_id = st.text_input("customer ID:", customer_id)
            new_product_id = st.text_input("product ID:", product_id)
        if st.button("Update Data"):
            edit_rating(new_rating_id,new_rating,new_customer_id,new_product_id, rating_id,rating,customer_id,product_id)
            st.success("Successfully updated {} to {}".format(rating_id, new_rating_id))

    result2 = view_rating()
    df2 = pd.DataFrame(result2, columns=['rating_id', 'rating', 'customer_id','product_id'])
    with st.expander("Updated Data"):
        st.dataframe(df2)


def update_restaurant():
                
    result = view_restaurant()
    df = pd.DataFrame(result, columns=['restaurant_id','restaurant_name','restaurant_address','restaurant_phone','restaurant_email','restaurant_password'])
    with st.expander("Current IDs"):
        st.dataframe(df)
    list_of_ids = [i[0] for i in view_restaurant_id()]
    selected_id = st.selectbox("IDs to Edit", list_of_ids)
    selected_result = get_status_restaurant(selected_id)
    # st.write(selected_result)
    if selected_result:
        restaurant_id = selected_result[0][0]
        restaurant_name = selected_result[0][1]
        restaurant_address = selected_result[0][2]
        restaurant_phone = selected_result[0][3]
        restaurant_email = selected_result[0][4]
        restaurant_password = selected_result[0][5]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_restaurant_id = st.text_input("restaurant ID:", restaurant_id)
            new_restaurant_name = st.text_input("restaurant Name:", restaurant_name)
            new_restaurant_address = st.text_input("restaurant Address:", restaurant_address)
            new_restaurant_phone = st.text_input("restaurant Phone:", restaurant_phone)
            new_restaurant_email = st.text_input("restaurant Email:", restaurant_email)
            new_restaurant_password = st.text_input("restaurant Password:", restaurant_password)
        if st.button("Update Data"):
            edit_restaurant(new_restaurant_id,new_restaurant_name,new_restaurant_address,new_restaurant_phone,new_restaurant_email,new_restaurant_password, restaurant_id,restaurant_name,restaurant_address,restaurant_phone,restaurant_email,restaurant_password)
            st.success("Successfully updated {} to {}".format(restaurant_id, new_restaurant_id))

    result2 = view_restaurant()
    df2 = pd.DataFrame(result2, columns=['restaurant_id', 'restaurant_name', 'restaurant_address','restaurant_phone','restaurant_email','restaurant_password'])
    with st.expander("Updated Data"):
        st.dataframe(df2)