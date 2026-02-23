import streamlit as st

def open_card(title=None, icon="📊"):

    st.markdown(f"""
    <div style="
        background:#020617;
        border:1px solid #1f2937;
        border-radius:14px;
        padding:18px;
        margin-bottom:18px;
        box-shadow:0 0 20px rgba(99,102,241,0.08);
    ">
    <h4 style="margin-top:0;">{icon} {title if title else ""}</h4>
    """, unsafe_allow_html=True)

def close_card():
    st.markdown("</div>", unsafe_allow_html=True)
