import streamlit as st

def render_kpi_tiles(df, sales_col):

    total   = df[sales_col].sum()
    avg     = df[sales_col].mean()
    highest = df[sales_col].max()
    lowest  = df[sales_col].min()

    st.markdown("""
<style>
.kpi-card {
    background: linear-gradient(145deg, rgba(2,6,23,0.95), rgba(15,10,40,0.9));
    border: 1px solid rgba(99,102,241,0.3);
    padding: 20px 16px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 0 20px rgba(99,102,241,0.12);
    position: relative;
    overflow: hidden;
    transition: all 0.25s ease;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 20%; right: 20%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,102,241,0.6), transparent);
}
.kpi-card:hover {
    border-color: rgba(99,102,241,0.6);
    box-shadow: 0 0 30px rgba(99,102,241,0.25);
    transform: translateY(-2px);
}
.kpi-title {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #6366f1;
    margin-bottom: 10px;
}
.kpi-value {
    font-size: 28px;
    font-weight: 700;
    background: linear-gradient(90deg, #e2e8f0, #a5b4fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
}
</style>
""", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    tiles = [
        (c1, "Total Value",  f"{total:,.0f}"),
        (c2, "Average",      f"{avg:,.2f}"),
        (c3, "Highest",      f"{highest:,.2f}"),
        (c4, "Lowest",       f"{lowest:,.2f}"),
    ]

    for col, title, value in tiles:
        with col:
            st.markdown(f"""
<div class="kpi-card">
    <div class="kpi-title">{title}</div>
    <div class="kpi-value">{value}</div>
</div>
""", unsafe_allow_html=True)