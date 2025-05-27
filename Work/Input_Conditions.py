import streamlit as st

# Using if loop 

# st.title("Conditionals")

# name = st.text_input("Enter your name ")

# if name:
#     st.write(f"Welcome {name} !")

# choose = st.text_input("Do you want to do total of your marks ?? ")
# if choose.upper == 'Y':
   
#     maths = st.slider("Your maths marks",0,20,10)
#     st.write(f"Your maths marks are {maths}")

#     physics = st.slider("Your physics marks",0,20,10)
#     st.write(f"Your physics marks are {physics}")
  
#     chemistry = st.slider("Your chemistry marks",0,20,10)
#     st.write(f"Your chemistry marks are {chemistry}")

#     sum = maths+physics+chemistry
#     if sum>=90:
#         grade = 'A'
#     elif sum>=80 and sum <90 :
#         grade = 'B'
#     elif sum>=70 and sum <80 :
#         grade = 'C'
#     elif sum>=60 and sum <70 :
#         grade = 'D'
#     else:
#         grade = 'E'

#     st.write(f"Your total marks are {sum}")
#     st.write(f"Your grade is **{grade}**")
#     st.success("Your grade has been seen by you")


# Using for loop



st.title("Conditionals with Loop")

name = st.text_input("Enter your name")

if name:
    st.write(f"Welcome {name}!")

date = st.date_input("Enter the date you were born ")

if date:
    st.write(f"Yuor selected date is {date}")

choose = st.text_input("Do you want to do total of your marks? (Y/N)")

if choose.upper() == 'Y':
    subjects = ["Maths", "Physics", "Chemistry"]
    marks = {}

    st.write("Enter your marks:")

    # Loop through each subject
    for i in subjects:
        marks[i] = st.slider(f"{i} marks", 0, 20, 10)
        st.write(f"Your {i.lower()} marks are {marks[i]}")

    total_marks = sum(marks.values())

    # Grade logic
    if total_marks >= 90:
        grade = 'A'
    elif total_marks >= 80:
        grade = 'B'
    elif total_marks >= 70:
        grade = 'C'
    elif total_marks >= 60:
        grade = 'D'
    else:
        grade = 'E'

    st.write(f"Your total marks are {total_marks}")
    st.write(f"Your grade is **{grade}**")
    st.success("Your grade has been seen by you")
