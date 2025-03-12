
import os
import pickle
import streamlit as st  
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Vital Care", layout="wide", page_icon="heart-attack.png")

try:
    diabetes_model = pickle.load(open(r'C:\Users\harsh\OneDrive\Desktop\Multiple Disease system\models sav\diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open(r'C:\Users\harsh\OneDrive\Desktop\Multiple Disease system\models sav\heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open(r'C:\Users\harsh\OneDrive\Desktop\Multiple Disease system\models sav\parkinsons_model.sav', 'rb'))

except FileNotFoundError:
    st.error("Model files are missing. Please ensure that the models are available.")
    st.stop()

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Disease', 'Heart Disease', 'Parkinsons Disease'],
                           menu_icon='hospital-fill', 
                           icons=['activity', 'heart', 'person'], 
                           default_index=0)
    
    image_path = r'C:\Users\harsh\OneDrive\Desktop\Multiple Disease system\Vital Care.png'
    if os.path.exists(image_path):
        st.image(image_path)
    else:
        st.error("Image file 'Vital Care.png' not found!")


def validate_inputs(user_input, selected_disease):
    errors = []
    try:   

        user_input = [float(x) for x in user_input]

    except ValueError:

        st.error("Please enter valid numeric values. Invalid input found.")
        return None 

    if selected_disease == 'Diabetes Disease':

            if not (0 <= user_input[0] <= 20):
                errors.append("Number of Pregnancies should be between 0 and 20.")

            if not (0 <= user_input[1] <= 300):
                errors.append("Glucose level should be between 0 and 300.")

            if not (0 <= user_input[2] <= 200):
                errors.append("Blood Pressure should be between 0 and 200.")

            if not (0 <= user_input[3] <= 100):
                errors.append("Skin Thickness should be between 0 and 100.")

            if not (0 <= user_input[4] <= 900):
                errors.append("Insulin level should be between 0 and 900.")

            if not (0.0 <= user_input[5] <= 70.0):
                errors.append("BMI should be between 0 and 70.")

            if not (0.000 <= user_input[6] <= 2.50):
                errors.append("Diabetes Pedigree Function should be between 0.000 and 2.50.")

            if not (1 <= user_input[7] <= 120):
                errors.append("Age should be between 1 and 120.")

    elif selected_disease == 'Heart Disease':

        if not (1 <= user_input[0] <= 120):
            errors.append("Age should be between 1 and 120.")

        if user_input[1] == -1:
            errors.append("Please select a valid gender (Female or Male).")

        if user_input[2] == -1:
            errors.append("Please select a valid Chest Pain type.")

        if not (50 <= user_input[3] <= 300):
            errors.append("Resting Blood Pressure should be between 50 and 300.")

        if not (100 <= user_input[4] <= 600):
            errors.append("Serum Cholesterol should be between 100 and 600.")

        if user_input[5] == -1:
            errors.append("Please select a valid option for Fasting Blood Sugar.")

        if user_input[6] == -1:
            errors.append("Please select a valid Resting ECG result.")

        if not (50 <= user_input[7] <= 300):
            errors.append("Maximum Heart Rate should be between 50 and 300.")

        if user_input[8] == -1:
            errors.append("Please select a valid option for Exercise Induced Angina.")

        if not (0.0 <= user_input[9] <= 7.0):
            errors.append("ST depression should be between 0.0 and 7.0.")

        if user_input[10] == -1:
            errors.append("Please select a valid Slope value.")

        if not (0 <= user_input[11] <= 5):
            errors.append("Major vessels should be between 0 and 5.")

        if user_input[12] == -1:
            errors.append("Please select a valid Thalassemia value.")

            
    elif selected_disease == 'Parkinsons Disease':

        for i, (min_val, max_val, name) in enumerate([
                (50.00, 300.00, "MDVP:Fo(Hz)"), 
                (50.00, 600.00, "MDVP:Fhi(Hz)"), 
                (50.00, 300.00, "MDVP:Flo(Hz)"),
                (0.00000, 0.10000, "MDVP:Jitter(%)"), 
                (0.000000, 0.10000, "MDVP:Jitter(Abs)"),
                (0.00000, 0.10000, "MDVP:RAP"), 
                (0.00000, 0.10000, "MDVP:PPQ"), 
                (0.00000, 0.10000, "MDVP:DDP"),
                (0.00000, 1.00000, "MDVP:Shimmer"), 
                (0.000, 2.000, "MDVP:Shimmer(dB)"),
                (0.00000, 0.10000, "Shimmer:APQ3"), 
                (0.0000, 0.1000, "Shimmer:APQ5"),
                (0.00000, 0.50000, "MDVP:APQ"), 
                (0.00000, 0.50000, "Shimmer:DDA"), 
                (0.00000, 0.50000, "NHR"),
                (0.00, 50.00, "HNR"), 
                (0.00000, 0.10000, "RPDE"), 
                (0.00000, 1.00000, "DFA"),
                (-10.00, 10.00, "Spread1"), 
                (0.00000, 1.00000, "Spread2"), 
                (0.00, 10.00, "D2"),
                (0.00000, 1.00000, "PPE")
            ]):
                if not (min_val <= user_input[i] <= max_val):
                    errors.append(f"{name} should be between {min_val} and {max_val}.")

    if errors:        
        for err in errors:
            st.error(err)
        return None

    return user_input          


