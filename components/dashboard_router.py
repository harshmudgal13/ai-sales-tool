from panels.intelligence_panel import render_intelligence
from panels.breakdown_panel import render_breakdown
from panels.kpi_panel import render_kpis
import streamlit as st


def route_dashboard(mode, df, sales_col):

    # 🚀 REVENUE MODE
    if mode == "Revenue Intelligence":
        st.markdown("## 🚀 Revenue Intelligence Mode")
        render_intelligence(df, sales_col)
        st.divider()
        render_breakdown(df, sales_col)

    # 📈 GROWTH MODE
    elif mode == "Growth Signals":
        st.markdown("## 📈 Growth Signals Mode")
        render_breakdown(df, sales_col)

    # 🧠 EXECUTIVE MODE
    else:
        st.markdown("## 🧠 Executive Command Center")
        render_intelligence(df, sales_col)
        st.divider()
        render_breakdown(df, sales_col)
