import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
# In a real app, this would query from the database
# from src.core.database import db

class PredictiveAnalyticsService:
    @staticmethod
    def forecast_bed_occupancy(historical_data_days=30, forecast_days=7):
        """
        Uses simple linear regression to forecast hospital bed occupancy
        for the next `forecast_days` based on the past `historical_data_days`.
        """
        
        # 1. Fetch historical occupancy data from DB (Mocked here for demonstration)
        # SELECT date, count(id) FROM encounters WHERE status='ACTIVE' GROUP BY date
        dates = [datetime.today() - timedelta(days=i) for i in range(historical_data_days, 0, -1)]
        # Simulated occupancy data with an upward trend and some noise
        base_occupancy = 150
        occupancy_data = [base_occupancy + (i * 0.5) + np.random.randint(-10, 10) for i in range(historical_data_days)]
        
        df = pd.DataFrame({
            'date': dates,
            'day_index': range(historical_data_days),
            'occupancy': occupancy_data
        })

        # 2. Train Linear Regression Model
        X = df[['day_index']]
        y = df['occupancy']
        
        model = LinearRegression()
        model.fit(X, y)

        # 3. Predict future occupancy
        future_indices = pd.DataFrame({
            'day_index': range(historical_data_days, historical_data_days + forecast_days)
        })
        
        predictions = model.predict(future_indices)
        
        # 4. Format results
        forecast = []
        for i, pred in enumerate(predictions):
            forecast_date = datetime.today() + timedelta(days=i+1)
            forecast.append({
                'date': forecast_date.strftime('%Y-%m-%d'),
                'predicted_occupancy': int(max(0, pred)) # Cannot have negative beds
            })
            
        return {
            'model_confidence_r2': round(model.score(X, y), 2),
            'forecast': forecast
        }