if 'diabetes_fields' not in st.session_state:

    st.session_state.diabetes_fields = {
        'Pregnancies': 0,
        'Glucose': 0,
        'BloodPressure': 0,
        'SkinThickness': 0,
        'Insulin': 0,
        'BMI': 0.0,
        'DiabetesPedigreeFunction': 0.000,
        'Age': 1
    }

if selected == 'Diabetes Disease':

    st.title('Diabetes Prediction')
    
    with st.expander("Input Fields for Diabetes Disease"):

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.session_state.diabetes_fields['Pregnancies'] = st.slider('Number of Pregnancies', 0, 20, st.session_state.diabetes_fields['Pregnancies'], key='diabetes_Pregnancies')
            st.session_state.diabetes_fields['SkinThickness'] = st.slider('Skin Thickness value(mm)', 0, 100, st.session_state.diabetes_fields['SkinThickness'], key='diabetes_SkinThickness')
            st.session_state.diabetes_fields['DiabetesPedigreeFunction'] = st.slider('Diabetes Pedigree Function', 0.000, 2.50, st.session_state.diabetes_fields['DiabetesPedigreeFunction'], key='diabetes_DiabetesPedigreeFunction')
        
        with col2:
            st.session_state.diabetes_fields['Glucose'] = st.slider('Glucose Level(mg/dL)', 0, 300, st.session_state.diabetes_fields['Glucose'], key='diabetes_Glucose')
            st.session_state.diabetes_fields['Insulin'] = st.slider('Insulin Level(µU/mL)', 0, 900, st.session_state.diabetes_fields['Insulin'], key='diabetes_Insulin')
            st.session_state.diabetes_fields['Age'] = st.slider('Age(in Years)', 1, 120, st.session_state.diabetes_fields['Age'], key='diabetes_Age')
        
        with col3:
            st.session_state.diabetes_fields['BloodPressure'] = st.slider('Blood Pressure(mmHg)', 0, 200, st.session_state.diabetes_fields['BloodPressure'], key='diabetes_BloodPressure')
            st.session_state.diabetes_fields['BMI'] = st.slider('BMI(kg/m²)', 0.0, 70.0, st.session_state.diabetes_fields['BMI'], key='diabetes_BMI')        
        
        submit_button = st.button(label='Diabetes Test Result')
        
        if submit_button:
            try:
                user_input = [
                    int(st.session_state.diabetes_fields['Pregnancies']),
                    int(st.session_state.diabetes_fields['Glucose']),
                    int(st.session_state.diabetes_fields['BloodPressure']),
                    int(st.session_state.diabetes_fields['SkinThickness']),
                    int(st.session_state.diabetes_fields['Insulin']),
                    float(st.session_state.diabetes_fields['BMI']),
                    float(st.session_state.diabetes_fields['DiabetesPedigreeFunction']),
                    int(st.session_state.diabetes_fields['Age'])
                ]                
        
                user_input = validate_inputs(user_input, selected_disease='Diabetes Disease') if 'validate_inputs' in globals() else user_input
                
                if user_input is not None:
                    if 'diabetes_model' in globals():
                        diab_prediction = diabetes_model.predict([user_input])
                        st.success('The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic')
                    else:
                        st.error("Model not loaded. Please check the model initialization.")
                else:
                    st.error("Input validation failed. Please correct the highlighted errors.")
            except ValueError:
                st.error("Invalid input detected. Please enter correct values.")
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

