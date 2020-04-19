# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/predictmlp', methods=['POST'])
def predict():
    if mlp:
        try:
            json_ = request.json
            print(json_)
            query = pd.DataFrame(json_)
            # query = query.reindex(columns=model_columns, fill_value=0)
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(mlp.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 3000 # If you don't provide any port the port will be set to 12345

    mlp = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print(model_columns)
    print ('Model columns loaded')

    app.run(port=port, debug=True)