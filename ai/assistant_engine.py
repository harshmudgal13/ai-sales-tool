import streamlit as st
import re

def _md_to_html(text):
    """Convert **bold** markdown to <b>HTML</b> so it renders inside st.markdown HTML blocks."""
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = text.replace('\n', '<br>')
    return text.strip()

def run_ai_agent(df, sales_col):
    """
    Pure logic engine — all UI (buttons, text input) is rendered by ai_assistant.py.
    Reads st.session_state.ai_prompt, generates a response, displays chat history.
    """

    if "chat" not in st.session_state:
        st.session_state.chat = []

    if "last_topic" not in st.session_state:
        st.session_state.last_topic = None

    prompt = st.session_state.get("ai_prompt", None)

    if prompt:
        answer = ""

        if prompt in ("summary", "total"):
            total = df[sales_col].sum()
            avg   = df[sales_col].mean()
            answer = f"**◈ Executive Revenue Overview**\nTotal performance value: **{total:,.2f}**\nAverage baseline: **{avg:,.2f}**\nSignals indicate strong aggregate activity across monitored segments."
            st.session_state.last_topic = "revenue"

        elif prompt == "trend":
            avg  = df[sales_col].mean()
            peak = df[sales_col].max()
            answer = f"**◈ Executive Trend Analysis**\nAverage baseline: **{avg:,.2f}** — Peak: **{peak:,.2f}**\nMomentum appears clustered rather than evenly distributed."
            st.session_state.last_topic = "trend"

        elif prompt == "highest":
            cat_cols = df.select_dtypes("object").columns
            if len(cat_cols) > 0:
                cat = cat_cols[0]
                top = df.groupby(cat)[sales_col].sum().idxmax()
                answer = f"**◈ Top Segment Intelligence**\nTop performing segment: **{top}**\nStrategic focus here may accelerate growth momentum."
            else:
                answer = "**◈ Top Segment:** No categorical columns found."
            st.session_state.last_topic = "segment"

        elif prompt == "risk":
            std = df[sales_col].std()
            answer = f"**◈ Risk Intelligence**\nVariance level: **{std:,.2f}**\nHigh fluctuation suggests performance spikes — monitor volatility zones."
            st.session_state.last_topic = "risk"

        else:
            text  = prompt.lower()
            topic = st.session_state.last_topic

            if "deeper" in text or "expand" in text:
                if topic == "trend":
                    answer = "**◈ Strategic Expansion — Trend**\nTrend concentration suggests uneven growth distribution. Evaluate whether peaks come from sustained demand or short-term spikes."
                elif topic == "risk":
                    answer = "**◈ Risk Deep Dive**\nVolatility indicates exposure to performance swings. Consider stabilising mid-performing categories to reduce peak dependency."
                elif topic == "revenue":
                    answer = "**◈ Revenue Strategy Insight**\nHigh aggregate may mask uneven category contribution. Segment-level optimisation could unlock hidden efficiency."
                else:
                    answer = "Executive AI requires prior context to expand analysis. Run a Quick Action first."

            elif "summary" in text:
                total = df[sales_col].sum()
                avg   = df[sales_col].mean()
                answer = f"**◈ Executive Strategic Brief**\nTotal value: **{total:,.2f}** | Average: **{avg:,.2f}**\nSignals suggest clustered growth dynamics."
            else:
                answer = "**◈ Executive AI**\nContext understood but needs clearer strategic direction.\nTry: expand deeper, give summary, or use a Quick Action above."

        st.session_state.chat.append((prompt, answer))
        st.session_state.ai_prompt = None

    # ── Clear chat button ─────────────────────────────────────────────────────
    if st.session_state.chat:
        if st.button("⬡ Clear Conversation", key="clear_chat_btn"):
            st.session_state.chat = []
            st.session_state.last_topic = None
            st.rerun()

    # ── Chat display — newest first ───────────────────────────────────────────
    for q, a in reversed(st.session_state.chat):
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
background:rgba(16,185,129,0.05);
border:1px solid rgba(16,185,129,0.2);
border-radius:12px;
padding:14px 18px;
margin-bottom:14px;
">
<div style="color:#10b981;font-size:10px;font-weight:700;letter-spacing:2px;
text-transform:uppercase;margin-bottom:6px;">⬡ AI EXECUTIVE</div>
<div style="color:#e2e8f0;font-size:13px;line-height:1.7;">{a_html}</div>
</div>
""", unsafe_allow_html=True)