if 'heart_fields' not in st.session_state:

    st.session_state.heart_fields = {
        'Sex': 'Select Gender',
        'Age': 1,
        'ChestPain': 'Select Chest Pain',
        'BloodPressure': 50,
        'Cholesterol': 100,
        'FastingBloodSugar': 'Select Option',
        'RestingECG': 'Select ECG Result',
        'MaxHR': 50,
        'ExerciseAngina': 'Select Option',
        'Oldpeak': 0.0,
        'Slope': 'Select Slope',
        'Ca': 0,
        'Thal': 'Select Thal'
    }

if selected == 'Heart Disease':

    st.title('Heart Disease Prediction')

    with st.expander("Input Fields for Heart Disease"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.session_state.heart_fields['Age'] = st.slider('Age(in Years)', 1, 120, st.session_state.heart_fields.get('Age', 50), key='heart_Age')
            st.session_state.heart_fields['Sex'] = st.selectbox('Sex', ['Select Gender', 'Female', 'Male'],
                                                                index=['Select Gender', 'Female', 'Male'].index(st.session_state.heart_fields.get('Sex', 'Select Gender')),
                                                                key='heart_Sex')
            st.session_state.heart_fields['ChestPain'] = st.selectbox('Chest Pain Type', ['Select Chest Pain', 'Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'],
                                                                      index=['Select Chest Pain', 'Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'].index(st.session_state.heart_fields.get('ChestPain', 'Select Chest Pain')), 
                                                                      key='heart_ChestPain')

        with col2:
            st.session_state.heart_fields['BloodPressure'] = st.slider('Blood Pressure(mmHg)', 50, 300, st.session_state.heart_fields.get('BloodPressure', 50), key='heart_BloodPressure')
            st.session_state.heart_fields['Cholesterol'] = st.slider('Cholesterol(mg/dL)', 100, 600, st.session_state.heart_fields.get('Cholesterol', 100), key='heart_Cholesterol')
            st.session_state.heart_fields['FastingBloodSugar'] = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Select Option', 'No', 'Yes'], 
                                                                              index=['Select Option', 'No', 'Yes'].index(st.session_state.heart_fields.get('FastingBloodSugar', 'Select Option')),
                                                                              key='heart_FastingBloodSugar')

        with col3:
            st.session_state.heart_fields['RestingECG'] = st.selectbox('Resting ECG Results', ['Select ECG Result', 'Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'],
                                                                       index=['Select ECG Result', 'Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'].index(st.session_state.heart_fields.get('RestingECG', 'Select ECG Result')),
                                                                       key='heart_RestingECG')
            st.session_state.heart_fields['MaxHR'] = st.slider('Max Heart Rate(bpm)', 50, 300, st.session_state.heart_fields.get('MaxHR', 50), key='heart_MaxHR')
            st.session_state.heart_fields['ExerciseAngina'] = st.selectbox('Exercise Induced Angina', ['Select Option', 'No', 'Yes'], 
                                                                           index=['Select Option', 'No', 'Yes'].index(st.session_state.heart_fields.get('ExerciseAngina', 'Select Option')),
                                                                           key='heart_ExerciseAngina')

        with col1:
            st.session_state.heart_fields['Oldpeak'] = st.slider('Oldpeak (ST depression)', 0.0, 7.0, st.session_state.heart_fields.get('Oldpeak', 0.0), key='heart_Oldpeak')
            st.session_state.heart_fields['Slope'] = st.selectbox('Slope of Peak Exercise ST Segment', ['Select Slope', 'Upsloping', 'Flat', 'Downsloping'],
                                                                  index=['Select Slope', 'Upsloping', 'Flat', 'Downsloping'].index(st.session_state.heart_fields.get('Slope', 'Select Slope')),
                                                                  key='heart_Slope')

        with col2:
            st.session_state.heart_fields['Ca'] = st.slider('Number of Major Vessels', 0, 5, st.session_state.heart_fields.get('Ca', 0), key='heart_Ca')

        with col3:
            st.session_state.heart_fields['Thal'] = st.selectbox('Thalassemia', ['Select Thal', 'Normal', 'Fixed Defect', 'Reversible Defect'],
                                                                 index=['Select Thal', 'Normal', 'Fixed Defect', 'Reversible Defect'].index(st.session_state.heart_fields.get('Thal', 'Select Thal')),
                                                                 key='heart_Thal')

        submit_button = st.button(label='Heart Disease Test Result')

        if submit_button:
            try:
                user_input = [
                    int(st.session_state.heart_fields['Age']),
                    0 if st.session_state.heart_fields['Sex'] == 'Female' else 1 if st.session_state.heart_fields['Sex'] == 'Male' else -1,
                    ['Select Chest Pain', 'Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'].index(st.session_state.heart_fields['ChestPain']) - 1,
                    int(st.session_state.heart_fields['BloodPressure']),
                    int(st.session_state.heart_fields['Cholesterol']),
                    1 if st.session_state.heart_fields['FastingBloodSugar'] == 'Yes' else 0 if st.session_state.heart_fields['FastingBloodSugar'] == 'No' else -1,
                    ['Select ECG Result', 'Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'].index(st.session_state.heart_fields['RestingECG']) - 1,
                    int(st.session_state.heart_fields['MaxHR']),
                    1 if st.session_state.heart_fields['ExerciseAngina'] == 'Yes' else 0 if st.session_state.heart_fields['ExerciseAngina'] == 'No' else -1,
                    float(st.session_state.heart_fields['Oldpeak']),
                    ['Select Slope', 'Upsloping', 'Flat', 'Downsloping'].index(st.session_state.heart_fields['Slope']) - 1,
                    int(st.session_state.heart_fields['Ca']),
                    ['Select Thal', 'Normal', 'Fixed Defect', 'Reversible Defect'].index(st.session_state.heart_fields['Thal']) - 1
                ]

                user_input = validate_inputs(user_input, selected_disease='Heart Disease') if 'validate_inputs' in globals() else user_input
                
                if user_input is not None:
                    if 'heart_disease_model' in globals():
                        heart_prediction = heart_disease_model.predict([user_input])
                        st.success('The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease')
                    else:
                        st.error("Model not loaded. Please check the model initialization.")
                else:
                    st.error("Input validation failed. Please correct the highlighted errors.")
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

