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
    st.markdown("<h2 style='font-style: bold;'>Medical Equation</h2>", unsafe_allow_html=True)
    st.markdown("### 📂 Upload & Select")
    a1, a2 = st.columns([3, 1])
    with a1:
        st.file_uploader("Upload Excel file", type=[".xlsx"])
    c1, c2 = st.columns(2)
    with c1:
        st.selectbox("Template Format", ['', 'Geoff', 'Marcus', 'Marisa'])

with col2:
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

    st.markdown("### 📍 Address")
    st.markdown("___")
    co1, co2, co3 = st.columns(3)
    with co1:
        rn = st.text_input("Recipient Name")
    with co2:
        sa = st.text_input("Street Address or P.O. Box")
    with co3:
        st.text_input("Secondary Address Line")

    ssubcol1, ssubcol2, ssubcol3 = st.columns(3)
    with ssubcol1:
        one = st.text_input("City")
    with ssubcol2:
        two = st.text_input("State Abbreviation")
    with ssubcol3:
        if "zip_code" not in st.session_state:
            st.session_state.zip_code = ""

        def format_zip():
            raw = st.session_state.zip_code_input
            if raw.isdigit():
                num = int(raw)
                if 501 <= num <= 99950:
                    st.session_state.zip_code = str(num).zfill(5)
                else:
                    st.session_state.zip_code = "Invalid"
            else:
                st.session_state.zip_code = "Invalid"

        st.text_input(
            "Zip Code",
            value=st.session_state.zip_code,
            key="zip_code_input",
            max_chars=5,
            on_change=format_zip
        )

    r1, r2, r3 = st.columns(3)
    with r1:
        country = st.text_input("Country")

    if st.button("Generate", key="green"):
        person_name = []
        address_info = []
        address_last_division = []
        has_error = False

        if honorific != "":
            person_name.append(honorific)
        else:
            st.error("Please select an Honorific.")
            has_error = True

        if fname.strip() != "":
            person_name.append(fname.strip())
        else:
            st.error("First Name is required.")
            has_error = True

        if mname.strip() != "":
            person_name.append(mname.strip())  # optional

        if lname.strip() != "":
            person_name.append(lname.strip())
        else:
            st.error("Last Name is required.")
            has_error = True

        if rn.strip() != "":
            address_info.append(rn.strip())
        else:
            st.error("Recipient name is required.")
            has_error = True

        if sa.strip() != "":
            address_info.append(sa.strip())
        else:
            st.error("Street Address or P.O. Box is required.")
            has_error = True

        if one.strip() != "":
            address_last_division.append(one.strip())
        else:
            st.error("City is required.")
            has_error = True

        if two.strip() != "":
            address_last_division.append(two.strip())
        else:
            st.error("State Abbreviation is required.")
            has_error = True

        if st.session_state.zip_code not in ["", "Invalid"]:
            address_last_division.append(st.session_state.zip_code)
        else:
            st.error("Enter a valid ZIP Code.")
            has_error = True

        if country.strip() == "":
            st.error("Country is required.")
            has_error = True

        if not has_error:
            st.success("✅ Your form has been successfully generated!")

            if address_last_division:
                address_info.append(", ".join(address_last_division))
            print("#######################",address_info)
            # Display collected information
            st.markdown("### 📝 Submitted Information")
            st.markdown("#### Personal Details")
            st.write(f"{' '.join(person_name)}")

            st.markdown("#### Address")
            st.write(f"{rn}")
            st.write(f"{sa}")
            st.write(f"{', '.join(address_last_division)}")
            st.write(f"{country}")
