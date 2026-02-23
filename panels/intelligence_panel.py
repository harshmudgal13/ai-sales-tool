import streamlit as st
import plotly.express as px

def render_intelligence(df, sales_col):

    st.markdown("""
<style>
/* ── Studio cards ── */
.studio-card {
    background: linear-gradient(145deg, rgba(2,6,23,0.95), rgba(15,10,40,0.9));
    border-radius: 14px;
    border: 1px solid rgba(99,102,241,0.3);
    padding: 14px 14px 4px 14px;
    box-shadow: 0 0 20px rgba(99,102,241,0.12);
    margin-bottom: 15px;
    position: relative;
    overflow: hidden;
    transition: all 0.25s ease;
}
.studio-card:hover {
    border-color: rgba(99,102,241,0.6);
    box-shadow: 0 0 30px rgba(99,102,241,0.22);
    transform: translateY(-2px);
}
.card-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #6366f1;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
}
/* ── KPI metric hover ── */
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, rgba(2,6,23,0.95), rgba(15,10,40,0.9));
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 12px;
    padding: 14px 18px;
    transition: all 0.25s ease;
    cursor: default;
}
div[data-testid="stMetric"]:hover {
    border-color: rgba(99,102,241,0.6);
    box-shadow: 0 0 24px rgba(99,102,241,0.25);
    transform: translateY(-2px);
}
div[data-testid="stMetric"] label {
    color: #6366f1 !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
}
div[data-testid="stMetricValue"] {
    background: linear-gradient(90deg, #e2e8f0, #a5b4fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

    df = df.head(3000)

    total = df[sales_col].sum()
    avg   = df[sales_col].mean()
    mx    = df[sales_col].max()

    k1, k2, k3 = st.columns(3)
    k1.metric("Total",   f"{total:,.0f}")
    k2.metric("Average", f"{avg:,.2f}")
    k3.metric("Peak",    f"{mx:,.2f}")

    st.markdown("""
<div style="height:1px;
background:linear-gradient(90deg,transparent,rgba(99,102,241,0.3),transparent);
margin:16px 0;"></div>
""", unsafe_allow_html=True)

    # ── Row 1 ─────────────────────────────────────────────────────────────────
    # KEY FIX: card label merged into the SAME markdown call as the opening div
    # so Streamlit doesn't render an empty visual block before the label.
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
<div class="studio-card">
<div class="card-label">◈ Trend Intelligence</div>
""", unsafe_allow_html=True)
        fig1 = px.line(
            df.reset_index(), y=sales_col,
            template="plotly_dark",
            color_discrete_sequence=["#6366F1"]
        )
        fig1.update_layout(
            height=220, margin=dict(l=0,r=0,t=4,b=0),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class="studio-card">
<div class="card-label">◉ Distribution Signals</div>
""", unsafe_allow_html=True)
        fig2 = px.histogram(
            df, x=sales_col,
            template="plotly_dark",
            color_discrete_sequence=["#22C55E"]
        )
        fig2.update_layout(
            height=220, margin=dict(l=0,r=0,t=4,b=0),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Row 2 ─────────────────────────────────────────────────────────────────
    c3, c4 = st.columns(2)

    with c3:
        st.markdown("""
<div class="studio-card">
<div class="card-label">⬡ Variance Intelligence</div>
""", unsafe_allow_html=True)
        fig3 = px.box(
            df, y=sales_col,
            template="plotly_dark",
            color_discrete_sequence=["#8B5CF6"]
        )
        fig3.update_layout(
            height=220, margin=dict(l=0,r=0,t=4,b=0),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c4:
        st.markdown("""
<div class="studio-card">
<div class="card-label">⟁ Performance Mapping</div>
""", unsafe_allow_html=True)
        fig4 = px.scatter(
            df.reset_index(), y=sales_col,
            template="plotly_dark",
            color_discrete_sequence=["#F59E0B"]
        )
        fig4.update_layout(
            height=220, margin=dict(l=0,r=0,t=4,b=0),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)