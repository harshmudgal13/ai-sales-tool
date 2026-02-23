import streamlit as st

def render_sidebar(df):

    with st.sidebar:
        st.markdown("""
<style>
.sidebar-title {
    font-size: 16px;
    font-weight: 700;
    background: linear-gradient(90deg, #a5b4fc, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 16px;
}
.sidebar-divider {
    height: 1px;
    background: linear-gradient(90deg, rgba(99,102,241,0.4), transparent);
    margin: 14px 0;
}
</style>
<div class="sidebar-title">◈ AI Studio Control</div>
<div class="sidebar-divider"></div>
""", unsafe_allow_html=True)

        mode = st.selectbox(
            "Analysis Mode",
            ["Revenue Intelligence", "Growth Signals", "Executive Overview"]
        )

        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

        category_cols = df.select_dtypes(include="object").columns
        selected_col  = None
        selected_vals = None

        if len(category_cols) > 0:
            selected_col = st.selectbox("Segment Data By", category_cols)
            if selected_col:
                vals          = df[selected_col].dropna().unique()
                selected_vals = st.multiselect("Filter Values", vals)

        return mode, selected_col, selected_vals