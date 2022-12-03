import pandas as pd
import streamlit as st
from database import *


def delete_delivery_details():
    result = view_delivery_details()
    df = pd.DataFrame(result, columns=['delivery_id','delivery_address', 'delivery_status'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_ids = [i[0] for i in view_delivery_id()]
    selected_id = st.selectbox("id to Delete", list_of_ids)
    st.warning("Do you want to delete {}?".format(selected_id))
    if st.button("Delete ID"):
        delete_delivery_id(selected_id)
        st.success("ID has been deleted successfully")
    new_result = view_delivery_details()
    df2 = pd.DataFrame(new_result, columns=['delivery_id','delivery_address','delivery_status'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_admin():
    result = view_admin()
    df = pd.DataFrame(result, columns=['admin_id','admin_name','admin_password'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_ids = [i[0] for i in view_admin_id()]
    selected_id = st.selectbox("id to Delete", list_of_ids)
    st.warning("Do you want to delete {}?".format(selected_id))
    if st.button("Delete ID"):
        delete_admin_id(selected_id)
        st.success("ID has been deleted successfully")
    new_result = view_admin()
    df2 = pd.DataFrame(new_result, columns=['admin_id','admin_name','admin_password'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_category():

    result = view_category()
    df = pd.DataFrame(result, columns=['category_id','category_name','restaurant_id'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_ids = [i[0] for i in view_category_id()]
    selected_id = st.selectbox("id to Delete", list_of_ids)
    st.warning("Do you want to delete {}?".format(selected_id))
    if st.button("Delete ID"):
        delete_category_id(selected_id)
        st.success("ID has been deleted successfully")
    new_result = view_category()
    df2 = pd.DataFrame(new_result, columns=['category_id','category_name','restaurant_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_customer():

    result = view_customer()
    df = pd.DataFrame(result, columns=['customer_id','customer_firstname','customer_lastname','customer_password','customer_phoneno','customer_address','customer_email','Admin_id'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_ids = [i[0] for i in view_customer_id()]
    selected_id = st.selectbox("id to Delete", list_of_ids)
    st.warning("Do you want to delete {}?".format(selected_id))
    if st.button("Delete ID"):
        delete_customer_id(selected_id)
        st.success("ID has been deleted successfully")
    new_result = view_customer()
    df2 = pd.DataFrame(new_result, columns=['customer_id','customer_firstname','customer_lastname','customer_password','customer_phoneno','customer_address','customer_email','Admin_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_restaurant():
    
    result = view_restaurant()
    df = pd.DataFrame(result, columns=['restaurant_id','restaurant_name','restaurant_address','restaurant_phoneno','restaurant_email'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_ids = [i[0] for i in view_restaurant_id()]
    selected_id = st.selectbox("id to Delete", list_of_ids)
    st.warning("Do you want to delete {}?".format(selected_id))
    if st.button("Delete ID"):
        delete_restaurant_id(selected_id)
        st.success("ID has been deleted successfully")
    new_result = view_restaurant()
    df2 = pd.DataFrame(new_result, columns=['restaurant_id','restaurant_name','restaurant_address','restaurant_phoneno','restaurant_email'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_menu_items():

    result = view_menu_items()
    df = pd.DataFrame(result, columns=['item_code','item_name','Price','category_id'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_ids = [i[0] for i in view_menu_items_id()]
    selected_id = st.selectbox("id to Delete", list_of_ids)
    st.warning("Do you want to delete {}?".format(selected_id))
    if st.button("Delete ID"):
        delete_menu_items_id(selected_id)
        st.success("ID has been deleted successfully")
    new_result = view_menu_items()
    df2 = pd.DataFrame(new_result, columns=['item_code','item_name','Price','category_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_orders():

    result = view_orders()
    df = pd.DataFrame(result, columns=['quantity','Order_id','item_code'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_ids = [i[0] for i in view_order_id()]
    selected_id = st.selectbox("id to Delete", list_of_ids)
    st.warning("Do you want to delete {}?".format(selected_id))
    if st.button("Delete ID"):
        delete_orders_id(selected_id)
        st.success("ID has been deleted successfully")
    new_result = view_orders()
    df2 = pd.DataFrame(new_result, columns=['quantity','Order_id','item_code'])
    with st.expander("Updated data"):
        st.dataframe(df2)   


def delete_order_details():
    
        result = view_order_details()
        df = pd.DataFrame(result, columns=['order_timestamp','order_amount','order_status','customer_id','delivery_id','payment_id','order_id'])
        with st.expander("Current Data present"):
            st.dataframe(df)
    
        list_of_ids = [i[4] for i in view_order_details_id()]
        selected_id = st.selectbox("id to Delete", list_of_ids)
        st.warning("Do you want to delete {}?".format(selected_id))
        if st.button("Delete ID"):
            delete_order_details_id(selected_id)
            st.success("ID has been deleted successfully")
        new_result = view_order_details()
        df2 = pd.DataFrame(new_result, columns=['order_timestamp','order_amount','order_status','customer_id','delivery_id','payment_id','order_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)

def delete_payment_details():
    
        result = view_payment_details()
        df = pd.DataFrame(result, columns=['payment_id','payment_mode','payment_timestamp','tax'])
        with st.expander("Current Data present"):
            st.dataframe(df)
    
        list_of_ids = [i[0] for i in view_payment_id()]
        selected_id = st.selectbox("id to Delete", list_of_ids)
        st.warning("Do you want to delete {}?".format(selected_id))
        if st.button("Delete ID"):
            delete_payment_details_id(selected_id)
            st.success("ID has been deleted successfully")
        new_result = view_payment_details()
        df2 = pd.DataFrame(new_result, columns=['payment_id','payment_mode','payment_timestamp','tax'])
        with st.expander("Updated data"):
            st.dataframe(df2)


def delete_rating():
        
            result = view_rating()
            df = pd.DataFrame(result, columns=['ratings','customer_id','restaurant_id','rating_id'])
            with st.expander("Current Data present"):
                st.dataframe(df)
        
            list_of_ids = [i[3] for i in view_rating_id()]
            selected_id = st.selectbox("id to Delete", list_of_ids)
            st.warning("Do you want to delete {}?".format(selected_id))
            if st.button("Delete ID"):
                delete_rating_id(selected_id)
                st.success("ID has been deleted successfully")
            new_result = view_rating()
            df2 = pd.DataFrame(new_result, columns=['ratings','customer_id','restaurant_id','rating_id'])
            with st.expander("Updated data"):
                st.dataframe(df2)


def delete_restaurant():
        
        result = view_restaurant()
        df = pd.DataFrame(result, columns=['restaurant_id','restaurant_name','restaurant_address','restaurant_password','restaurant_phoneno','Admin_id'])
        with st.expander("Current Data present"):
            st.dataframe(df)
    
        list_of_ids = [i[0] for i in view_restaurant_id()]
        selected_id = st.selectbox("id to Delete", list_of_ids)
        st.warning("Do you want to delete {}?".format(selected_id))
        if st.button("Delete ID"):
            delete_restaurant_id(selected_id)
            st.success("ID has been deleted successfully")
        new_result = view_restaurant()
        df2 = pd.DataFrame(new_result, columns=['restaurant_id','restaurant_name','restaurant_address','restaurant_password','restaurant_phoneno','Admin_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)