from fastapi import FastAPI
from propertyvariables import realestatepricepredict
import pandas as pd
import joblib
import uvicorn

# Creating the App object
real_estate_pred_app = FastAPI()

# Load the model from local disc
filename = 'Data\property_price_prediction.sav'
loaded_model = joblib.load(filename)

# Create the get and index method to open automatically on a server
@real_estate_pred_app.get('/')
def index():
    return {'message': 'Hello, world!'}

# Expose the prediction functionality, to make predictions
# from the passed JSON data and return the prdecited price 
# along with the predicted intervals http://127.0.0.1:8000
# http://127.0.0.1:8000/docs
@real_estate_pred_app.post('/predict')
def predict_price(data: realestatepricepredict):
    data = data.dict()
    print(data)
    data = pd.DataFrame([data])
    print(data.head())

    prediction = loaded_model.predict(data)
    print(str(prediction))
    return str(prediction)

if __name__ == '__main__':
    uvicorn.run("app:real_estate_pred_app", host='127.0.0.1', port=8000, reload = True)