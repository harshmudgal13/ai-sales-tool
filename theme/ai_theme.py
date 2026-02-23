import streamlit as st

def apply_theme():
    st.markdown("""
<style>
/* ── Base app ── */
.stApp {
    background: radial-gradient(ellipse at top, #0d0b1e 0%, #020617 60%, #010409 100%);
    color: white;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0818 0%, #020617 100%);
    border-right: 1px solid rgba(99,102,241,0.25);
    box-shadow: 4px 0 30px rgba(99,102,241,0.1);
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stMultiSelect label,
section[data-testid="stSidebar"] h2 {
    color: #a5b4fc !important;
}

/* ── Selectbox ── */
div[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(99,102,241,0.3) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

/* ── File uploader ── */
section[data-testid="stFileUploadDropzone"] {
    background: rgba(99,102,241,0.04) !important;
    border: 1px dashed rgba(99,102,241,0.4) !important;
    border-radius: 14px !important;
}

/* ── Metric cards ── */
div[data-testid="stMetric"] {
    background: rgba(99,102,241,0.05);
    border: 1px solid rgba(99,102,241,0.2);
    border-radius: 12px;
    padding: 14px;
}

/* ── Divider ── */
hr {
    border-color: rgba(99,102,241,0.2) !important;
}

/* ── Success/info/warning boxes ── */
div[data-testid="stAlert"] {
    border-radius: 12px !important;
    border-left: 3px solid rgba(99,102,241,0.6) !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #020617; }
::-webkit-scrollbar-thumb {
    background: rgba(99,102,241,0.4);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover { background: #6366f1; }

/* ── Caption text ── */
.stCaption { color: #6366f1 !important; font-size: 11px !important; letter-spacing: 0.5px; }
</style>
""", unsafe_allow_html=True)