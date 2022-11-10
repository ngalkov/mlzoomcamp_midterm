import pickle
import numpy as np
from pathlib import Path

from flask import Flask, request, jsonify

import xgboost as xgb


MODELS_DIR = './models'


model_path = Path(MODELS_DIR) / 'model.bin'
with open(model_path, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('concrete_strength_est')


@app.route('/predict', methods=['POST'])
def predict():
    sample = request.get_json()
    print(sample)
    dval = xgb.DMatrix([np.array(sample)])
    strength = model.predict(dval)
    result = {
        'strength': float(strength[0])
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)