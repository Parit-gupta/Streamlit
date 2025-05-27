import streamlit as st
import pathlib

# Set page configuration to wide layout
st.set_page_config(layout="wide")

# Function to load and inject custom CSS file
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("style.css")  # Path to CSS file
load_css(css_path)

# Create two columns with comfortable width ratios
col1, col2 = st.columns([1.8, 3.2])

with col1:
    # Title and file upload section
    st.markdown("<h2 style='font-style: bold;'>Medical Equation</h2>", unsafe_allow_html=True)
    st.markdown("### 📂 Upload & Select")
    a1,a2 = st.columns([3,1])
    with a1:
        st.file_uploader("Upload Excel file", type=[".xlsx"])

    # Two sub-columns to hold dropdown or other widgets
    c1, c2 = st.columns(2)
    with c1:
        st.selectbox("Template Format", ['', 'Geoff', 'Marcus', 'Marisa'])

with col2:
    # Personal Information section with sub-columns for inputs
    st.markdown("### 🙋 Personal Information")
    subcol1, subcol2, subcol3, subcol4 = st.columns([1.5, 2.5, 2.5, 2.5])
    with subcol1:
        honorific = st.selectbox("Honorific", ["", "Mr.", "Mrs.", "Ms.", "Dr.", "Prof."])
    with subcol2:
        fname = st.text_input("First Name")
    with subcol3:
        mname = st.text_input("Middle Name")
    with subcol4:
        lname = st.text_input("Last Name")

    # Address section inputs
    st.markdown("### 📍 Address")
    st.markdown("___")
    co1,co2,co3 = st.columns(3)
    with co1:
        rn = st.text_input("Recipient Name")
    with co2:
        sa = st.text_input("Street Address or P.O. Box")
    with co3:
        st.text_input("Secondary Address Line")

    # Sub-columns for city, state, ZIP
    ssubcol1, ssubcol2, ssubcol3 = st.columns(3)
    with ssubcol1:
        one = st.text_input("City")
    with ssubcol2:
        two = st.text_input("State Abbreviation")
    with ssubcol3:
        three = st.number_input("ZIP Code",100000,999999,100000)

    r1,r2,r3 = st.columns(3)
    with r1:
        country = st.text_input("Country")

    # Generate button with required field validation
    if st.button("Generate", key="green"):
        if honorific == "":
            st.error("Please select an Honorific.")
        elif fname.strip() == "":
            st.error("First Name is required.")
        elif lname.strip() == "":
            st.error("Last Name is required.")
        elif rn.strip() == "":
            st.error("Recipient name is required.")
        elif sa.strip() == "":
            st.error("Street Address or P.O. Box is required.")
        elif one.strip() == "":
            st.error("City is required.")
        elif two.strip() == "":
            st.error("State Abbreviation is required.")
        elif three == 0:
            st.error("Enter a valid ZIP Code.")
        else:
            st.success("✅ Your form has been successfully generated!")

