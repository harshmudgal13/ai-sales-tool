import streamlit as st
from utils.data_loader import load_data

from layout.sidebar import render_sidebar
from layout.header import render_header
from engine.data_engine import apply_filters
from theme.ai_theme import apply_theme
from components.studio_controls import render_studio_controls
from components.studio_router import render_studio_view
from components.ai_ribbon import render_ai_ribbon
from components.ai_assistant import render_ai_assistant
from components.studio_header import render_studio_header
from components.kpi_tiles import render_kpi_tiles
from engine.schema_engine import detect_schema


st.set_page_config(layout="wide", page_title="AI Studio Analytics")

apply_theme()
render_header()

file = st.file_uploader("Upload Business CSV", type=["csv"])

if file:

    df = load_data(file)
    schema = detect_schema(df)

    active_region = render_studio_header()

    region_col = None
    for col in schema["categories"]:
        values = df[col].astype(str).str.lower().unique().tolist()
        if any(r in values for r in ["central", "east", "south", "west"]):
            region_col = col
            break

    if region_col and active_region != "All":
        df = df[df[region_col].astype(str).str.lower() == active_region.lower()]

    mode, selected_segment, studio_tab = render_studio_controls(df)

    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) == 0:
        st.warning("No numeric columns detected.")
        st.stop()
    sales_col = numeric_cols[0]

    mode, col, vals = render_sidebar(df)
    df = apply_filters(df, col, vals)

    render_kpi_tiles(df, sales_col)
    render_ai_ribbon(df, sales_col)
    render_studio_view(studio_tab, df, sales_col)

    # ── AI Executive Assistant section divider ────────────────────────────────
    st.markdown("""
<div style="
background: linear-gradient(135deg, #020617 0%, #0f0a28 100%);
border: 1px solid rgba(99,102,241,0.35);
border-radius: 12px;
padding: 14px 24px;
margin: 24px 0 0 0;
box-shadow: 0 0 20px rgba(99,102,241,0.1);
position: relative;
overflow: hidden;
display: flex;
align-items: center;
gap: 12px;
">
<div style="position:absolute;top:0;left:5%;right:5%;height:1px;
background:linear-gradient(90deg,transparent,rgba(99,102,241,0.5),transparent);"></div>
<span style="color:#6366f1;font-size:18px;">◈</span>
<span style="
background: linear-gradient(90deg,#a5b4fc,#6366f1);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
font-weight: 700;
font-size: 13px;
letter-spacing: 2px;
text-transform: uppercase;
">AI Executive Assistant</span>
<div style="flex:1;height:1px;
background:linear-gradient(90deg,rgba(99,102,241,0.3),transparent);
margin-left:8px;"></div>
<span style="
background:rgba(16,185,129,0.1);
border:1px solid rgba(16,185,129,0.3);
border-radius:100px;
padding:3px 12px;
color:#10b981;
font-size:10px;
font-weight:700;
letter-spacing:1px;
">LIVE</span>
</div>
""", unsafe_allow_html=True)

    render_ai_assistant(df, sales_col)