import streamlit as st
import pandas as pd

name = st.text_input("Enter Your First Name : ")
Fname = st.text_input("Enter Your Father Name : ")
address = st.text_area("Enter Your Address : ")
classdata = st.selectbox("Enter class :", (1,2,3))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name: {name}
    FAther Name: {Fname}
    Address: {address}
    class : {classdata}""")