import streamlit as st
import plotly.express as px

def render_breakdown(df, sales_col):

    st.markdown("""
<style>
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
</style>
""", unsafe_allow_html=True)

    category_cols = df.select_dtypes(include="object").columns.tolist()
    if len(category_cols) == 0:
        st.info("No categorical columns detected.")
        return

    priority_cols = ["Category", "Sub-Category", "Segment", "Ship Mode", "State", "Region"]
    cat = next((p for p in priority_cols if p in category_cols), category_cols[0])

    bar_df = df.groupby(cat)[sales_col].sum().reset_index()
    bar_df = bar_df.sort_values(sales_col, ascending=False)

    # ── Row 1 ─────────────────────────────────────────────────────────────────
    # KEY FIX: card label merged into the SAME markdown call as the opening div
    # so Streamlit doesn't render an empty visual block before the label.
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
<div class="studio-card">
<div class="card-label">◈ Category Performance</div>
""", unsafe_allow_html=True)
        fig1 = px.bar(
            bar_df, x=cat, y=sales_col,
            template="plotly_dark",
            color_discrete_sequence=["#6366F1"]
        )
        fig1.update_layout(
            height=260, margin=dict(l=0,r=0,t=4,b=0),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class="studio-card">
<div class="card-label">◉ Revenue Distribution</div>
""", unsafe_allow_html=True)
        pie_df = bar_df.head(10)
        fig2 = px.pie(
            pie_df, names=cat, values=sales_col,
            hole=0.65, template="plotly_dark"
        )
        fig2.update_layout(
            height=260, margin=dict(l=0,r=0,t=4,b=0),
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Row 2 ─────────────────────────────────────────────────────────────────
    c3, c4 = st.columns(2)

    with c3:
        st.markdown("""
<div class="studio-card">
<div class="card-label">⟁ Top Segments Ranking</div>
""", unsafe_allow_html=True)
        fig3 = px.bar(
            bar_df.head(10), y=cat, x=sales_col,
            orientation="h",
            template="plotly_dark",
            color_discrete_sequence=["#22C55E"]
        )
        fig3.update_layout(
            height=260, margin=dict(l=0,r=0,t=4,b=0),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c4:
        st.markdown("""
<div class="studio-card">
<div class="card-label">⬡ Revenue Radar</div>
""", unsafe_allow_html=True)
        radar_df = bar_df.head(8)
        fig4 = px.line_polar(
            radar_df, r=sales_col, theta=cat,
            line_close=True, template="plotly_dark"
        )
        fig4.update_layout(
            height=260, margin=dict(l=0,r=0,t=4,b=0),
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)