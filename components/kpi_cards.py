import streamlit as st

def show_kpis(df, sales_col):

    total = df[sales_col].sum()
    avg = df[sales_col].mean()
    mx = df[sales_col].max()
    mn = df[sales_col].min()

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Total Value", f"{total:,.0f}")
    c2.metric("Average", f"{avg:,.2f}")
    c3.metric("Highest", f"{mx:,.2f}")
    c4.metric("Lowest", f"{mn:,.2f}")
