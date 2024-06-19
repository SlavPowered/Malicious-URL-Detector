from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import extract_attrs
import pandas as pd

app = Flask(__name__)
CORS(app)

with open("rf_model.sav", "rb") as file:
    knn_loaded = pickle.load(file)

@app.route("/eval")
def evaluate_url():
    url = request.args.get('target')
    
    evaluation = evaluate(url)
    
    print("------------------------")
    print(url)
    print("------------------------")
    print("Malicious: ", evaluation)
    print("------------------------")

    return jsonify({'prediction': evaluation})
    
def evaluate(url: str)-> bool:
    url_attrs = pd.DataFrame([extract_attrs.get_attributes(url, False)], columns=extract_attrs.feature_names)
    prediction = knn_loaded.predict(url_attrs)
    if prediction[0] == 0:
        return False
    elif prediction[0] == 1:
        return True
    else:
        print(f"Unexpected Prediction: {prediction}")
        return False