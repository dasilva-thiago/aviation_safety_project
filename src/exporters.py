"""
Module responsible for exporting processed data to files.
Saves in CSV and Excel formats for Power BI consumption.
Made for demonstration, testing, and learning purposes.
"""

import pandas as pd
import os
from . import config

class DataExporter:
    """Data exporter to files."""
    
    @staticmethod
    def ensure_folder_exists():
        """Create data folder if it doesn't exist."""
        os.makedirs(config.DATA_FOLDER, exist_ok=True)
    
    @staticmethod
    def export_main_data(df):
        """
        Export main DataFrame to CSV and Excel.
        
        Args:
            df (DataFrame): Complete data
        """
        DataExporter.ensure_folder_exists()
        
        df.to_csv(config.MAIN_DATA_FILE, index=False)
        df.to_excel(config.EXCEL_FILE, index=False)
        
        print(f"✅ Main data saved:")
        print(f"   - {config.MAIN_DATA_FILE}")
        print(f"   - {config.EXCEL_FILE}")
    
    @staticmethod
    def export_kpis(kpis_dict):
        """
        Export KPIs to CSV.
        
        Args:
            kpis_dict (dict): Dictionary with KPIs
        """
        df_kpis = pd.DataFrame([kpis_dict])
        df_kpis.to_csv(config.KPIS_FILE, index=False)
        
        print(f"✅ KPIs saved: {config.KPIS_FILE}")
    
    @staticmethod
    def export_aircraft_analysis(df_analysis):
        """
        Export aircraft analysis to CSV.
        
        Args:
            df_analysis (DataFrame): Aggregated analysis
        """
        df_analysis.to_csv(config.AIRCRAFT_ANALYSIS_FILE)
        
        print(f"✅ Aircraft analysis saved: {config.AIRCRAFT_ANALYSIS_FILE}")
    
    @staticmethod
    def export_trend(df_trend):
        """
        Export time trend to CSV.
        
        Args:
            df_trend (DataFrame): Time series
        """
        df_trend.to_csv(config.TREND_FILE, index=False)
        
        print(f"✅ Monthly trend saved: {config.TREND_FILE}")