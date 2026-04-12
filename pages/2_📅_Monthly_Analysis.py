import streamlit as st
import calendar
from utils.data_loader import load_monthly_data
from utils.visualizations import create_monthly_chart, create_monthly_heatmap, create_seasonal_chart
import pandas as pd

st.set_page_config(page_title="Monthly Analysis", page_icon="📅")

st.markdown('<div class="sub-header">📊 Analisis Kutipan Bulanan</div>', unsafe_allow_html=True)

# Load data
monthly_df = load_monthly_data()

# Apply date filter
if 'date_range' in st.session_state and len(st.session_state.date_range) == 2:
    mask = (monthly_df['date'] >= pd.to_datetime(st.session_state.date_range[0])) & \
           (monthly_df['date'] <= pd.to_datetime(st.session_state.date_range[1]))
    filtered_df = monthly_df[mask]
else:
    filtered_df = monthly_df

col1, col2 = st.columns(2)

with col1:
    # Monthly trend
    fig_monthly = create_monthly_chart(filtered_df, 'line')
    st.plotly_chart(fig_monthly, use_container_width=True)

with col2:
    # Monthly heatmap
    fig_heatmap = create_monthly_heatmap(filtered_df)
    st.plotly_chart(fig_heatmap, use_container_width=True)

# Seasonal analysis
st.markdown("### Analisis Musiman")
fig_seasonal = create_seasonal_chart(filtered_df)
st.plotly_chart(fig_seasonal, use_container_width=True)

# Best and worst months
col1, col2 = st.columns(2)

with col1:
    best_month = filtered_df.loc[filtered_df['jumlah_kutipan'].idxmax()]
    st.markdown(f"""
    <div class="insight-box">
        <strong>🏆 Bulan Terbaik:</strong><br>
        {calendar.month_name[int(best_month['bulan_kutipan'])]} {int(best_month['tahun_kutipan'])}<br>
        RM {best_month['jumlah_kutipan']:,.2f}
    </div>
    """, unsafe_allow_html=True)

with col2:
    worst_month = filtered_df.loc[filtered_df['jumlah_kutipan'].idxmin()]
    st.markdown(f"""
    <div class="insight-box">
        <strong>📉 Bulan Terburuk:</strong><br>
        {calendar.month_name[int(worst_month['bulan_kutipan'])]} {int(worst_month['tahun_kutipan'])}<br>
        RM {worst_month['jumlah_kutipan']:,.2f}
    </div>
    """, unsafe_allow_html=True)

# Monthly statistics table
st.markdown("### Statistik Bulanan")
st.dataframe(
    filtered_df.sort_values('date', ascending=False).style.format({'jumlah_kutipan': 'RM {:,.2f}'
