import pickle

model = pickle.load(open('./model/stacking_model.pkl', 'rb'))

def make_prediction(features):
    prediction = model.predict([features])[0]
    output = 'High Wine Quality' if prediction == 1 else 'Low Wine Quality'
    return output
