import streamlit as st

def render_studio_controls(df):

    if "studio_tab" not in st.session_state:
        st.session_state.studio_tab = "Executive Dashboard"

    # ── Shared segmented control styling ─────────────────────────────────────
    st.markdown("""
<style>
.studio-toolbar {
    background: linear-gradient(135deg, #020617 0%, #0f0a28 100%);
    border-radius: 12px;
    border: 1px solid rgba(99,102,241,0.35);
    padding: 14px 18px;
    margin-bottom: 15px;
    box-shadow: 0 0 20px rgba(99,102,241,0.12);
    position: relative;
    overflow: hidden;
}
.studio-toolbar::before {
    content: '';
    position: absolute;
    top: 0; left: 10%; right: 10%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,102,241,0.5), transparent);
}
/* Selectbox styling */
div[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(99,102,241,0.3) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}
/* Segmented control track */
div[data-testid="stSegmentedControl"] {
    background: rgba(2,6,23,0.8) !important;
    border: 1px solid rgba(99,102,241,0.35) !important;
    border-radius: 10px !important;
    padding: 3px !important;
    box-shadow: 0 0 12px rgba(99,102,241,0.1) !important;
    width: 100% !important;
}
div[data-testid="stSegmentedControl"] label {
    color: #94a3b8 !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
    white-space: nowrap !important;
}
div[data-testid="stSegmentedControl"] label:hover {
    color: white !important;
    background: rgba(99,102,241,0.15) !important;
}
div[data-testid="stSegmentedControl"] label[data-selected="true"],
div[data-testid="stSegmentedControl"] [aria-checked="true"] {
    background: linear-gradient(90deg, #4f46e5, #6366f1) !important;
    color: white !important;
    box-shadow: 0 0 14px rgba(99,102,241,0.6) !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

    st.markdown('<div class="studio-toolbar">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2, 2, 3])

    with c1:
        mode = st.selectbox(
            "◈ Intelligence Mode",
            ["Revenue Intelligence", "Growth Intelligence", "Segment Intelligence"]
        )

    category_cols    = df.select_dtypes(include="object").columns
    selected_segment = None

    if len(category_cols) > 0:
        cat    = category_cols[0]
        values = df[cat].dropna().unique().tolist()
        with c2:
            selected_segment = st.selectbox(
                f"⬡ {cat} Filter",
                ["All"] + values
            )

    # ── Native segmented control for tabs — no JS needed ─────────────────────
    tabs = ["Executive Dashboard", "Performance Lab", "AI Signals"]

    with c3:
        selected_tab = st.segmented_control(
            label="View",
            options=tabs,
            default=st.session_state.studio_tab,
            key="tab_segmented",
            label_visibility="collapsed"
        )

    if selected_tab and selected_tab != st.session_state.studio_tab:
        st.session_state.studio_tab = selected_tab
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    active_tab = selected_tab or st.session_state.studio_tab
    return mode, selected_segment, active_tab