# API to Render the Machine Learning Classifier Model Inferences

# Python Libraries
from flask import Flask, request
import numpy as np
import pickle
import pandas as pd

# Creting a Flask Application Instance
app=Flask(__name__)

# Loading the Pre-Trained Classifier Model
pickle_in = open("classifier_model.pkl","rb")
classifier = pickle.load(pickle_in)

# Home Page
@app.route('/')
def home():
    return "Welcome to the Bank Notes Authentication Application..."

# Prediction Results Page
@app.route('/predict', methods=["Get"])
def predict_bank_note_authentication():
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "The Authentication Status of the given Bank Note is " + str(prediction)

# Executing the Python Flask Application
if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000)
    
    
# API URL for a Sample Inference Results
# http://http://127.0.0.1:8000/predict?variance=2&skewness=1&curtosis=4&entropy=2