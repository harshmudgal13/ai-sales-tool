import streamlit as st

def render_floating_ai(df, sales_col):

    # ---------- FLOATING PANEL STYLE ----------
    st.markdown("""
    <style>
    .floating-ai{
        position:fixed;
        bottom:25px;
        right:25px;
        width:280px;
        background:#020617;
        border:1px solid rgba(99,102,241,0.4);
        border-radius:14px;
        padding:16px;
        box-shadow:0 0 25px rgba(99,102,241,0.35);
        z-index:999;
    }
    .ai-title{
        font-weight:600;
        margin-bottom:6px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- FLOATING CONTAINER ----------
    st.markdown('<div class="floating-ai">', unsafe_allow_html=True)

    st.markdown("🤖 **AI Studio Assistant**")

    # ---------- BASIC DATA SIGNALS ----------
    avg_val = round(df[sales_col].mean(),2)
    total_val = int(df[sales_col].sum())

    st.caption(f"Avg value detected: {avg_val}")
    st.caption("Signals suggest monitoring peak patterns.")

    # ---------- PLACEHOLDER FOR REAL AI ----------
    # We will connect LLM engine here next
    # DO NOT REMOVE — this is the hook
    from ai.assistant_engine import run_ai_agent
    run_ai_agent(df, sales_col)

    st.markdown("</div>", unsafe_allow_html=True)
