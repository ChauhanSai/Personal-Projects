import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import MultiHeadAttention
import joblib  # For saving and loading the scaler

# Load the fitted scaler and level_mapping
scaler = joblib.load('model/severityScaler.pkl')  # Load the scaler saved during training
level_mapping = {'Low': 0, 'Medium': 1, 'High': 2}  # Replace with the actual mapping used during training

def predict(patient_data):
    # Load the model
    model = load_model('model/severityModel.h5', custom_objects={'MultiHeadAttention': MultiHeadAttention})

    # Define the expected column names
    column_names = [
        'Age', 'Gender', 'Air Pollution', 'Alcohol use', 'Dust Allergy', 'OccuPational Hazards',
        'Genetic Risk', 'chronic Lung Disease', 'Balanced Diet', 'Obesity', 'Smoking',
        'Passive Smoker', 'Chest Pain', 'Coughing of Blood', 'Fatigue', 'Weight Loss',
        'Shortness of Breath', 'Wheezing', 'Swallowing Difficulty', 'Clubbing of Finger Nails',
        'Frequent Cold', 'Dry Cough', 'Snoring'
    ]

    # Convert input data to a DataFrame with the correct column names
    patient_df = pd.DataFrame([patient_data], columns=column_names)
    patient_df_scaled = scaler.transform(patient_df)

    # Make predictions
    predictions = model.predict(patient_df_scaled)
    predicted_class = np.argmax(predictions, axis=1)[0]

    # Map the predicted class back to the original labels
    reverse_mapping = {v: k for k, v in level_mapping.items()}
    predicted_level = reverse_mapping[predicted_class]

    return predicted_level

if __name__ == "__main__":
    # Open the test file and read text
    patient = open("testSeverityPatient.json").read()

    # The "Patient" object encapsulates all relevant attributes.
    '''
    Age (int): Patient's age, must be 14 or older.
    Gender (int): 1 for male, 2 for female.
    Air Pollution (int): Level of exposure to air pollution (1-10).
    Alcohol use (int): Frequency of alcohol consumption (1-10).
    Dust Allergy (int): Severity of dust allergy (1-10).
    OccuPational Hazards (int): Exposure to occupational hazards (1-10).
    Genetic Risk (int): Genetic predisposition to health conditions (1-10).
    chronic Lung Disease (int): Severity of chronic lung disease (1-10).
    Balanced Diet (int): Adherence to a balanced diet (1-10).
    Obesity (int): Level of obesity (1-10).
    Smoking (int): Smoking frequency (1-10).
    Passive Smoker (int): Exposure to secondhand smoke (1-10).
    Chest Pain (int): Frequency and severity of chest pain (1-10).
    Coughing of Blood (int): Severity of hemoptysis (1-10).
    Fatigue (int): Level of fatigue experienced (1-10).
    Weight Loss (int): Severity of unintended weight loss (1-10).
    Shortness of Breath (int): Frequency and severity of shortness of breath (1-10).
    Wheezing (int): Occurrence of wheezing (1-10).
    Swallowing Difficulty (int): Severity of difficulty swallowing (1-10).
    Clubbing of Finger Nails (int): Presence and severity of clubbing in fingernails (1-10).
    Frequent Cold (int): Frequency of colds (1-10).
    Dry Cough (int): Severity and frequency of dry cough (1-10).
    Snoring (int): Intensity and frequency of snoring (1-10).
    '''

    print(patient)
    # Ensure patient data is passed as a dictionary
    patient_data = eval(patient)  # Convert JSON string to dictionary
    print(predict(patient_data))