if 'parkinson_fields' not in st.session_state:

    st.session_state.parkinson_fields = {
        'MDVP_Fo': 50.00,
        'MDVP_Fhi': 50.00,
        'MDVP_Flo': 50.00,
        'MDVP_Jitter': 0.00000,
        'MDVP_Jitter_Abs': 0.000000,
        'MDVP_RAP': 0.00000,
        'MDVP_PPQ': 0.00000,
        'MDVP_DDP': 0.00000,
        'MDVP_Shimmer': 0.00000,
        'MDVP_Shimmer_dB': 0.000,
        'Shimmer_APQ3': 0.00000,
        'Shimmer_APQ5': 0.0000,
        'MDVP_APQ': 0.00000,
        'Shimmer_DDA': 0.00000,
        'NHR': 0.00000,
        'HNR': 0.00,
        'RPDE': 0.00000,
        'DFA': 0.00000,
        'Spread1': -10.00,
        'Spread2': 0.00000,
        'D2': 0.00,
        'PPE': 0.00000
    }


if selected == 'Parkinsons Disease':
    
    st.title("Parkinson's Disease Prediction")

    with st.expander("Input Fields for Parkinson's Disease"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.session_state.parkinson_fields['MDVP_Fo'] = st.slider('MDVP_Fo', 50.00, 300.00, st.session_state.parkinson_fields['MDVP_Fo'])
            st.session_state.parkinson_fields['MDVP_Fhi'] = st.slider('MDVP_Fhi', 50.00, 600.00, st.session_state.parkinson_fields['MDVP_Fhi'])
            st.session_state.parkinson_fields['MDVP_Flo'] = st.slider('MDVP_Flo', 50.00, 300.00, st.session_state.parkinson_fields['MDVP_Flo'])
            st.session_state.parkinson_fields['MDVP_Jitter'] = st.slider('MDVP Jitter', 0.00000, 0.10000, st.session_state.parkinson_fields['MDVP_Jitter'])
            st.session_state.parkinson_fields['MDVP_Jitter_Abs'] = st.slider('MDVP Jitter (Abs)', 0.000000, 0.10000, st.session_state.parkinson_fields['MDVP_Jitter_Abs'])
            st.session_state.parkinson_fields['PPE'] = st.slider('PPE', 0.00000, 1.00000, st.session_state.parkinson_fields['PPE'])
            
        with col2:
            st.session_state.parkinson_fields['MDVP_RAP'] = st.slider('MDVP RAP', 0.00000, 0.10000, st.session_state.parkinson_fields['MDVP_RAP'])
            st.session_state.parkinson_fields['MDVP_PPQ'] = st.slider('MDVP PPQ', 0.00000, 0.10000, st.session_state.parkinson_fields['MDVP_PPQ'])
            st.session_state.parkinson_fields['MDVP_DDP'] = st.slider('MDVP DDP', 0.00000, 0.10000, st.session_state.parkinson_fields['MDVP_DDP'])
            st.session_state.parkinson_fields['MDVP_Shimmer'] = st.slider('MDVP Shimmer', 0.00000, 1.00000, st.session_state.parkinson_fields['MDVP_Shimmer'])
            st.session_state.parkinson_fields['MDVP_Shimmer_dB'] = st.slider('MDVP Shimmer (dB)', 0.000, 2.000, st.session_state.parkinson_fields['MDVP_Shimmer_dB'])
            
        with col3:
            st.session_state.parkinson_fields['Shimmer_APQ3'] = st.slider('Shimmer APQ3', 0.00000, 0.10000, st.session_state.parkinson_fields['Shimmer_APQ3'])
            st.session_state.parkinson_fields['Shimmer_APQ5'] = st.slider('Shimmer APQ5', 0.0000, 0.1000, st.session_state.parkinson_fields['Shimmer_APQ5'])
            st.session_state.parkinson_fields['MDVP_APQ'] = st.slider('MDVP APQ', 0.00000, 0.50000, st.session_state.parkinson_fields['MDVP_APQ'])
            st.session_state.parkinson_fields['Shimmer_DDA'] = st.slider('Shimmer DDA', 0.00000, 0.50000, st.session_state.parkinson_fields['Shimmer_DDA'])
            st.session_state.parkinson_fields['NHR'] = st.slider('NHR', 0.00000,0.50000, st.session_state.parkinson_fields['NHR'])
            
        with col1:
            st.session_state.parkinson_fields['HNR'] = st.slider('HNR', 0.00, 50.00, st.session_state.parkinson_fields['HNR'])
            st.session_state.parkinson_fields['RPDE'] = st.slider('RPDE', 0.00000, 0.10000, st.session_state.parkinson_fields['RPDE'])
            
        with col2:
            st.session_state.parkinson_fields['DFA'] = st.slider('DFA', 0.00000, 1.00000, st.session_state.parkinson_fields['DFA'])
            st.session_state.parkinson_fields['Spread1'] = st.slider('Spread1', -10.00, 10.00, st.session_state.parkinson_fields['Spread1'])
            
        with col3:
            st.session_state.parkinson_fields['Spread2'] = st.slider('Spread2', 0.00000, 1.00000, st.session_state.parkinson_fields['Spread2'])
            st.session_state.parkinson_fields['D2'] = st.slider('D2', 0.00, 10.00, st.session_state.parkinson_fields['D2'])
           
        
    submit_button = st.button(label='Parkinson Disease Test Result')

    if submit_button:
        try:
            user_input = list(st.session_state.parkinson_fields.values())
            user_input = validate_inputs(user_input, selected_disease='Parkinsons Disease') if 'validate_inputs' in globals() else user_input

            if user_input is not None:
                if 'parkinsons_model' in globals():
                    parkinsons_prediction = parkinsons_model.predict([user_input])
                    st.success("The person has Parkinson's Disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's Disease")
                else:
                    st.error("Model not loaded. Please check the model initialization.")
            else:
                st.error("Input validation failed. Please correct the highlighted errors.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")