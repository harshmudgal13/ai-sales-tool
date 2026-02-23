import streamlit as st

def render_header():
    st.markdown("""
<style>
.main-header { padding: 10px 0 20px 0; margin-bottom: 10px; }
.main-header h1 {
    font-size: 36px;
    font-weight: 800;
    background: linear-gradient(90deg, #e2e8f0 0%, #a5b4fc 50%, #6366f1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
    margin-bottom: 4px;
}
.main-header p {
    color: #64748b;
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 0;
}
</style>
<div class="main-header">
    <h1>◈ AI Studio Analytics</h1>
    <p>Executive-grade AI business intelligence platform</p>
</div>
""", unsafe_allow_html=True)