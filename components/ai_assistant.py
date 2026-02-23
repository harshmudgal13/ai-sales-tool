import streamlit as st
from ai.assistant_engine import run_ai_agent
from ai.assistant_llm import run_llm_agent

def render_ai_assistant(df, sales_col):

    total = df[sales_col].sum()
    avg   = df[sales_col].mean()

    if "ai_prompt" not in st.session_state:
        st.session_state.ai_prompt = None

    st.markdown("""
<style>
.ai-exec-panel {
    background: linear-gradient(135deg,rgba(2,6,23,0.97) 0%,rgba(15,10,40,0.97) 100%);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(99,102,241,0.4);
    border-radius: 20px;
    padding: 30px 35px;
    margin-top: 10px;
    box-shadow: 0 0 60px rgba(79,70,229,0.15),
                inset 0 1px 0 rgba(255,255,255,0.05);
    position: relative;
    overflow: hidden;
}
.ai-exec-panel::before {
    content:'';
    position:absolute;
    top:0;left:10%;right:10%;
    height:1px;
    background:linear-gradient(90deg,transparent,#6366f1,transparent);
}
.ai-metric-row {
    display: flex;
    gap: 12px;
    margin-bottom: 20px;
    flex-wrap: wrap;
}
.ai-chip-green {
    background: rgba(16,185,129,0.08);
    border: 1px solid rgba(16,185,129,0.35);
    padding: 7px 16px;
    border-radius: 100px;
    color: #10b981;
    font-weight: 600;
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
    box-shadow: 0 0 12px rgba(16,185,129,0.1);
}
.ai-chip-blue {
    background: rgba(99,102,241,0.08);
    border: 1px solid rgba(99,102,241,0.35);
    padding: 7px 16px;
    border-radius: 100px;
    color: #a5b4fc;
    font-weight: 600;
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.ai-section-label {
    color: #6366f1;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 18px 0 10px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}
.ai-section-label::after {
    content:'';flex:1;height:1px;
    background:linear-gradient(90deg,rgba(99,102,241,0.4),transparent);
}
.ai-divider {
    height: 1px;
    background: linear-gradient(90deg,transparent,rgba(99,102,241,0.4),transparent);
    margin: 20px 0;
}
div[data-testid="stRadio"] > div { gap:12px !important; }
div[data-testid="stRadio"] label {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid rgba(99,102,241,0.2) !important;
    padding: 10px 22px !important;
    border-radius: 10px !important;
    color: #94a3b8 !important;
    font-size: 13px !important;
    transition: all 0.25s !important;
}
div[data-testid="stRadio"] label:hover {
    border-color: rgba(99,102,241,0.6) !important;
    color: white !important;
}
div[data-testid="stRadio"] label[data-selected="true"] {
    background: rgba(99,102,241,0.12) !important;
    border-color: #6366f1 !important;
    color: white !important;
    box-shadow: 0 0 18px rgba(99,102,241,0.25) !important;
}
.stButton > button {
    background: rgba(99,102,241,0.05) !important;
    border: 1px solid rgba(99,102,241,0.25) !important;
    color: #94a3b8 !important;
    border-radius: 10px !important;
    font-size: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    transition: all 0.25s ease !important;
}
.stButton > button:hover {
    border-color: #6366f1 !important;
    background: rgba(99,102,241,0.15) !important;
    color: white !important;
    box-shadow: 0 0 18px rgba(99,102,241,0.3) !important;
    transform: translateY(-2px) !important;
}
div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(99,102,241,0.25) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-size: 13px !important;
    transition: border-color 0.25s !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 20px rgba(99,102,241,0.2) !important;
}
</style>
""", unsafe_allow_html=True)

    # ── Open panel + metric chips in ONE markdown call to avoid blank block ───
    # (Splitting the opening <div> from content causes Streamlit to render
    #  an empty visual block between them. Merging fixes it.)
    st.markdown(f"""
<div class="ai-exec-panel">
<div class="ai-metric-row">
    <span class="ai-chip-green">⬡ AVG BASELINE: ${avg:,.2f}</span>
    <span class="ai-chip-blue">◉ GROSS VOLUME: ${total:,.0f}</span>
</div>
""", unsafe_allow_html=True)

    # AI Mode
    st.markdown('<div class="ai-section-label">⬡ AI MODE</div>', unsafe_allow_html=True)
    mode = st.radio(
        "AI Mode",
        ["Executive AI (Free)", "AI Copilot (Pro)"],
        horizontal=True,
        key="ai_mode_radio",
        label_visibility="collapsed"
    )

    # Quick Actions
    st.markdown('<div class="ai-section-label">◈ QUICK ACTIONS</div>', unsafe_allow_html=True)
    actions = [
        ("Executive Summary", "summary"),
        ("Performance Trend", "trend"),
        ("Total Revenue",     "total"),
        ("Top Segment",       "highest"),
        ("Risk Analysis",     "risk"),
    ]
    action_cols = st.columns(len(actions))
    for col, (label, prompt_key) in zip(action_cols, actions):
        with col:
            if st.button(label, key=f"ai_btn_{prompt_key}"):
                st.session_state.ai_prompt = prompt_key

    # Free-text input
    st.markdown('<div class="ai-section-label">⟁ CONTINUE DISCUSSION</div>', unsafe_allow_html=True)
    user_text = st.text_input(
        "Continue executive discussion",
        placeholder="Example: explain deeper, expand risk, give summary...",
        key="ai_input",
        label_visibility="collapsed"
    )
    if user_text:
        st.session_state.ai_prompt = user_text

    st.markdown('<div class="ai-divider"></div>', unsafe_allow_html=True)

    if mode == "Executive AI (Free)":
        run_ai_agent(df, sales_col)
    else:
        run_llm_agent(df, sales_col)

    st.markdown('</div>', unsafe_allow_html=True)