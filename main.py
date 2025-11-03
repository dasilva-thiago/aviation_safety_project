# IMPORTANT DISCLAIMER
# ====================
# This project uses SYNTHETIC DATA for educational purposes.
# Data does NOT represent any real actual fleet performance.
# All incidents, costs, and metrics are RANDOMLY GENERATED.

"""
Main execution script for the project.
Orchestrates data generation, analysis, and export.
Made for demonstration, testing, and learning purposes.

Usage:
    python main.py
"""

import sys
from src import config
from src.data_generator import SafetyEventGenerator
from src.risk_calculator import RiskCalculator
from src.analyzers import SafetyAnalyzer
from src.exporters import DataExporter
import pandas as pd

def display_header():
    """Display program header."""
    print("=" * 70)
    print("  FLIGHT SAFETY DATA GENERATOR - Internship Application Project 2026")
    print("=" * 70)
    print()

def display_data_summary(df, kpis):
    """
    Display statistical summary of generated data.
    
    Args:
        df (DataFrame): Complete data
        kpis (dict): Calculated KPIs
    """
    print("\n" + "=" * 70)
    print("  GENERATED DATA SUMMARY")
    print("=" * 70)
    
    print(f"\nPeriod: {df['date'].min()} to {df['date'].max()}")
    print(f" Total events: {len(df)}")
    
    print(f"\n SEVERITY:")
    print(df['severity'].value_counts().to_string())
    
    print(f"\n STATUS:")
    print(df['status'].value_counts().to_string())
    
    print(f"\n BY MODEL:")
    print(df['aircraft_model'].value_counts().to_string())
    
    print(f"\n Total Cost: ${kpis['total_cost_usd']:,.2f}")
    print(f" Average Resolution Time: {kpis['avg_resolution_time']} days")
    print(f" Safety Rate: {kpis['safety_rate']}%")
    print(f"  Pending Events: {kpis['pending_events']}")
    
    print("\n" + "=" * 70)

def main():
    """Main execution function."""
    try:
        display_header()
        
        # Generate raw data
        print("⏳ Step 1/5: Generating safety events...")
        generator = SafetyEventGenerator(seed=config.RANDOM_SEED)
        events = generator.generate_all_events(config.NUM_EVENTS)
        df = pd.DataFrame(events)
        print(f" {len(df)} events generated successfully!")
        
        # Calculate risk scores
        print("\n⏳ Step 2/5: Calculating risk scores...")
        df = RiskCalculator.add_scores_to_dataframe(df)
        df = RiskCalculator.add_classification(df)
        print(" Risk scores calculated!")
        
        # Perform analysess
        print("\n Step 3/5: Running statistical analyses...")
        analyzer = SafetyAnalyzer(df)
        kpis = analyzer.calculate_main_kpis()
        aircraft_analysis = analyzer.analyze_by_aircraft()
        trend = analyzer.generate_time_trend()
        print(" Analyses completed!")
        
        #Export data
        print("\n Step 4/5: Exporting data...")
        DataExporter.export_main_data(df)
        DataExporter.export_kpis(kpis)
        DataExporter.export_aircraft_analysis(aircraft_analysis)
        DataExporter.export_trend(trend)
        print(" All files exported!")
        
        # Display summary
        print("\n Step 5/5: Generating summary...")
        display_data_summary(df, kpis)
        
        print("\n PROCESS COMPLETED SUCCESSFULLY!")
        print("\n Files generated in 'data/' folder:")
        print("   - flight_safety_data.csv")
        print("   - flight_safety_data.xlsx")
        print("   - safety_kpis.csv")
        print("   - aircraft_analysis.csv")
        print("   - monthly_trend.csv")
        print("\n Next step: Import data into Power BI!")
        
        return 0
        
    except Exception as e:
        print(f"\n ERROR: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())