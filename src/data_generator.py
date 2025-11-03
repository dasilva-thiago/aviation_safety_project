# IMPORTANT DISCLAIMER
# ====================
# This project uses SYNTHETIC DATA for educational purposes.
# Data does NOT represent any real actual fleet performance.
# All incidents, costs, and metrics are RANDOMLY GENERATED.

"""
Module responsible for generating synthetic safety event data.
Simulates realistic records based on commercial aviation patterns.
Made for demonstration, testing, and learning purposes.
"""

import numpy as np
import pandas as pd
import random
from datetime import timedelta
from . import config

class SafetyEventGenerator:
    """Generator for aviation safety events."""
    
    def __init__(self, seed=None):
        """
        Initialize the generator.
        
        Args:
            seed (int, optional): Seed for reproducibility
        """
        if seed:
            np.random.seed(seed)
            random.seed(seed)
        
        self.generated_dates = []
        self.events = []
    
    def generate_random_dates(self, num_events):
        """
        Generate random dates within the defined period.
        
        Args:
            num_events (int): Number of events to generate
            
        Returns:
            list: Sorted list of dates
        """
        dates = []
        for _ in range(num_events):
            days = random.randint(0, config.PERIOD_DAYS)
            date = config.START_DATE + timedelta(days=days)
            dates.append(date)
        
        self.generated_dates = sorted(dates)
        return self.generated_dates
    
    def determine_severity(self, incident_type):
        """
        Determine severity based on incident type.
        
        Args:
            incident_type (str): Type of incident
            
        Returns:
            str: Severity level
        """
        # Critical incidents by nature
        if incident_type in ['Near Miss', 'Runway Incursion', 'Engines']:
            return np.random.choice(['High', 'Critical'], p=[0.6, 0.4])
        
        # Generally minor incidents
        elif incident_type in ['Bird Strike', 'Weather Diversion', 'Ground Damage']:
            return np.random.choice(['Low', 'Medium'], p=[0.7, 0.3])
        
        # Variable technical incidents
        elif incident_type in ['Minor Technical Failure', 'Communication Failure']:
            return np.random.choice(['Low', 'Medium', 'High'], p=[0.6, 0.3, 0.1])
        
        # Other cases - general distribution
        else:
            return np.random.choice(config.SEVERITY_LEVELS, p=[0.4, 0.35, 0.20, 0.05])
    
    def calculate_resolution_time(self, severity, days_since_event):
        """
        Calculate estimated resolution time based on severity and event age.
        
        Args:
            severity (str): Severity level
            days_since_event (int): Days since the event
            
        Returns:
            int or None: Days to resolution (None if still open)
        """
        # Define time range by severity
        ranges = {
            'Low': (1, 15),
            'Medium': (10, 45),
            'High': (30, 90),
            'Critical': (60, 180)
        }
        
        base_time = np.random.randint(*ranges[severity])
        
        # Recent events may not be resolved
        if days_since_event < base_time * 0.5:
            return None  # Still in progress
        
        return base_time
    
    def determine_status(self, days_since_event, resolution_time):
        """
        Determine current status of the event.
        
        Args:
            days_since_event (int): Days since the event
            resolution_time (int): Time to resolve
            
        Returns:
            str: Current status
        """
        if resolution_time is None:
            # Recent events without resolution
            if days_since_event < 30:
                return np.random.choice(
                    ['Under Investigation', 'Corrective Action'], 
                    p=[0.6, 0.4]
                )
            else:
                return np.random.choice(
                    ['Under Investigation', 'Corrective Action'], 
                    p=[0.3, 0.7]
                )
        else:
            # Events with defined resolution time
            if days_since_event >= resolution_time:
                return np.random.choice(['Resolved', 'Monitoring'], p=[0.8, 0.2])
            else:
                return 'Corrective Action'
    
    def calculate_consequences(self, severity):
        """
        Calculate event consequences based on severity.
        
        Args:
            severity (str): Severity level
            
        Returns:
            dict: Dictionary with injuries, damage, and delay
        """
        if severity in ['Critical', 'High']:
            injuries = random.choice([0, 0, 0, 1, 2])
            damage = random.choice(['Moderate', 'Significant', 'Severe'])
            delay = np.random.randint(120, 600)
        elif severity == 'Medium':
            injuries = 0
            damage = random.choice(['None', 'Minor', 'Moderate'])
            delay = np.random.randint(30, 180)
        else:  # Low
            injuries = 0
            damage = random.choice(['None', 'None', 'Minor'])
            delay = np.random.randint(0, 60)
        
        return {
            'injuries': injuries,
            'aircraft_damage': damage,
            'delay_minutes': delay
        }
    
    def calculate_cost(self, severity, damage):
        """
        Estimate incident cost.
        
        Args:
            severity (str): Severity level
            damage (str): Damage level
            
        Returns:
            float: Estimated cost in USD
        """
        if severity in ['High', 'Critical']:
            return round(random.uniform(10000, 500000), 2)
        elif damage in ['Severe', 'Significant']:
            return round(random.uniform(5000, 150000), 2)
        else:
            return round(random.uniform(100, 50000), 2)
    
    def generate_event(self, idx, date):
        """
        Generate a complete individual event.
        
        Args:
            idx (int): Event index
            date (datetime): Event date
            
        Returns:
            dict: Dictionary with event data
        """
        # Select basic characteristics
        incident_type = np.random.choice(
            config.INCIDENT_TYPES['types'],
            p=config.INCIDENT_TYPES['weights']
        )
        severity = self.determine_severity(incident_type)
        model = np.random.choice(
            config.AIRCRAFT_MODELS['models'],
            p=config.AIRCRAFT_MODELS['weights']
        )
        
        # Calculate time and status
        days_since = (config.END_DATE - date).days
        resolution_time = self.calculate_resolution_time(severity, days_since)
        status = self.determine_status(days_since, resolution_time)
        
        # Calculate consequences
        consequences = self.calculate_consequences(severity)
        cost = self.calculate_cost(severity, consequences['aircraft_damage'])
        
        # Build event
        event = {
            'event_id': f'EVT{idx+1:04d}',
            'date': date.strftime('%Y-%m-%d'),
            'time': f'{random.randint(0,23):02d}:{random.randint(0,59):02d}',
            'aircraft_model': model,
            'registration': f'PR-{model[:3].upper()}{random.randint(100,999)}',
            'incident_type': incident_type,
            'severity': severity,
            'flight_phase': np.random.choice(config.FLIGHT_PHASES),
            'airport': np.random.choice(config.BRAZILIAN_AIRPORTS),
            'status': status,
            'resolution_days': resolution_time,
            'injuries': consequences['injuries'],
            'aircraft_damage': consequences['aircraft_damage'],
            'delay_minutes': consequences['delay_minutes'],
            'investigator': f'INV{random.randint(1,15):02d}',
            'immediate_action': random.choice(['Yes', 'No']),
            'anac_notification': random.choice(['Yes', 'Yes', 'No']),
            'estimated_cost_usd': cost,
            'month': date.month,
            'year': date.year,
            'quarter': f'Q{(date.month-1)//3 + 1}',
            'day_of_week': date.strftime('%A')
        }
        
        return event
    
    def generate_all_events(self, num_events):
        """
        Generate complete set of events.
        
        Args:
            num_events (int): Total number of events
            
        Returns:
            list: List of generated events
        """
        dates = self.generate_random_dates(num_events)
        
        self.events = [
            self.generate_event(i, date) 
            for i, date in enumerate(dates)
        ]
        
        return self.events