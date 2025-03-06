from prophet import Prophet
import pandas as pd

def predict_keyword_trend(data):
    """Uses Facebook Prophet to predict future keyword popularity"""
    df = data.reset_index()[['date', data.columns[1]]]
    df.columns = ['ds', 'y']  # Prophet requires 'ds' (date) and 'y' (value)

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=90)  # Predict next 3 months
    forecast = model.predict(future)

    return forecast[['ds', 'yhat']]

# Testing
if __name__ == "__main__":
    from trends.py import get_trending_keywords
    trend_data = get_trending_keywords("AI Marketing")
    if trend_data is not None:
        prediction = predict_keyword_trend(trend_data)
        print(prediction)
