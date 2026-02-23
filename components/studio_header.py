import streamlit as st

def render_studio_header():

    if "active_region" not in st.session_state:
        st.session_state.active_region = "All"

    # ── Futuristic header banner ──────────────────────────────────────────────
    st.markdown("""
<div style="
background: linear-gradient(135deg, #020617 0%, #0f0a28 100%);
border: 1px solid rgba(99,102,241,0.4);
border-radius: 14px;
padding: 18px 24px;
margin-bottom: 15px;
box-shadow: 0 0 30px rgba(99,102,241,0.2);
position: relative;
overflow: hidden;
">
<div style="position:absolute;top:0;left:10%;right:10%;height:1px;
background:linear-gradient(90deg,transparent,#6366f1,transparent);"></div>
<span style="
background: linear-gradient(90deg,#a5b4fc,#6366f1);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
font-weight: 700;
font-size: 15px;
letter-spacing: 1px;
">
◈ AI STUDIO ANALYTICS — Interactive Intelligence Platform
</span>
</div>
""", unsafe_allow_html=True)

    # ── Style the segmented control to match the dark HUD theme ──────────────
    st.markdown("""
<style>
/* Segmented control track */
div[data-testid="stSegmentedControl"] {
    background: #020617 !important;
    border: 1px solid rgba(99,102,241,0.35) !important;
    border-radius: 12px !important;
    padding: 4px !important;
    gap: 4px !important;
    box-shadow: 0 0 16px rgba(99,102,241,0.1) !important;
    width: 100% !important;
}
/* Individual option labels */
div[data-testid="stSegmentedControl"] label {
    color: #94a3b8 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    border-radius: 9px !important;
    transition: all 0.2s ease !important;
}
/* Hover state */
div[data-testid="stSegmentedControl"] label:hover {
    color: white !important;
    background: rgba(99,102,241,0.15) !important;
}
/* Active / selected pill — Streamlit handles this natively */
div[data-testid="stSegmentedControl"] label[data-selected="true"],
div[data-testid="stSegmentedControl"] [aria-checked="true"] {
    background: linear-gradient(90deg, #4f46e5, #6366f1) !important;
    color: white !important;
    box-shadow: 0 0 16px rgba(99,102,241,0.6) !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

    # ── Native segmented control — Streamlit handles active state itself ──────
    regions = ["All", "Central", "East", "South", "West"]

    selected = st.segmented_control(
        label="Region",
        options=regions,
        default=st.session_state.active_region,
        key="region_segmented",
        label_visibility="collapsed"
    )

    if selected and selected != st.session_state.active_region:
        st.session_state.active_region = selected
        st.rerun()

    active = selected or st.session_state.active_region
    st.markdown(f"""
<div style="font-size:11px;color:#6366f1;letter-spacing:1px;
text-transform:uppercase;margin-top:6px;">
◈ {active} Region View Active
</div>
""", unsafe_allow_html=True)

    return active