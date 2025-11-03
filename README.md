# aviation_safety_project
This is a coding project for an aeronautical operational safety event monitoring system, simulating a control room that monitors incidents, trends and criticality levels in real time using simulated data.

**This project contains SYNTHETIC DATA for demonstration purposes only.**

- All data is randomly generated using Python coding
- **NO data represents any actual real aircraft performance**
- **NO data reflects real safety incidents or records**
- All metrics, costs, and incidents are FICTIONAL

This is a portfolio project to demonstrate:
- Data analysis skills
- Power BI dashboard design
- Python programming proficiency

## Overview

This project generates synthetic aviation safety event data and provides statistical analysis tools for monitoring aircraft operational safety, specifically focused on fleet operations.

## Technologies

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **OpenPyXL**: Excel file generation

## Installation
```bash

git clone https://github.com/dasilva-thiago/aviation-safety-analysis


cd aviation-safety-analysis


pip install -r requirements.txt
```

##  Usage
```bash
# Run main script
python main.py
```

This will generate:
- `flight_safety_data.csv` - Main dataset
- `flight_safety_data.xlsx` - Excel format
- `safety_kpis.csv` - Key performance indicators
- `aircraft_analysis.csv` - Analysis by aircraft model
- `monthly_trend.csv` - Time series data

## Data Structure

### Main Dataset Fields

- `event_id`: Unique event identifier
- `date`: Event date
- `aircraft_model`: Embraer model (E175, E190, E195-E2, etc.)
- `incident_type`: Classification (Bird Strike, Technical Failure, etc.)
- `severity`: Level (Low, Medium, High, Critical)
- `flight_phase`: Phase when occurred (Takeoff, Cruise, Landing, etc.)
- `status`: Current status (Under Investigation, Resolved, etc.)
- `risk_score`: Calculated risk score (0-100)

## Power BI Integration

1. Open Power BI Desktop
2. Get Data → Text/CSV
3. Select `flight_safety_data.csv`
4. Load and start building visualizations

## Module Structure

- `config.py`: Configuration settings and constants
- `data_generator.py`: Synthetic data generation engine
- `risk_calculator.py`: Risk scoring algorithms
- `analyzers.py`: Statistical analysis functions
- `exporters.py`: Data export utilities

## Author

**Thiago da Silva**  
Tech student and aspiring software developer. Eager to contribute to meaningful projects with others who share the same passion.
Computer Engineering Student — UNIVESP
IT Technician — SENAC

Developed for Internship Application - November 2026 :D 

## Contact

- LinkedIn: [linkedin.com/in/thiago-da-silva-876805269](...)
- GitHub: [github.com/dasilva-thiago](...)