import streamlit as st

def load_theme():

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(180deg,#020617,#020617,#020617);
        color:white;
    }

    div[data-testid="metric-container"] {
        background: rgba(15,23,42,0.6);
        border: 1px solid rgba(99,102,241,0.4);
        padding: 20px;
        border-radius: 14px;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 12px rgba(99,102,241,0.15);
    }

    section[data-testid="stSidebar"] {
        background:#020617;
        border-right:1px solid rgba(99,102,241,0.3);
    }

    </style>
    """, unsafe_allow_html=True)
