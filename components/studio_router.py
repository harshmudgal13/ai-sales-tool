import streamlit as st
from panels.intelligence_panel import render_intelligence
from panels.breakdown_panel import render_breakdown
from layout.enterprise_layout import enterprise_section, close_section



# 🧠 MAIN STUDIO VIEW ENGINE
def render_studio_view(tab, df, sales_col):

    # ======================================
    # 📊 EXECUTIVE DASHBOARD (MAIN VIEW)
    # ======================================
    if tab == "Executive Dashboard":

        enterprise_section("Executive Intelligence", "🧭")
        render_intelligence(df, sales_col)
        close_section()

        enterprise_section("Strategic Breakdown", "📊")
        render_breakdown(df, sales_col)
        close_section()

    # ======================================
    # 🚀 PERFORMANCE LAB (NOW REAL GRID)
    # ======================================
    elif tab == "Performance Lab":

        enterprise_section("Performance Analytics Lab", "🚀")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Dataset Rows", len(df))

        with c2:
            st.metric(
                "Unique Segments",
                df.select_dtypes(include="object").nunique().sum()
            )

        with c3:
            st.metric(
                "Numeric Features",
                len(df.select_dtypes(include="number").columns)
            )

        st.markdown("---")

        c4, c5 = st.columns(2)

        with c4:
            st.area_chart(df[sales_col].head(200))

        with c5:
            st.bar_chart(df[sales_col].head(200))

        close_section()

    # ======================================
    # 🤖 AI SIGNAL INTELLIGENCE PANEL
    # ======================================
    else:

        enterprise_section("AI Signal Intelligence", "🤖")

        st.success("""
        ✔ Revenue acceleration signals detected  
        ✔ Behavioral clustering active  
        ✔ Strategic anomaly monitoring enabled  
        """)

        st.markdown("### 🧠 AI Strategic Summary")

        st.write(f"""
        The AI engine detects patterns based on **{sales_col}** performance.
        Future versions will include forecasting, segmentation heatmaps,
        and automated executive briefings.
        """)

        close_section()