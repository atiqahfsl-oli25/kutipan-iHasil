import streamlit as st
import plotly.express as px
from utils.data_loader import load_yearly_data
from utils.visualizations import create_yearly_chart, create_yearly_bar_chart, create_growth_chart, create_cumulative_chart

st.set_page_config(page_title="Yearly Analysis", page_icon="📊")

st.markdown('<div class="sub-header">📈 Trend Kutipan Tahunan (2001-2026)</div>', unsafe_allow_html=True)

# Load data
yearly_df = load_yearly_data()

# Filter by selected years from session state
if 'selected_years' in st.session_state:
    filtered_df = yearly_df[yearly_df['tahun_kutipan'].isin(st.session_state.selected_years)]
else:
    filtered_df = yearly_df

col1, col2 = st.columns([2, 1])

with col1:
    # Yearly trend line
    fig_line = create_yearly_chart(filtered_df, 'line')
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    # Top 5 years
    st.markdown("### 🏆 5 Tahun Tertinggi")
    top_years = filtered_df.nlargest(5, 'jumlah_kutipan')[['tahun_kutipan', 'jumlah_kutipan']]
    for _, row in top_years.iterrows():
        st.markdown(f"""
        <div style="margin: 10px 0; padding: 10px; background: #f0f2f6; border-radius: 5px;">
            <strong>{int(row['tahun_kutipan'])}</strong><br>
            RM {row['jumlah_kutipan']:,.2f}
        </div>
        """, unsafe_allow_html=True)

# Bar chart
st.markdown("### Perbandingan Tahunan")
fig_bar = create_yearly_bar_chart(filtered_df)
st.plotly_chart(fig_bar, use_container_width=True)

# Growth analysis
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Pertumbuhan Tahun ke Tahun")
    fig_growth = create_growth_chart(filtered_df)
    st.plotly_chart(fig_growth, use_container_width=True)

with col2:
    st.markdown("### Kutipan Kumulatif")
    fig_cumulative = create_cumulative_chart(filtered_df)
    st.plotly_chart(fig_cumulative, use_container_width=True)

# Statistics table
st.markdown("### Statistik Tahunan")
st.dataframe(
    filtered_df.style.format({'jumlah_kutipan': 'RM {:,.2f}'}),
    use_container_width=True
)
