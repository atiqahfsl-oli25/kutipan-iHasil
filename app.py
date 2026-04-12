import streamlit as st
from styles.custom_css import apply_custom_css
from utils.data_loader import load_all_data
from utils.metrics_calculator import calculate_metrics
from components.sidebar import render_sidebar
from components.metrics import display_metrics

# Page configuration
st.set_page_config(
    page_title="iHasil Dashboard - Kutipan Analysis",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
apply_custom_css()

# Load data
@st.cache_data
def get_data():
    return load_all_data()

monthly_df, daily_df, yearly_df = get_data()

# Calculate metrics
metrics = calculate_metrics(yearly_df, monthly_df, daily_df)

# Render sidebar and get filters
selected_years, date_range = render_sidebar(monthly_df, yearly_df)

# Main header
st.markdown('<div class="main-header">💰 iHasil Dashboard - Analisis Kutipan</div>', unsafe_allow_html=True)

# Display metrics
display_metrics(metrics)

st.markdown("---")

# Navigation info
st.info("👈 Gunakan menu di sebelah kiri untuk menapis data. Pilih tab di bawah untuk analisis terperinci.")

# The main content is handled by the pages
# Each page will be in the pages/ directory and will appear as tabs in the sidebar
