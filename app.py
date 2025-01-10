from fastapi import FastAPI
from bigmartvariables import bigmartsalespredict
import pandas as pd
import joblib
import uvicorn

# Create the App object
big_mart_sales_app = FastAPI()

# Load model from local disc
filename = 'Bigmart_pred_gam_model.sav'
loaded_model = joblib.load(filename)

# Create the get and index method to open automatically on a server
@big_mart_sales_app.get("/")
def index():
    return {'message': 'Hello'}

# Expose the prediction functionality, to make predictions
@big_mart_sales_app.post('/predict')
def predict_sales(data: bigmartsalespredict):
    data = data.dict()
    print(data)
    data = pd.DataFrame([data])
    print(data.head())

    prediction = loaded_model.predict(data)
    print(str(prediction))
    return str(prediction)

if __name__ == '__main__':
    uvicorn.run("app:big_mart_sales_app", host= '127.0.0.1', port=8000, reload = True)