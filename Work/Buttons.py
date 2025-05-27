import streamlit as st

st.title("How would you rate working in StatusNeo ?? ")

st.write("Working Experience ")
exp = st.radio("Choose",['Excelent','Good','Normal','Poor','Average'])
if exp=='Poor' or exp=='Average':
    input = st.text_input("Tell us what was bad from our side ")
    if input:
        st.success("Your review has been stored")

st.write("Environment")
exp = st.multiselect("Choose your experience:", ['Excellent', 'Good', 'Normal', 'Poor', 'Average'])
if 'Poor' in exp or 'Average' in exp:
    feedback = st.text_area("Write your feedback here")
    if feedback:
        st.success("Your review has been stored")


st.write("Rating")
overall=st.selectbox("Tell your overall experience: ",[1,2,3,4,5])
if overall:
    a = st.text_input("Any feedback ")
    if a.upper() == 'Y':
        st.text_input("Enter your feedback ") 

if st.button("Submit"):
    st.success("Your feedback is recived")