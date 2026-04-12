import streamlit as st
from styles.custom_css import get_metric_card

def display_metrics(metrics):
    """Display key metrics in a row"""
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(
            get_metric_card(
                "💰 Total Keseluruhan",
                f"RM {metrics['total_all_time']:,.2f}",
                "Semua tahun"
            ),
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            get_metric_card(
                f"📊 Tahun {metrics['latest_year']}",
                f"RM {metrics['latest_year_value']:,.2f}",
                "Jumlah kutipan"
            ),
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            get_metric_card(
                "📅 Bulan Terkini",
                f"RM {metrics['latest_month_value']:,.2f}",
                f"Bulan {metrics['latest_month']}/{metrics['latest_month_year']}"
            ),
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            get_metric_card(
                "📆 Hari Terkini",
                f"RM {metrics['latest_day_value']:,.2f}",
                metrics['latest_day_date'].strftime('%d/%m/%Y')
            ),
            unsafe_allow_html=True
        )

def display_top_performers(metrics, title="Top Performers"):
    """Display top and worst performers"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏆 Prestasi Terbaik")
        
        # Best year
        st.markdown(f"""
        <div class="info-box">
            <strong>Tahun Terbaik:</strong><br>
            {int(metrics['best_year']['tahun_kutipan'])}<br>
            RM {metrics['best_year']['jumlah_kutipan']:,.2f}
        </div>
        """, unsafe_allow_html=True)
        
        # Best month if available
        if 'best_month' in metrics:
            st.markdown(f"""
            <div class="info-box">
                <strong>Bulan Terbaik:</strong><br>
                {metrics['best_month']['bulan_kutipan']}/{int(metrics['best_month']['tahun_kutipan'])}<br>
                RM {metrics['best_month']['jumlah_kutipan']:,.2f}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📉 Prestasi Terburuk")
        
        # Worst year
        st.markdown(f"""
        <div class="warning-box">
            <strong>Tahun Terburuk:</strong><br>
            {int(metrics['worst_year']['tahun_kutipan'])}<br>
            RM {metrics['worst_year']['jumlah_kutipan']:,.2f}
        </div>
        """, unsafe_allow_html=True)
        
        # Worst month if available
        if 'worst_month' in metrics:
            st.markdown(f"""
            <div class="warning-box">
                <strong>Bulan Terburuk:</strong><br>
                {metrics['worst_month']['bulan_kutipan']}/{int(metrics['worst_month']['tahun_kutipan'])}<br>
                RM {metrics['worst_month']['jumlah_kutipan']:,.2f}
            </div>
            """, unsafe_allow_html=True)
