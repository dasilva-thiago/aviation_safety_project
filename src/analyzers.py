"""
Module for statistical analysis and aggregations.
Generates KPIs, trends, and insights from raw data.
Made for demonstration, testing, and learning purposes.
"""

import pandas as pd

class SafetyAnalyzer:
    """Safety data analyzer."""
    
    def __init__(self, df):
        """
        Initialize analyzer with DataFrame.
        
        Args:
            df (DataFrame): Event data
        """
        self.df = df.copy()
        self._prepare_data()
    
    def _prepare_data(self):
        """Prepare data by adding calculated columns."""
        self.df['date_datetime'] = pd.to_datetime(self.df['date'])
        self.df['week_of_year'] = self.df['date_datetime'].dt.isocalendar().week
    
    def calculate_main_kpis(self):
        """
        Calculate main dashboard KPIs.
        
        Returns:
            dict: Dictionary with KPIs
        """
        total = len(self.df)
        critical = len(self.df[self.df['severity'] == 'Critical'])
        high = len(self.df[self.df['severity'] == 'High'])
        
        kpis = {
            'total_events': total,
            'critical_events': critical,
            'high_events': high,
            'safety_rate': round((1 - (critical + high) / total) * 100, 2),
            'total_injuries': int(self.df['injuries'].sum()),
            'avg_resolution_time': round(self.df['resolution_days'].mean(), 1),
            'total_cost_usd': round(self.df['estimated_cost_usd'].sum(), 2),
            'pending_events': len(self.df[
                self.df['status'].isin(['Under Investigation', 'Corrective Action'])
            ]),
            'most_incidents_model': self.df['aircraft_model'].mode()[0],
            'most_common_type': self.df['incident_type'].mode()[0]
        }
        
        return kpis
    
    def analyze_by_aircraft(self):
        """
        Generate aggregated analysis by aircraft model.
        
        Returns:
            DataFrame: Analysis by model
        """
        analysis = self.df.groupby('aircraft_model').agg({
            'event_id': 'count',
            'risk_score': 'mean',
            'estimated_cost_usd': 'sum',
            'resolution_days': 'mean'
        }).rename(columns={
            'event_id': 'total_events'
        }).round(2)
        
        return analysis
    
    def generate_time_trend(self):
        """
        Generate time series of events by month.
        
        Returns:
            DataFrame: Monthly trend
        """
        trend = self.df.groupby(['year', 'month']).size().reset_index(name='events')
        trend['year_month'] = (
            trend['year'].astype(str) + '-' + 
            trend['month'].astype(str).str.zfill(2)
        )
        return trend
    
    def identify_critical_patterns(self):
        """
        Identify patterns in critical events.
        
        Returns:
            dict: Identified patterns
        """
        critical_events = self.df[self.df['severity'].isin(['Critical', 'High'])]
        
        patterns = {
            'most_common_critical_type': critical_events['incident_type'].mode()[0],
            'most_critical_phase': critical_events['flight_phase'].mode()[0],
            'most_incidents_airport': critical_events['airport'].mode()[0],
            'critical_percentage': round(len(critical_events) / len(self.df) * 100, 2)
        }
        
        return patterns