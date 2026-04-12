import streamlit as st
from datetime import datetime

def render_sidebar(monthly_df, yearly_df):
    """Render sidebar with filters and information"""
    
    with st.sidebar:
        st.markdown("## 🔍 iHasil Dashboard")
        st.markdown("---")
        
        # Year filter
        min_year = int(yearly_df['tahun_kutipan'].min())
        max_year = int(yearly_df['tahun_kutipan'].max())
        
        selected_years = st.multiselect(
            "📅 Pilih Tahun",
            options=list(range(max_year, min_year-1, -1)),
            default=[max_year],
            help="Pilih tahun untuk analisis"
        )
        
        # Date range for monthly data
        st.markdown("### 📆 Rentang Waktu Bulanan")
        date_range = st.date_input(
            "Pilih rentang tarikh",
            value=[monthly_df['date'].min(), monthly_df['date'].max()],
            min_value=monthly_df['date'].min(),
            max_value=monthly_df['date'].max(),
            help="Pilih julat tarikh untuk data bulanan"
        )
        
        st.markdown("---")
        
        # Dashboard info
        with st.expander("ℹ️ Maklumat Dashboard"):
            st.markdown("""
            **iHasil Collection Dashboard**
            
            Dashboard ini memaparkan analisis kutipan iHasil dari tahun 2001 hingga 2026.
            
            **Data Sources:**
            - Data Bulanan
            - Data Harian  
            - Data Tahunan
            
            **Features:**
            - Trend analysis
            - Seasonal patterns
            - Growth metrics
            - Forecasting
            """)
        
        st.markdown("---")
        st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        return selected_years, date_range
