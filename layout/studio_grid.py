import streamlit as st

def studio_two_by_two():

    top_left, top_right = st.columns(2)
    bottom_left, bottom_right = st.columns(2)

    return top_left, top_right, bottom_left, bottom_right
