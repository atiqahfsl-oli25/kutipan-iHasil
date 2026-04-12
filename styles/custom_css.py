import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling to the dashboard"""
    st.markdown("""
        <style>
        .main-header {
            font-size: 2.5rem;
            color: #1E88E5;
            text-align: center;
            padding: 1rem;
            background: linear-gradient(90deg, #1E88E5, #64B5F6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
        }
        .sub-header {
            font-size: 1.5rem;
            color: #2C3E50;
            padding: 0.5rem;
            border-left: 4px solid #1E88E5;
            margin: 1rem 0;
            font-weight: 600;
        }
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem;
            border-radius: 10px;
            color: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s;
        }
        .metric-card:hover {
            transform: translateY(-5px);
        }
        .metric-card h3 {
            margin: 0;
            font-size: 1rem;
            opacity: 0.9;
        }
        .metric-card h2 {
            margin: 0.5rem 0;
            font-size: 1.8rem;
            font-weight: bold;
        }
        .metric-card small {
            opacity: 0.8;
        }
        .insight-box {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #28a745;
            margin: 1rem 0;
        }
        .info-box {
            background-color: #e3f2fd;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #2196f3;
            margin: 1rem 0;
        }
        .warning-box {
            background-color: #fff3e0;
            padding: 1rem;
            border-radius: 10px;
            border-left: 4px solid #ff9800;
            margin: 1rem 0;
        }
        .footer {
            text-align: center;
            color: gray;
            padding: 1rem;
            margin-top: 2rem;
            border-top: 1px solid #e0e0e0;
        }
        .stButton > button {
            background: linear-gradient(90deg, #1E88E5, #64B5F6);
            color: white;
            border: none;
            padding: 0.5rem 2rem;
            border-radius: 5px;
            transition: transform 0.3s;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

def get_metric_card(title, value, subtitle=""):
    """Return HTML for metric card"""
    return f"""
    <div class="metric-card">
        <h3>{title}</h3>
        <h2>{value}</h2>
        <small>{subtitle}</small>
    </div>
    """
