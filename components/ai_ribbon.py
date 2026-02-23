import streamlit as st

def render_ai_ribbon(df, sales_col):

    total = df[sales_col].sum()
    avg = df[sales_col].mean()
    std = df[sales_col].std()

    topic = st.session_state.get("last_topic", None)

    # =============================
    # 🧠 AUTONOMOUS EXECUTIVE SIGNAL ENGINE
    # =============================
    signal = None
    briefing = None

    if std > avg * 0.5:
        signal = "⚠️ AI detected high volatility across performance clusters."
        briefing = "Risk patterns suggest uneven performance distribution. Leadership should monitor mid-tier segments closely."

    elif total > avg * len(df) * 0.9:
        signal = "📈 AI detects strong aggregate growth momentum."
        briefing = "Performance signals indicate concentrated high-value activity driving overall momentum."

    # =============================
    # 🎯 DEFAULT MESSAGE
    # =============================
    message = f"""
    🤖 <b>AI Insight:</b> Dataset analyzed successfully.
    Avg value: <b>{avg:,.2f}</b> | Total volume: <b>{total:,.0f}</b>
    """

    # =============================
    # ⭐ MEMORY-BASED STATUS
    # =============================
    if topic == "trend":
        message = "📈 <b>AI Monitoring Performance Trend Signals</b>"

    elif topic == "risk":
        message = "⚠️ <b>Risk Intelligence Active</b> — volatility under review."

    elif topic == "revenue":
        message = "📊 <b>Executive Revenue Mode Active</b>"

    elif topic == "segment":
        message = "🏆 <b>Segment Optimization Intelligence Running</b>"

    # Autonomous signal overrides
    if signal:
        message = signal

    # =============================
    # ✨ AI PRESENCE ACTIVATION
    # =============================
    if topic or signal:
        st.markdown(
            "<script>document.body.classList.add('ai-active');</script>",
            unsafe_allow_html=True,
        )

    # =============================
    # 🎨 RIBBON STYLE
    # =============================
    st.markdown("""
    <style>
    .ai-ribbon{
        background:linear-gradient(90deg,#022c22,#064e3b);
        border-radius:12px;
        padding:14px;
        margin-top:10px;
        margin-bottom:10px;
        border:1px solid rgba(16,185,129,0.4);
        box-shadow:0 0 18px rgba(16,185,129,0.15);
        font-size:14px;
    }
    .ai-briefing{
        background:#020617;
        border:1px solid rgba(99,102,241,0.3);
        border-radius:12px;
        padding:14px;
        margin-bottom:12px;
        box-shadow:0 0 14px rgba(99,102,241,0.15);
    }
    </style>
    """, unsafe_allow_html=True)

    # =============================
    # 🧠 EXECUTIVE BRIEFING PANEL (AUTO)
    # =============================
    if briefing:
        st.markdown(f"""
        <div class="ai-briefing">
        🧠 <b>Executive AI Briefing</b><br><br>
        {briefing}
        </div>
        """, unsafe_allow_html=True)

    # Ribbon output
    st.markdown(f"""
    <div class="ai-ribbon">
    {message}
    </div>
    """, unsafe_allow_html=True)