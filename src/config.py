"""
Configuration settings for aviation safety analysis project.
Defines constants and parameters used throughout the system.
Generates simulated data for demonstration, testing and learning purposes.
"""

from datetime import datetime, timedelta

# Data generation settings
RANDOM_SEED = 42
NUM_EVENTS = 450
PERIOD_DAYS = 365

# Reference dates
END_DATE = datetime.now()
START_DATE = END_DATE - timedelta(days=PERIOD_DAYS)

# aircraft models and their weights for simulation
AIRCRAFT_MODELS = {
    'models': ['E175', 'E190', 'E195-E2', 'E-Jet E2', 'Legacy 600', 'Phenom 300'],
    'weights': [0.25, 0.25, 0.20, 0.15, 0.10, 0.05]
}

# Incident classification (ICAO-based)
INCIDENT_TYPES = {
    'types': [
        'Bird Strike',
        'Severe Turbulence',
        'Minor Technical Failure',
        'Weather Diversion',
        'Ground Damage',
        'Smoke/Fumes',
        'Pressurization',
        'Hydraulic System',
        'Electrical System',
        'Landing Gear',
        'Engines',
        'Avionics',
        'Communication Failure',
        'Runway Incursion',
        'Near Miss'
    ],
    'weights': [0.20, 0.15, 0.12, 0.10, 0.08, 0.06, 0.05, 0.04, 0.04, 
                0.03, 0.03, 0.03, 0.03, 0.02, 0.02]
}

# Severity levels
SEVERITY_LEVELS = ['Low', 'Medium', 'High', 'Critical']

# Possible statuses
STATUS_OPTIONS = ['Under Investigation', 'Corrective Action', 'Resolved', 'Monitoring']

# Flight phases
FLIGHT_PHASES = [
    'Taxi', 'Takeoff', 'Climb', 'Cruise',
    'Descent', 'Approach', 'Landing', 'Post-landing'
]

# Major Brazilian airports (only for better localization in simulations)
BRAZILIAN_AIRPORTS = [
    'GRU - Guarulhos',
    'GIG - Galeão',
    'BSB - Brasília',
    'CGH - Congonhas',
    'SDU - Santos Dumont',
    'CNF - Confins',
    'SSA - Salvador',
    'FOR - Fortaleza',
    'REC - Recife',
    'POA - Porto Alegre',
    'CWB - Curitiba',
    'VCP - Viracopos'
]

# File paths
DATA_FOLDER = 'data'
MAIN_DATA_FILE = f'{DATA_FOLDER}/flight_safety_data.csv'
EXCEL_FILE = f'{DATA_FOLDER}/flight_safety_data.xlsx'
KPIS_FILE = f'{DATA_FOLDER}/safety_kpis.csv'
AIRCRAFT_ANALYSIS_FILE = f'{DATA_FOLDER}/aircraft_analysis.csv'
TREND_FILE = f'{DATA_FOLDER}/monthly_trend.csv'