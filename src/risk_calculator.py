"""
Module for calculating risk scores and safety metrics.
Implements algorithms for severity and probability assessment.
Made for demonstration, testing, and learning purposes.
"""

import pandas as pd

class RiskCalculator:
    """Risk score calculator for safety events."""
    
    @staticmethod
    def calculate_individual_score(event):
        """
        Calculate risk score for an individual event.
        
        Score based on multiple factors:
        - Severity (0-40 points)
        - Injuries (0-20 points)
        - Damage (0-20 points)
        - Flight phase (0-10 points)
        - Status (0-10 points)
        
        Args:
            event (dict or Series): Event data
            
        Returns:
            int: Risk score (0-100)
        """
        score = 0
        
        # Severity (higher weight)
        severity_scores = {
            'Critical': 40,
            'High': 30,
            'Medium': 20,
            'Low': 10
        }
        score += severity_scores.get(event['severity'], 0)
        
        # Injuries
        if event['injuries'] > 0:
            score += 20
        
        # Aircraft damage
        damage_scores = {
            'Severe': 20,
            'Significant': 15,
            'Moderate': 10,
            'Minor': 5,
            'None': 0
        }
        score += damage_scores.get(event['aircraft_damage'], 0)
        
        # Critical flight phase (takeoff and landing are riskier)
        if event['flight_phase'] in ['Takeoff', 'Landing']:
            score += 10
        
        # Status (events under investigation = unknown risk)
        if event['status'] == 'Under Investigation':
            score += 10
        
        return min(score, 100)  # Cap at 100
    
    @staticmethod
    def add_scores_to_dataframe(df):
        """
        Add risk score column to DataFrame.
        
        Args:
            df (DataFrame): DataFrame with events
            
        Returns:
            DataFrame: DataFrame with 'risk_score' column added
        """
        df['risk_score'] = df.apply(
            RiskCalculator.calculate_individual_score,
            axis=1
        )
        return df
    
    @staticmethod
    def classify_risk(score):
        """
        Classify risk into categories.
        
        Args:
            score (int): Risk score
            
        Returns:
            str: Risk category
        """
        if score >= 70:
            return 'Very High'
        elif score >= 50:
            return 'High'
        elif score >= 30:
            return 'Moderate'
        else:
            return 'Low'
    
    @staticmethod
    def add_classification(df):
        """
        Add risk classification to DataFrame.
        
        Args:
            df (DataFrame): DataFrame with risk_score
            
        Returns:
            DataFrame: DataFrame with 'risk_classification' column
        """
        df['risk_classification'] = df['risk_score'].apply(
            RiskCalculator.classify_risk
        )
        return df