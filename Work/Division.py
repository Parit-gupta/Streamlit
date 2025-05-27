import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 3])

with col1:
    st.write("Rate us:")
    rating = st.selectbox("Rating", [1, 2, 3, 4, 5])

with col2:
    feedback = st.text_area("Write your feedback here")

if feedback:
    st.success("Thank you for your feedback!")
