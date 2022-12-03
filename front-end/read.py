import pandas as pd
import streamlit as st
from database import *
import plotly.express as px


def read_delivery_details():
    result = view_delivery_details()
    # st.write(result)
    df = pd.DataFrame(result, columns=['delivery_id','delivery_address','delivery_status'])
    with st.expander("View all IDs"):
        st.dataframe(df)
    with st.expander("delivery status"):
        task_df = df['delivery_status'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names='index', values='delivery_status')
        st.plotly_chart(p1)


def read_admin():
    result = view_admin()
    # st.write(result)
    df = pd.DataFrame(result, columns=['admin_id','admin_name','admin_password'])
    with st.expander("View all IDs"):
        st.dataframe(df)

def read_category():
    result = view_category()
    # st.write(result)
    df = pd.DataFrame(result, columns=['category_id','category_name','restaurant_id'])
    with st.expander("View all IDs"):
        st.dataframe(df)

def read_customer():
    result = view_customer()
    # st.write(result)
    df = pd.DataFrame(result, columns=['customer_id','customer_firstname','customer_lastname','customer_password','customer_phoneno','customer_address','customer_email','Admin_id'])
    with st.expander("View all IDs"):
        st.dataframe(df)

def read_menu_items():
    result = view_menu_items()
    # st.write(result)
    df = pd.DataFrame(result, columns=['item_code','item_name','Price','category_id'])
    with st.expander("View all IDs"):
        st.dataframe(df)

def read_orders():
    result = view_orders()
    # st.write(result)
    df = pd.DataFrame(result, columns=['quantity','Order_id','item_code'])
    with st.expander("View all IDs"):
        st.dataframe(df)

def read_order_details():
    result = view_order_details()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Order_timestamp','Order_amount','Order_status','customer_id','delivery_id','payment_id','Order_id'])
    with st.expander("View all IDs"):
        st.dataframe(df)

def read_payment_details():
    result = view_payment_details()
    # st.write(result)
    df = pd.DataFrame(result, columns=['payment_id','payment_mode','payment_timestamp','tax'])
    with st.expander("View all IDs"):
        st.dataframe(df)

def read_rating():
    result = view_rating()

    # st.write(result)
    df = pd.DataFrame(result, columns=['ratings','customer_id','restaurant_id','rating_id'])
    with st.expander("View all IDs"):
        st.dataframe(df)

def read_restaurant():
    result = view_restaurant()
    # st.write(result)
    df = pd.DataFrame(result, columns=['restaurant_id','restaurant_name','restaurant_address','restaurant_password','restaurant_phoneno','Admin_id'])
    with st.expander("View all IDs"):
        st.dataframe(df)