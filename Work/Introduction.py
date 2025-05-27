import streamlit as st

# Introduction

st.title("Hello All")  # title of the page is written using this
st.subheader("My first app") # act as a sub title with bold font
st.write("What is your faviourite language ?? ") # writing a text in normal size
choose = st.selectbox("Choose from this: ",['','Hindi','English','Tamil','Rajasthani'])  #used for making drop down menu 
st.write(f"You chose {choose}")  # here we write the language we choosed using f string format
st.success("Congrats on choosing your fav language")  # used for creatinng or showing acceptance of sth.






