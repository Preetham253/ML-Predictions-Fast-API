'''
This is the service layer of FastAPI project. Its responsibility is to:
1. Load the trained machine learning model.
2. Accept input data from the API
3. Check if the prediction already exists in Redis
4. If yes, return the cached prediction
5. Otherwise, make a new prediction, cache it, and return it
'''
'''
                User
                  │
                  ▼
        POST /predict
                  │
                  ▼
      predict_car_price(data)
                  │
                  ▼
      Generate cache_key
                  │
                  ▼
          Check Redis Cache
           ┌───────────────┐
           │               │
      Cache Hit       Cache Miss
           │               │
           ▼               ▼
 Return cached      Convert dict
   prediction        to DataFrame
                           │
                           ▼
                    ML Model Predict
                           │
                           ▼
                 Store result in Redis
                           │
                           ▼
                   Return prediction
'''


import joblib
import pandas as pd
from app.core.config import settings

from app.cache.redis_cache import (
    set_cached_prediction,
    get_cached_prediction
)

# Load the model
model = joblib.load(settings.MODEL_PATH)
def predict_car_price(data:dict):
    cache_key = " ".join([str(val) for val in data.values()])
    cached = get_cached_prediction(cache_key)
    if cached:
        return cached
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    set_cached_prediction(cache_key,prediction)
    return prediction
