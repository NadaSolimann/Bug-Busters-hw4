from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     G1 = request.args.get('G1')
     G2 = request.args.get('G2')
     absences = request.args.get('absences')
     data = [[G1],[G2],[absences]]
     query_df = pd.DataFrame({ 'G1' : [G1] ,'G2' : [G2] ,'absences' : [absences]})
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)
