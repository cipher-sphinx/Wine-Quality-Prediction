import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('stacking_model.pkl', 'rb'))
output = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    features = [
        request.form.get('fixed-acidity'),
        request.form.get('volatile-acidity'),
        request.form.get('citric-acid'),
        request.form.get('residual-sugar'), 
        request.form.get('chlorides'),
        request.form.get('free-sulfur-dioxide'),
        request.form.get('total-sulfur-dioxide'),
        request.form.get('density'),
        request.form.get('pH'),
        request.form.get('sulphates'),
        request.form.get('alcohol')
    ]

    prediction = model.predict([features])[0]
    output = 'High Wine Quality' if prediction == 1 else 'Low Wine Quality'

    return render_template('index.html', prediction_text=f'Predicted output: {output}')


if __name__ == '__main__':
    app.run(debug=True)