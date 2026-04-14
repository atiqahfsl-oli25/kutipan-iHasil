import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="iHasil Dashboard",
    page_icon="💰",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2rem;
        color: #1E88E5;
        text-align: center;
        padding: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Load data directly from CSV files in GitHub
@st.cache_data
def load_monthly_data():
    """Load monthly data from embedded CSV string"""
    csv_data = """tahun_kutipan,bulan_kutipan,jumlah_kutipan
2026,4,14887219.29
2026,3,205701224.56
2026,2,115013653.48
2026,1,167698978.23
2025,12,233335103.71
2025,11,176012755.69
2025,10,100356928.61
2025,9,160996765.31
2025,8,85599468.12
2025,7,150252179.44
2025,6,169392124.89
2025,5,152769602.15
2025,4,302006624.16
2025,3,177348549.52
2025,2,261934231.75
2025,1,110163930.51
2024,12,142214806.56
2024,11,262059648.12
2024,10,198584760.46
2024,9,111677882.05
2024,8,113787606.9
2024,7,137655038.35
2024,6,241663195.14
2024,5,264644437.46
2024,4,175390759.59
2024,3,197229408.98
2024,2,132199596.17
2024,1,147890632.35"""
    
    from io import StringIO
    df = pd.read_csv(StringIO(csv_data))
    df['date'] = pd.to_datetime(df['tahun_kutipan'].astype(str) + '-' + df['bulan_kutipan'].astype(str) + '-01')
    return df

@st.cache_data
def load_yearly_data():
    """Load yearly data from embedded CSV string"""
    csv_data = """tahun_kutipan,jumlah_kutipan
2026,503301075.56
2025,2080168263.86
2024,2124997772.13
2023,854833976.49
2022,457747105.68
2021,488643830.52
2020,258213455.62
2019,303743084.55
2018,255694648.07
2017,289928787.44
2016,265607486.53
2015,263790843.14
2014,274481910.15
2013,23073783.48
2012,234012732.25
2011,251058145.91
2010,233009303.12
2009,186340902.21
2008,169719082.26
2007,28121029.68
2006,10702435.9
2005,7479146.5
2004,6861788.3
2003,5426358.3
2002,5422058.2
2001,2406897.15"""
    
    from io import StringIO
    df = pd.read_csv(StringIO(csv_data))
    return df

@st.cache_data
def load_daily_data():
    """Load daily data from embedded CSV string"""
    csv_data = """tarikh_kutipan,jumlah_kutipan
2026-04-09,2751143.33
2026-04-08,2100194.83
2026-04-07,1646740.23
2026-04-06,3352152.08
2026-04-05,1408200.79
2026-04-04,70137.15
2026-04-03,105469.34
2026-04-02,1414420.85
2026-04-01,2036628.29
2026-03-31,2764090.11
2026-03-30,1473185.96
2026-03-29,60846344.62
2026-03-28,68801.93
2026-03-27,135254.14
2026-03-26,1677231.01
2026-03-25,1005780.52
2026-03-24,635132.1
2026-03-23,30589.94
2026-03-22,15658.6
2026-03-21,7805.86
2026-03-20,29711.18
2026-03-19,303839.7
2026-03-18,78245960
2026-03-17,2127220.28
2026-03-16,1740512.21
2026-03-15,21690258.02
2026-03-14,60325.62
2026-03-13,407918.9
2026-03-12,2109915.65
2026-03-11,11396704
2026-03-10,279847.5"""
    
    from io import StringIO
    df = pd.read_csv(StringIO(csv_data))
    df['tarikh_kutipan'] = pd.to_datetime(df['tarikh_kutipan'])
    return df

# Load all data
monthly_df = load_monthly_data()
yearly_df = load_yearly_data()
daily_df = load_daily_data()

# Calculate metrics
total_all_time = yearly_df['jumlah_kutipan'].sum()
current_year = yearly_df.iloc[0]['tahun_kutipan']
current_year_value = yearly_df.iloc[0]['jumlah_kutipan']
current_month_value = monthly_df.iloc[0]['jumlah_kutipan']
current_day_value = daily_df.iloc[-1]['jumlah_kutipan']

# Title
st.markdown('<div class="main-header">💰 iHasil Dashboard - Analisis Kutipan</div>', unsafe_allow_html=True)

# Key metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>💰 Total Keseluruhan</h3>
        <h2>RM {total_all_time:,.2f}</h2>
        <small>2001-2026</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>📊 Tahun {current_year}</h3>
        <h2>RM {current_year_value:,.2f}</h2>
        <small>Jumlah kutipan</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ogo', 'Sep', 'Okt', 'Nov', 'Dis']
    current_month = int(monthly_df.iloc[0]['bulan_kutipan'])
    st.markdown(f"""
    <div class="metric-card">
        <h3>📅 Bulan Terkini</h3>
        <h2>RM {current_month_value:,.2f}</h2>
        <small>{month_name[current_month-1]} {monthly_df.iloc[0]['tahun_kutipan']}</small>
    </div>
    """, unsafe_allow_html=True)

