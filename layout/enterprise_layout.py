import streamlit as st

# Icon map — replaces emoji with futuristic geometric symbols
ICONS = {
    "📊": "◉",
    "🧭": "◈",
    "🚀": "⟁",
    "🧠": "⬡",
    "📈": "◈",
    "⭐": "◈",
    "🤖": "⬡",
}

def enterprise_section(title, icon="◉"):
    # Remap any emoji icon passed in
    icon = ICONS.get(icon, icon)

    st.markdown(f"""
<div style="
background: linear-gradient(135deg, #020617 0%, #0f0a28 100%);
border-radius: 14px;
border: 1px solid rgba(99,102,241,0.3);
padding: 16px 20px 4px 20px;
margin-top: 16px;
box-shadow: 0 0 24px rgba(99,102,241,0.1);
position: relative;
overflow: hidden;
">
<div style="position:absolute;top:0;left:8%;right:8%;height:1px;
background:linear-gradient(90deg,transparent,rgba(99,102,241,0.5),transparent);"></div>
<div style="
display:flex;align-items:center;gap:10px;margin-bottom:10px;
">
<span style="color:#6366f1;font-size:20px;">{icon}</span>
<span style="
background: linear-gradient(90deg,#e2e8f0,#a5b4fc);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
font-weight: 700;
font-size: 17px;
letter-spacing: 0.5px;
">{title}</span>
</div>
""", unsafe_allow_html=True)


def close_section():
    st.markdown("</div>", unsafe_allow_html=True)