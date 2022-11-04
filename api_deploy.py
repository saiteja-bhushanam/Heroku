# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    Daily_Time: float
    Age:int
    Area_Income: float
    DailyInternetUsage: float
    Male: int
    
ad_clicked_model= pickle.load(open('model.sav','rb'))

@app.post('/ad_click_prediction')
def click_pred(input_parameters: model_input):
    input_data=input_parameters.json()
    input_dict=json.loads(input_data)

    daily_time = input_dict['Daily_Time']
    age=input_dict['age']
    income=input_dict['Area_Income']
    Internet=input_dict['DailyInternetUsage']
    male=input_dict['Male']
    
    input_list=[daily_time,age,income,Internet,male]
    
    prediction=ad_clicked_model.predict([input_list])
    
    if prediction[0]==1:
        return 'Clicked the ad'
    else:
        return "didn't click the ad"
    
    