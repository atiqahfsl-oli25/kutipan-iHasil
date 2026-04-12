import pandas as pd
import numpy as np

def calculate_metrics(yearly_df, monthly_df, daily_df):
    """Calculate key metrics for the dashboard"""
    
    metrics = {}
    
    # Total all time
    metrics['total_all_time'] = yearly_df['jumlah_kutipan'].sum()
    
    # Latest year
    latest_year = yearly_df['tahun_kutipan'].max()
    metrics['latest_year'] = latest_year
    metrics['latest_year_value'] = yearly_df[yearly_df['tahun_kutipan'] == latest_year]['jumlah_kutipan'].values[0]
    
    # Latest month
    if not monthly_df.empty:
        metrics['latest_month_value'] = monthly_df.iloc[0]['jumlah_kutipan']
        metrics['latest_month'] = monthly_df.iloc[0]['bulan_kutipan']
        metrics['latest_month_year'] = monthly_df.iloc[0]['tahun_kutipan']
    
    # Latest day
    if not daily_df.empty:
        metrics['latest_day_value'] = daily_df.iloc[-1]['jumlah_kutipan']
        metrics['latest_day_date'] = daily_df.iloc[-1]['tarikh_kutipan']
    
    # Averages
    metrics['avg_yearly'] = yearly_df['jumlah_kutipan'].mean()
    metrics['avg_monthly'] = monthly_df['jumlah_kutipan'].mean()
    metrics['avg_daily'] = daily_df['jumlah_kutipan'].mean() if not daily_df.empty else 0
    
    # Best and worst
    metrics['best_year'] = yearly_df.loc[yearly_df['jumlah_kutipan'].idxmax()]
    metrics['worst_year'] = yearly_df.loc[yearly_df['jumlah_kutipan'].idxmin()]
    
    if not monthly_df.empty:
        metrics['best_month'] = monthly_df.loc[monthly_df['jumlah_kutipan'].idxmax()]
        metrics['worst_month'] = monthly_df.loc[monthly_df['jumlah_kutipan'].idxmin()]
    
    if not daily_df.empty:
        metrics['best_day'] = daily_df.loc[daily_df['jumlah_kutipan'].idxmax()]
        metrics['worst_day'] = daily_df.loc[daily_df['jumlah_kutipan'].idxmin()]
    
    return metrics

def calculate_growth(yearly_df):
    """Calculate year-over-year growth"""
    yearly_df = yearly_df.copy()
    yearly_df['growth'] = yearly_df['jumlah_kutipan'].pct_change() * 100
    yearly_df['growth_amount'] = yearly_df['jumlah_kutipan'].diff()
    
    return yearly_df

def calculate_moving_average(daily_df, window=7):
    """Calculate moving average for daily data"""
    daily_df = daily_df.copy()
    daily_df[f'MA{window}'] = daily_df['jumlah_kutipan'].rolling(window=window).mean()
    return daily_df

def calculate_cumulative(yearly_df):
    """Calculate cumulative sum"""
    yearly_df = yearly_df.copy()
    yearly_df['cumulative'] = yearly_df['jumlah_kutipan'].cumsum()
    return yearly_df

def get_seasonal_stats(monthly_df):
    """Calculate seasonal statistics by month"""
    monthly_avg = monthly_df.groupby('bulan_kutipan')['jumlah_kutipan'].agg(['mean', 'median', 'std']).reset_index()
    monthly_avg.columns = ['bulan', 'purata', 'median', 'std']
    return monthly_avg
