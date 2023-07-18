
import streamlit as st
from main_def import main_def

st.image("iti.jpg")
st.header("Get your Attendance")

page = 0

def main():

    global page

    if st.button("Get your Attendance"):
        page = 1
    if st.button("Stop"):
        page = 2
    if page == 1:
        main_def()
    elif page == 2:
        st.title("Already Remarked!!!!!!")

if __name__ == "__main__":
    main()







