import streamlit as st
from create import *
from database import *
from delete import *
from read import *
from update import *

def main():
    st.title("Food Delivery")
    menu = ["query","admin","category","customer","delivery details","menu items","orders","order_details","payment details","rating","restaurant"]
    menu2 = ["Add", "View", "Edit", "Delete"]
    choice = st.sidebar.selectbox("Table", menu)
    choice2 = st.sidebar.radio("CRUD", menu2)
    
    query=""

    if choice == "query":
        st.subheader("Query")
        query = st.text_area("Enter Query")
        if st.button("Execute"):
            c.execute(query)
            result=c.fetchall()
            st.success("Query Executed")
            st.write(result)

    elif choice == "delivery details":
        if choice2=="Add":
            create_delivery_details()
        elif choice2=="View":
            read_delivery_details()
        elif choice2=="Edit":
            update_delivery_details()
        elif choice2=="Delete":
            delete_delivery_details()

    elif choice == "admin":
        if choice2=="Add":
            create_admin()
        elif choice2=="View":
            read_admin()
        elif choice2=="Edit":
            update_admin()
        elif choice2=="Delete":
            delete_admin()

    elif choice == "category":
        if choice2=="Add":
            create_customer()
        elif choice2=="View":
            read_customer()
        elif choice2=="Edit":
            update_customer()
        elif choice2=="Delete":
            delete_customer()

    elif choice == "customer":
        if choice2=="Add":
            create_customer()
        elif choice2=="View":
            read_customer()
        elif choice2=="Edit":
            update_customer()
        elif choice2=="Delete":
            delete_customer()

    elif choice == "menu items":
        if choice2=="Add":
            create_menu_items()
        elif choice2=="View":
            read_menu_items()
        elif choice2=="Edit":
            update_menu_items()
        elif choice2=="Delete":
            delete_menu_items()

    elif choice == "orders":
        if choice2=="Add":
            create_orders()
        elif choice2=="View":
            read_orders()
        elif choice2=="Edit":
            update_order()
        elif choice2=="Delete":
            delete_orders()

    elif choice == "order_details":
        if choice2=="Add":
            create_order_details()
        elif choice2=="View":
            read_order_details()
        elif choice2=="Edit":
            update_order_details()
        elif choice2=="Delete":
            delete_order_details()

    elif choice == "payment details":
        if choice2=="Add":
            create_payment_details()
        elif choice2=="View":
            read_payment_details()
        elif choice2=="Edit":
            update_payment_details()
        elif choice2=="Delete":
            delete_payment_details()

    elif choice == "rating":
        if choice2=="Add":
            create_rating()
        elif choice2=="View":
            read_rating()
        elif choice2=="Edit":
            update_rating()
        elif choice2=="Delete":
            delete_rating()

    elif choice == "restaurant":
        if choice2=="Add":
            create_restaurant()
        elif choice2=="View":
            read_restaurant()
        elif choice2=="Edit":
            update_restaurant()
        elif choice2=="Delete":
            delete_restaurant()

if __name__ == '__main__':
    main()