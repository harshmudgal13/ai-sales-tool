import streamlit as st

def open_card(title, icon="🧠"):
    st.markdown(f"""
    <div style="
        background: linear-gradient(145deg,#020617,#020617);
        border:1px solid rgba(99,102,241,0.25);
        padding:20px;
        border-radius:14px;
        margin-top:15px;
        box-shadow:0 0 12px rgba(99,102,241,0.15);
    ">
        <h4 style="margin-bottom:15px;">{icon} {title}</h4>
    """, unsafe_allow_html=True)


def close_card():
    st.markdown("</div>", unsafe_allow_html=True)
