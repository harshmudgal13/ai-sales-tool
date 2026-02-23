import streamlit as st
import re

def _md_to_html(text):
    """Convert **bold** markdown to <b>HTML</b> so it renders inside HTML divs."""
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'### (.*?)(<br>|$)', r'<div style="color:#a5b4fc;font-weight:700;font-size:13px;margin:10px 0 4px 0;">\1</div>', text)
    text = text.replace('\n', '<br>')
    return text.strip()

def run_llm_agent(df, sales_col):
    """
    Pro Copilot engine — all UI is rendered by ai_assistant.py.
    Reads st.session_state.ai_prompt and renders a response.
    """

    if "llm_chat" not in st.session_state:
        st.session_state.llm_chat = []

    prompt = st.session_state.get("ai_prompt", None)

    if prompt:
        avg     = df[sales_col].mean()
        max_val = df[sales_col].max()
        total   = df[sales_col].sum()

        response = (
            f"**◈ AI Copilot — Executive Intelligence**\n\n"
            f"Query analysed: {prompt}\n\n"
            f"Average performance: **{avg:,.2f}** — indicating moderate operational stability.\n"
            f"Peak values reach **{max_val:,.2f}**, suggesting localised high-impact segments.\n"
            f"Gross volume: **{total:,.0f}** — growth is concentrated rather than broad.\n\n"
            f"**◈ Strategic Interpretation**\n"
            f"Momentum is clustered within select categories. Monitor volatility and reinforce high-performing verticals.\n\n"
            f"**◈ Recommended Action**\n"
            f"Scale top-performing segments and reduce exposure to low-yield categories."
        )
        st.session_state.llm_chat.append((prompt, response))
        st.session_state.ai_prompt = None

    # ── Pro badge ─────────────────────────────────────────────────────────────
    st.markdown("""
<div style="
background:rgba(139,92,246,0.08);
border:1px solid rgba(139,92,246,0.3);
border-radius:10px;
padding:10px 16px;
font-size:11px;
color:#c4b5fd;
margin-bottom:12px;
letter-spacing:1px;
">
⬡ AI COPILOT — DEMO MODE (no API key required)
</div>
""", unsafe_allow_html=True)

    # ── Clear button ──────────────────────────────────────────────────────────
    if st.session_state.llm_chat:
        if st.button("⬡ Clear Conversation", key="clear_llm_btn"):
            st.session_state.llm_chat = []
            st.rerun()

    # ── Chat display ──────────────────────────────────────────────────────────
    for q, a in reversed(st.session_state.llm_chat):
        a_html = _md_to_html(a)
        st.markdown(f"""
<div style="
background:rgba(99,102,241,0.06);
border:1px solid rgba(99,102,241,0.2);
border-radius:12px;
padding:14px 18px;
margin-bottom:8px;
">
<div style="color:#6366f1;font-size:10px;font-weight:700;letter-spacing:2px;
text-transform:uppercase;margin-bottom:6px;">◈ YOU</div>
<div style="color:#cbd5e1;font-size:13px;">{q}</div>
</div>
<div style="
background:rgba(139,92,246,0.05);
border:1px solid rgba(139,92,246,0.25);
border-radius:12px;
padding:14px 18px;
margin-bottom:14px;
">
<div style="color:#8b5cf6;font-size:10px;font-weight:700;letter-spacing:2px;
text-transform:uppercase;margin-bottom:6px;">⬡ AI COPILOT PRO</div>
<div style="color:#e2e8f0;font-size:13px;line-height:1.7;">{a_html}</div>
</div>
""", unsafe_allow_html=True)