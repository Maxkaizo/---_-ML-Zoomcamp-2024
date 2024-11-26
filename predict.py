import pickle
from flask import Flask
from flask import request
from flask import jsonify

input_file = 'model_C=1.0_T=0.7.bin'

with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)

app = Flask('dropout')

@app.route('/predict', methods=['POST'])
def predict():
  student = request.get_json()  

  X = dv.transform([student])
  y_pred = model.predict_proba(X)[0, 1]
  dropout = y_pred >= 0.7

  result= {
     'dropout_probability' : float(y_pred),
     'dropout' : bool(dropout)
  }
  return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