with col4:
    latest_date = daily_df.iloc[-1]['tarikh_kutipan'].strftime('%d/%m/%Y')
    st.markdown(f"""
    <div class="metric-card">
        <h3>📆 Hari Terkini</h3>
        <h2>RM {current_day_value:,.2f}</h2>
        <small>{latest_date}</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["📈 Trend Tahunan", "📊 Analisis Bulanan", "📅 Trend Harian"])

with tab1:
    st.subheader("Trend Kutipan Tahunan")
    
    # Yearly line chart
    import plotly.express as px
    fig_yearly = px.line(
        yearly_df,
        x='tahun_kutipan',
        y='jumlah_kutipan',
        title='Kutipan Tahunan (2001-2026)',
        markers=True
    )
    fig_yearly.update_layout(height=500)
    st.plotly_chart(fig_yearly, use_container_width=True)
    
    # Top years
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏆 5 Tahun Tertinggi")
        top5 = yearly_df.nlargest(5, 'jumlah_kutipan')[['tahun_kutipan', 'jumlah_kutipan']]
        for _, row in top5.iterrows():
            st.write(f"**{int(row['tahun_kutipan'])}**: RM {row['jumlah_kutipan']:,.2f}")
    
    with col2:
        st.subheader("📊 Statistik Tahunan")
        st.write(f"Purata: RM {yearly_df['jumlah_kutipan'].mean():,.2f}")
        st.write(f"Median: RM {yearly_df['jumlah_kutipan'].median():,.2f}")
        st.write(f"Maksimum: RM {yearly_df['jumlah_kutipan'].max():,.2f}")
        st.write(f"Minimum: RM {yearly_df['jumlah_kutipan'].min():,.2f}")

with tab2:
    st.subheader("Analisis Kutipan Bulanan")
    
    # Monthly trend
    fig_monthly = px.line(
        monthly_df,
        x='date',
        y='jumlah_kutipan',
        title='Trend Kutipan Bulanan',
        markers=True
    )
    fig_monthly.update_layout(height=500)
    st.plotly_chart(fig_monthly, use_container_width=True)
    
    # Best and worst months
    col1, col2 = st.columns(2)
    
    with col1:
        best_month = monthly_df.loc[monthly_df['jumlah_kutipan'].idxmax()]
        st.info(f"**🏆 Bulan Terbaik:** {int(best_month['bulan_kutipan'])}/{int(best_month['tahun_kutipan'])} - RM {best_month['jumlah_kutipan']:,.2f}")
    
    with col2:
        worst_month = monthly_df.loc[monthly_df['jumlah_kutipan'].idxmin()]
        st.warning(f"**📉 Bulan Terburuk:** {int(worst_month['bulan_kutipan'])}/{int(worst_month['tahun_kutipan'])} - RM {worst_month['jumlah_kutipan']:,.2f}")
    
    # Monthly average by month
    monthly_avg = monthly_df.groupby('bulan_kutipan')['jumlah_kutipan'].mean().reset_index()
    fig_seasonal = px.bar(
        monthly_avg,
        x='bulan_kutipan',
        y='jumlah_kutipan',
        title='Purata Kutipan mengikut Bulan',
        labels={'bulan_kutipan': 'Bulan', 'jumlah_kutipan': 'Purata (RM)'}
    )
    st.plotly_chart(fig_seasonal, use_container_width=True)

with tab3:
    st.subheader("Trend Kutipan Harian (Mac - April 2026)")
    
    # Daily chart
    fig_daily = px.line(
        daily_df,
        x='tarikh_kutipan',
        y='jumlah_kutipan',
        title='Kutipan Harian',
        markers=True
    )
    fig_daily.update_layout(height=500)
    st.plotly_chart(fig_daily, use_container_width=True)
    
    # Daily statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Purata Harian", f"RM {daily_df['jumlah_kutipan'].mean():,.2f}")
    with col2:
        st.metric("Maksimum Harian", f"RM {daily_df['jumlah_kutipan'].max():,.2f}")
    with col3:
        st.metric("Minimum Harian", f"RM {daily_df['jumlah_kutipan'].min():,.2f}")
    
    # Top 5 days
    st.subheader("📅 5 Hari dengan Kutipan Tertinggi")
    top_days = daily_df.nlargest(5, 'jumlah_kutipan')
    for _, row in top_days.iterrows():
        st.write(f"**{row['tarikh_kutipan'].strftime('%d %B %Y')}**: RM {row['jumlah_kutipan']:,.2f}")

# Data table expander
with st.expander("📋 Lihat Data Mentah"):
    st.subheader("Data Bulanan")
    st.dataframe(monthly_df)
    st.subheader("Data Tahunan")
    st.dataframe(yearly_df)
    st.subheader("Data Harian")
    st.dataframe(daily_df)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "iHasil Dashboard | Data dikemaskini: {} | Dibangunkan dengan Streamlit"
    "</div>".format(datetime.now().strftime('%Y-%m-%d')),
    unsafe_allow_html=True
)
