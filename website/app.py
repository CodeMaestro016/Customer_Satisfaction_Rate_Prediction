from flask import Flask, render_template, request, jsonify
import pandas as pd
from catboost import CatBoostClassifier
import pickle
import os

app = Flask(__name__)


# Load the CatBoost model
try:
    model_path = 'website/model/catboost_model.pkl'
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file {model_path} not found")
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

# Define satisfaction mapping (based on your model's y variables: {'High': 0, 'Low': 1, 'Medium': 2})
satisfaction_mapping = {
    0: 'High',
    1: 'Low',
    2: 'Medium'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'success': False, 'error': 'Model not loaded. Please check server configuration.'}), 500

    try:
        # Get JSON data from request
        data = request.get_json()

        # Map form field names to model feature names (based on Colab testing code)
        input_data = {
            'Age': float(data.get('age', 0)),
            'Gender': data.get('gender', ''),
            'Occupation': data.get('occupation', ''),
            'Travel_Class': data.get('travel_class', ''),
            'State_of_Residence': data.get('state_of_residence', ''),
            'Duration_of_Stay_(Days)': float(data.get('duration_of_stays', 0)),
            'Number_of_Companions': float(data.get('number_of_companions', 0)),
            'Purpose_of_Travel': data.get('purpose_of_travel', ''),
            'Special_Requests': ', '.join(data.get('special_request', [])) if data.get('special_request') else 'No',
            'Loyalty_Program_Member': data.get('loyalty_program_member', ''),
            'Total_Price': float(data.get('total_price', 0)),
            'Destination_City': data.get('destination_city', ''),
            'Destination_Country': data.get('destination_country', ''),
            'Days_Before_Travel': float(data.get('days_before_travel', 0))
        }

        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Map prediction to satisfaction category
        satisfaction_class = satisfaction_mapping.get(int(prediction), 'Unknown')

        # Determine satisfaction score and color based on prediction
        # Assuming a normalized score between 1.0 and 5.0 for display
        score_map = {
            'High': 4.5,
            'Medium': 3.0,
            'Low': 1.5,
            'Unknown': 3.0
        }
        color_map = {
            'High': 'success',
            'Medium': 'info',
            'Low': 'danger',
            'Unknown': 'warning'
        }

        satisfaction_score = score_map.get(satisfaction_class, 3.0)
        color = color_map.get(satisfaction_class, 'warning')

        return jsonify({
            'success': True,
            'satisfaction_score': round(satisfaction_score, 2),
            'satisfaction_class': satisfaction_class,
            'color': color
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


















    