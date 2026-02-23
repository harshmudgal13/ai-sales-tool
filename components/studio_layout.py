import streamlit as st

def build_sidebar(df):

    with st.sidebar:

        st.markdown("## 🎛 AI Studio Control")

        analysis_mode = st.selectbox(
            "Analysis Mode",
            ["Executive Overview","Revenue Intelligence","Growth Signals"]
        )

        category_cols = df.select_dtypes(include="object").columns

        selected_category = None
        chosen = None

        if len(category_cols) > 0:

            selected_category = st.selectbox(
                "Segment Data By",
                list(category_cols)
            )

            unique_vals = df[selected_category].dropna().unique()
            chosen = st.multiselect("Filter Values", unique_vals)

    if chosen:
        df = df[df[selected_category].isin(chosen)]

    return df
