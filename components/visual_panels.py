import streamlit as st
import plotly.express as px
import pandas as pd

def show_visual_panels(df, sales_col):

    # -------------------------------------------------
    # 🚀 HARD SAFETY NORMALIZATION
    # -------------------------------------------------
    df = df.copy()
    df = df.reset_index(drop=True)

    # Prevent MultiIndex crash
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ["_".join(map(str,col)).strip() for col in df.columns]

    # Performance limit
    df = df.head(2000)

    st.markdown("## 🧭 Executive Intelligence Dashboard")

    # ==================================================
    # PRIMARY ROW
    # ==================================================

    c1,c2 = st.columns(2)

    with c1:
        fig1 = px.line(
            df,
            y=sales_col,
            template="plotly_dark"
        )
        fig1.update_layout(height=350)
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        fig2 = px.histogram(
            df,
            x=sales_col,
            template="plotly_dark"
        )
        fig2.update_layout(height=350)
        st.plotly_chart(fig2, use_container_width=True)

    # ==================================================
    # SECOND ROW
    # ==================================================

    c3,c4 = st.columns(2)

    with c3:
        fig3 = px.box(
            df,
            y=sales_col,
            template="plotly_dark"
        )
        fig3.update_layout(height=350)
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        fig4 = px.scatter(
            df,
            y=sales_col,
            template="plotly_dark"
        )
        fig4.update_layout(height=350)
        st.plotly_chart(fig4, use_container_width=True)
