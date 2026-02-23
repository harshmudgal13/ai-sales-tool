import streamlit as st

def render_kpis(df, sales_col):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Value", f"{df[sales_col].sum():,.0f}")
    c2.metric("Average", f"{df[sales_col].mean():.2f}")
    c3.metric("Highest", f"{df[sales_col].max():,.2f}")
    c4.metric("Lowest", f"{df[sales_col].min():,.2f}")
