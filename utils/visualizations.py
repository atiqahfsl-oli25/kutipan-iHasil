import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import calendar

def create_yearly_chart(yearly_df, chart_type='line'):
    """Create yearly trend visualization"""
    
    if chart_type == 'line':
        fig = px.line(
            yearly_df,
            x='tahun_kutipan',
            y='jumlah_kutipan',
            title='Trend Kutipan Tahunan',
            labels={'tahun_kutipan': 'Tahun', 'jumlah_kutipan': 'Jumlah Kutipan (RM)'},
            markers=True
        )
        fig.update_traces(line=dict(color='#1E88E5', width=3))
    else:
        fig = px.bar(
            yearly_df,
            x='tahun_kutipan',
            y='jumlah_kutipan',
            title='Kutipan per Tahun',
            labels={'tahun_kutipan': 'Tahun', 'jumlah_kutipan': 'Jumlah Kutipan (RM)'},
            color='jumlah_kutipan',
            color_continuous_scale='Viridis'
        )
    
    fig.update_layout(
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        height=500,
        showlegend=True
    )
    
    return fig

def create_yearly_bar_chart(yearly_df):
    """Create yearly bar chart"""
    fig = px.bar(
        yearly_df,
        x='tahun_kutipan',
        y='jumlah_kutipan',
        title='Kutipan per Tahun',
        labels={'tahun_kutipan': 'Tahun', 'jumlah_kutipan': 'Jumlah Kutipan (RM)'},
        color='jumlah_kutipan',
        color_continuous_scale='Blues'
    )
    return fig

def create_monthly_chart(monthly_df, chart_type='line'):
    """Create monthly trend visualization"""
    
    if chart_type == 'line':
        fig = px.line(
            monthly_df,
            x='date',
            y='jumlah_kutipan',
            title='Trend Kutipan Bulanan',
            labels={'date': 'Tarikh', 'jumlah_kutipan': 'Jumlah Kutipan (RM)'},
            markers=True
        )
        fig.update_traces(line=dict(color='#E91E63', width=2))
    else:
        fig = px.bar(
            monthly_df,
            x='date',
            y='jumlah_kutipan',
            title='Kutipan Bulanan',
            labels={'date': 'Tarikh', 'jumlah_kutipan': 'Jumlah Kutipan (RM)'},
            color='jumlah_kutipan',
            color_continuous_scale='RdYlGn'
        )
    
    return fig

def create_monthly_heatmap(monthly_df):
    """Create monthly heatmap by year"""
    monthly_pivot = monthly_df.pivot_table(
        index='tahun_kutipan',
        columns='bulan_kutipan',
        values='jumlah_kutipan',
        aggfunc='first'
    ).fillna(0)
    
    fig = px.imshow(
        monthly_pivot,
        labels=dict(x="Bulan", y="Tahun", color="Kutipan (RM)"),
        title="Heatmap Kutipan Bulanan",
        aspect="auto",
        color_continuous_scale='RdYlGn'
    )
    
    return fig

def create_seasonal_chart(monthly_df):
    """Create seasonal analysis chart"""
    monthly_avg = monthly_df.groupby('bulan_kutipan')['jumlah_kutipan'].mean().reset_index()
    monthly_avg['bulan_name'] = monthly_avg['bulan_kutipan'].apply(lambda x: calendar.month_name[x][:3])
    
    fig = px.bar(
        monthly_avg,
        x='bulan_name',
        y='jumlah_kutipan',
        title='Purata Kutipan mengikut Bulan',
        labels={'bulan_name': 'Bulan', 'jumlah_kutipan': 'Purata Kutipan (RM)'},
        color='jumlah_kutipan',
        color_continuous_scale='Blues'
    )
    
    return fig

def create_daily_chart(daily_df):
    """Create daily trend visualization"""
    fig = px.line(
        daily_df,
        x='tarikh_kutipan',
        y='jumlah_kutipan',
        title='Kutipan Harian',
        labels={'tarikh_kutipan': 'Tarikh', 'jumlah_kutipan': 'Jumlah Kutipan (RM)'},
        markers=True
    )
    fig.update_traces(line=dict(color='#FF9800', width=2))
    fig.update_layout(hovermode='x unified')
    
    return fig

def create_moving_average_chart(daily_df, window=7):
    """Create chart with moving average"""
    daily_df = daily_df.copy()
    daily_df[f'MA{window}'] = daily_df['jumlah_kutipan'].rolling(window=window).mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=daily_df['tarikh_kutipan'],
        y=daily_df['jumlah_kutipan'],
        mode='lines+markers',
        name='Kutipan Harian',
        line=dict(color='lightblue', width=1),
        marker=dict(size=4)
    ))
    fig.add_trace(go.Scatter(
        x=daily_df['tarikh_kutipan'],
        y=daily_df[f'MA{window}'],
        mode='lines',
        name=f'Moving Average ({window} hari)',
        line=dict(color='red', width=3)
    ))
    
    fig.update_layout(
        title=f'Trend Kutipan dengan Moving Average ({window} Hari)',
        xaxis_title='Tarikh',
        yaxis_title='Jumlah Kutipan (RM)',
        hovermode='x unified'
    )
    
    return fig

def create_growth_chart(yearly_df):
    """Create year-over-year growth chart"""
    yearly_df = yearly_df.copy()
    yearly_df['growth'] = yearly_df['jumlah_kutipan'].pct_change() * 100
    
    fig = px.bar(
        yearly_df.dropna(),
        x='tahun_kutipan',
        y='growth',
        title='Pertumbuhan Tahun ke Tahun (%)',
        labels={'tahun_kutipan': 'Tahun', 'growth': 'Pertumbuhan (%)'},
        color='growth',
        color_continuous_scale='RdYlGn'
    )
    
    return fig

def create_cumulative_chart(yearly_df):
    """Create cumulative sum chart"""
    yearly_df = yearly_df.copy()
    yearly_df['cumulative'] = yearly_df['jumlah_kutipan'].cumsum()
    
    fig = px.area(
        yearly_df,
        x='tahun_kutipan',
        y='cumulative',
        title='Kutipan Kumulatif Sepanjang Masa',
        labels={'tahun_kutipan': 'Tahun', 'cumulative': 'Kumulatif (RM)'},
        color_discrete_sequence=['#2196F3']
    )
    
    return fig

def create_correlation_heatmap(df):
    """Create correlation heatmap for numeric columns"""
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    if len(numeric_df.columns) > 1:
        corr = numeric_df.corr()
        fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            color_continuous_scale='RdBu',
            title="Correlation Heatmap"
        )
        return fig
    return None
