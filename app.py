import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="❤️")

# Get the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved models
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
lung_cancer_model = pickle.load(open(f'{working_dir}/saved_models/lung_cancer_model.sav', 'rb'))
kidney_disease_model = pickle.load(open(f'{working_dir}/saved_models/kidney_disease_model.sav', 'rb'))
breast_cancer_model = pickle.load(open(f'{working_dir}/saved_models/Breast_cancer_model.sav', 'rb'))
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_chance_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Disease Prediction System',
                           ['Heart Disease Prediction', 
                            'Lung Cancer Prediction',
                            'Kidney Disease Prediction',
                            'Breast Cancer Prediction',
                            'Diabetes Prediction'],
                           menu_icon='hospital-fill',
                           icons=['heart', 'lungs', 'activity', 'gender-female', 'droplet'],
                           default_index=0)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # Page title
    st.title('Heart Disease Prediction using ML')

    # Input form
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=1, max_value=120, step=1, value=25)

    with col2:
        sex = st.selectbox('Sex', options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")

    with col3:
        cp = st.selectbox('Chest Pain Type', 
                          options=[1, 2, 3, 4], 
                          format_func=lambda x: {1: "Typical Angina", 
                                                 2: "Atypical Angina", 
                                                 3: "Non-anginal Pain", 
                                                 4: "Asymptomatic"}[x])

    with col1:
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=50, max_value=250, step=1, value=120)

    with col2:
        chol = st.number_input('Serum Cholesterol (mg/dL)', min_value=100, max_value=600, step=1, value=200)

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results', 
                               options=[0, 1, 2], 
                               format_func=lambda x: {0: "Normal", 
                                                      1: "ST-T Wave Abnormality", 
                                                      2: "Probable/Definite LVH"}[x])

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=50, max_value=250, step=1, value=150)

    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, step=0.1, value=1.0)

    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', 
                             options=[1, 2, 3], 
                             format_func=lambda x: {1: "Upsloping", 
                                                    2: "Flat", 
                                                    3: "Downsloping"}[x])

    with col3:
        ca = st.number_input('Number of Major Vessels Colored by Flouroscopy', min_value=0, max_value=3, step=1, value=0)

    with col1:
        thal = st.selectbox('Thalassemia', 
                            options=[3, 6, 7], 
                            format_func=lambda x: {3: "Normal", 
                                                   6: "Fixed Defect", 
                                                   7: "Reversible Defect"}[x])

    # Prediction code
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Lung Cancer Prediction Page
if selected == 'Lung Cancer Prediction':

    # Page title
    st.title('Lung Cancer Prediction using ML')

    # Input form
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox('Gender', options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")

    with col2:
        age = st.number_input('Age', min_value=1, max_value=120, step=1, value=25)

    with col3:
        smoking = st.selectbox('Smoking', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col1:
        yellow_fingers = st.selectbox('Yellow Fingers', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col2:
        anxiety = st.selectbox('Anxiety', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col3:
        peer_pressure = st.selectbox('Peer Pressure', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col1:
        chronic_disease = st.selectbox('Chronic Disease', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col2:
        fatigue = st.selectbox('Fatigue', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col3:
        allergy = st.selectbox('Allergy', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col1:
        wheezing = st.selectbox('Wheezing', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col2:
        alcohol_consuming = st.selectbox('Alcohol Consuming', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col3:
        coughing = st.selectbox('Coughing', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col1:
        shortness_of_breath = st.selectbox('Shortness of Breath', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col2:
        swallowing_difficulty = st.selectbox('Swallowing Difficulty', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    with col3:
        chest_pain = st.selectbox('Chest Pain', options=[2, 1], format_func=lambda x: "Yes" if x == 2 else "No")

    # Prediction code
    lung_diagnosis = ''

    if st.button('Lung Cancer Test Result'):
        user_input = [gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]

        lung_prediction = lung_cancer_model.predict([user_input])

        if lung_prediction[0] == 1:
            lung_diagnosis = 'The person is at risk of lung cancer'
        else:
            lung_diagnosis = 'The person is not at risk of lung cancer'

    st.success(lung_diagnosis)

# Kidney Disease Prediction Page
if selected == 'Kidney Disease Prediction':
    
    # Page title
    st.title('Kidney Disease Prediction using ML')
    
    # Input form
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=1, max_value=100, step=1, value=25)
        
    with col2:
        blood_pressure = st.number_input('Blood Pressure (mm Hg)', min_value=50, max_value=180, step=1, value=80)
        
    with col3:
        specific_gravity = st.number_input('Specific Gravity', min_value=1.005, max_value=1.025, step=0.005, value=1.020)
    
    with col1:
        albumin = st.number_input('Albumin Level', min_value=0, max_value=5, step=1, value=0)
        
    with col2:
        sugar = st.number_input('Sugar Level', min_value=0, max_value=5, step=1, value=0)
        
    with col3:
        red_blood_cells = st.selectbox('Red Blood Cells (Normal=1, Abnormal=0)', 
                                      options=[1, 0], 
                                      format_func=lambda x: "Yes" if x == 1 else "No")
    
    with col1:
        pus_cell = st.selectbox('Pus Cell (Normal=1, Abnormal=0)', 
                               options=[1, 0], 
                               format_func=lambda x: "Yes" if x == 1 else "No")
        
    with col2:
        pus_cell_clumps = st.selectbox('Pus Cell Clumps (Present=1, Not Present=0)', 
                                      options=[1, 0], 
                                      format_func=lambda x: "Yes" if x == 1 else "No")
        
    with col3:
        bacteria = st.selectbox('Bacteria (Present=1, Not Present=0)', 
                              options=[1, 0], 
                              format_func=lambda x: "Yes" if x == 1 else "No")
    
    with col1:
        blood_glucose_random = st.number_input('Blood Glucose Random (mgs/dl)', 
                                             min_value=20, max_value=500, step=1, value=121)
        
    with col2:
        blood_urea = st.number_input('Blood Urea (mgs/dl)', 
                                    min_value=1, max_value=400, step=1, value=36)
        
    with col3:
        serum_creatinine = st.number_input('Serum Creatinine (mgs/dl)', 
                                          min_value=0.4, max_value=76.0, step=0.1, value=1.2)
    
    with col1:
        sodium = st.number_input('Sodium (mEq/L)', 
                               min_value=4.5, max_value=163.0, step=0.1, value=145.0)
        
    with col2:
        potassium = st.number_input('Potassium (mEq/L)', 
                                   min_value=2.5, max_value=47.0, step=0.1, value=4.3)
        
    with col3:
        haemoglobin = st.number_input('Haemoglobin (gms)', 
                                     min_value=3.1, max_value=17.8, step=0.1, value=15.4)
    
    with col1:
        packed_cell_volume = st.number_input('Packed Cell Volume', 
                                           min_value=9, max_value=54, step=1, value=44)
        
    with col2:
        white_blood_cell_count = st.number_input('White Blood Cell Count (cells/cumm)', 
                                                min_value=2200, max_value=26400, step=100, value=7800)
        
    with col3:
        red_blood_cell_count = st.number_input('Red Blood Cell Count (millions/cmm)', 
                                              min_value=2.1, max_value=8.0, step=0.1, value=5.2)
    
    with col1:
        hypertension = st.selectbox('Hypertension', 
                                   options=[1, 0], 
                                   format_func=lambda x: "Yes" if x == 1 else "No")
        
    with col2:
        diabetes_mellitus = st.selectbox('Diabetes Mellitus', 
                                        options=[1, 0], 
                                        format_func=lambda x: "Yes" if x == 1 else "No")
        
    with col3:
        coronary_artery_disease = st.selectbox('Coronary Artery Disease', 
                                              options=[1, 0], 
                                              format_func=lambda x: "Yes" if x == 1 else "No")
    
    with col1:
        appetite = st.selectbox('Appetite (Good=0, Poor=1)', 
                              options=[1, 0], 
                              format_func=lambda x: "poor" if x == 1 else "good")
        
    with col2:
        peda_edema = st.selectbox('Pedal Edema', 
                                 options=[1, 0], 
                                 format_func=lambda x: "Yes" if x == 1 else "No")
        
    with col3:
        aanemia = st.selectbox('Anemia', 
                              options=[1, 0], 
                              format_func=lambda x: "Yes" if x == 1 else "No")
    
    # Prediction code
    kidney_diagnosis = ''
    
    if st.button('Kidney Disease Test Result'):
        user_input = [age, blood_pressure, specific_gravity, albumin, sugar, 
                     red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
                     blood_glucose_random, blood_urea, serum_creatinine, sodium,
                     potassium, haemoglobin, packed_cell_volume,
                     white_blood_cell_count, red_blood_cell_count, hypertension,
                     diabetes_mellitus, coronary_artery_disease, appetite,
                     peda_edema, aanemia]
        
        kidney_prediction = kidney_disease_model.predict([user_input])
        
        if kidney_prediction[0] == 0:
            kidney_diagnosis = 'The person has Kidney Disease'
        else:
            kidney_diagnosis = 'The person does not have Kidney Disease'
            
    st.success(kidney_diagnosis)

# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    
    # Page title
    st.title('Breast Cancer Prediction using ML')
    
    # Input form
    col1, col2= st.columns(2)
    
    with col1:
        mean_radius = st.number_input('Mean Radius', 
                                    min_value=5.0, 
                                    max_value=30.0, 
                                    step=0.1, 
                                    value=15.0,
                                    help="Mean of distances from center to points on the perimeter")
        
    with col2:
        mean_texture = st.number_input('Mean Texture', 
                                     min_value=5.0, 
                                     max_value=40.0, 
                                     step=0.1, 
                                     value=18.0,
                                     help="Standard deviation of gray-scale values")
        
    with col1:
        mean_perimeter = st.number_input('Mean Perimeter', 
                                       min_value=40.0, 
                                       max_value=200.0, 
                                       step=0.1, 
                                       value=100.0,
                                       help="Mean size of the core tumor")
    
    with col2:
        mean_area = st.number_input('Mean Area', 
                                  min_value=200.0, 
                                  max_value=2000.0, 
                                  step=1.0, 
                                  value=800.0,
                                  help="Mean area of the core tumor")
        
    with col1:
        mean_smoothness = st.number_input('Mean Smoothness', 
                                        min_value=0.05, 
                                        max_value=0.20, 
                                        step=0.001, 
                                        value=0.10,
                                        help="Mean of local variation in radius lengths")
    
    # Add information about the measurements
    st.info("""
    💡 Information about measurements:
    - Radius: Mean of distances from center to points on the perimeter
    - Texture: Standard deviation of gray-scale values
    - Perimeter: Size of the core tumor
    - Area: Area of the core tumor
    - Smoothness: Local variation in radius lengths
    """)
    
    # Prediction code
    breast_cancer_diagnosis = ''
    
    if st.button('Breast Cancer Test Result'):
        user_input = [mean_radius, mean_texture, mean_perimeter, 
                     mean_area, mean_smoothness]
        
        breast_cancer_prediction = breast_cancer_model.predict([user_input])
        
        if breast_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = 'The breast mass is malignant (cancerous)'
        else:
            breast_cancer_diagnosis = 'The breast mass is benign (non-cancerous)'
            
    if breast_cancer_diagnosis:
        if 'malignant' in breast_cancer_diagnosis:
            st.error(breast_cancer_diagnosis)
            st.warning("⚠️ Please consult with a healthcare professional immediately for further evaluation.")
        else:
            st.success(breast_cancer_diagnosis)
            st.info("ℹ️ Regular screening and check-ups are still recommended for preventive care.")


# [Previous code remains exactly the same until after the breast cancer section]

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    
    # Page title
    st.title('Diabetes Prediction using ML')
    
    # Input form
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', 
                            min_value=1, 
                            max_value=120, 
                            step=1, 
                            value=25)
        
    with col2:
        gender = st.selectbox('Gender',
                            options=['Female', 'Male', 'Other'],
                            format_func=lambda x: x)
        
    with col3:
        bmi = st.number_input('BMI',
                            min_value=10.0,
                            max_value=50.0,
                            step=0.1,
                            value=25.0)
    
    with col1:
        hypertension = st.selectbox('Hypertension',
                                  options=['No', 'Yes'],
                                  format_func=lambda x: x)
        
    with col2:
        heart_disease = st.selectbox('Heart Disease',
                                   options=['No', 'Yes'],
                                   format_func=lambda x: x)
        
    with col3:
        HbA1c_level = st.number_input('HbA1c Level',
                                    min_value=3.0,
                                    max_value=9.0,
                                    step=0.1,
                                    value=5.0)
    
    with col1:
        blood_glucose_level = st.number_input('Blood Glucose Level',
                                           min_value=70,
                                           max_value=300,
                                           step=1,
                                           value=120)
        
    with col2:
        smoking_history = st.selectbox('Smoking History',
                                    options=['No Info', 'current', 'ever', 'former', 'never', 'not current'],
                                    format_func=lambda x: x)
    
    # Add information about the measurements
    st.info("""
    💡 Important Information:
    - BMI: Body Mass Index (weight in kg / height in meters squared)
    - HbA1c: Glycated hemoglobin test (measures average blood sugar over past 2-3 months)
    - Normal HbA1c: Below 5.7%
    - Prediabetes HbA1c: 5.7% to 6.4%
    - Diabetes HbA1c: 6.5% or higher
    """)
    
    # Encoding dictionaries
    gender_encoding = {'Female': 0, 'Male': 1, 'Other': 2}
    smoking_encoding = {'No Info': 0, 'current': 1, 'ever': 2, 'former': 3, 'never': 4, 'not current': 5}
    yes_no_encoding = {'No': 0, 'Yes': 1}
    
    # Prediction code
    diabetes_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        # Encode categorical variables
        gender_encoded = gender_encoding[gender]
        smoking_history_encoded = smoking_encoding[smoking_history]
        hypertension_encoded = yes_no_encoding[hypertension]
        heart_disease_encoded = yes_no_encoding[heart_disease]
        
        user_input = [age, hypertension_encoded, heart_disease_encoded, 
                     bmi, HbA1c_level, blood_glucose_level,
                     smoking_history_encoded, gender_encoded]
        
        diabetes_prediction = diabetes_model.predict([user_input])
        
        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = 'The person is likely to have diabetes'
            st.error(diabetes_diagnosis)
            st.warning("""
            ⚠️ Important Next Steps:
            1. Consult with a healthcare provider immediately
            2. Get a comprehensive blood sugar test
            3. Begin monitoring your blood sugar levels
            4. Consider lifestyle modifications
            """)
        else:
            diabetes_diagnosis = 'The person is not likely to have diabetes'
            st.success(diabetes_diagnosis)
            st.info("""
            ℹ️ Healthy Habits to Maintain:
            1. Regular exercise
            2. Balanced diet
            3. Maintain healthy weight
            4. Regular check-ups
            5. Adequate sleep
            """)
        
        # Display risk factors if present
        risk_factors = []
        if bmi > 25:
            risk_factors.append("High BMI")
        if HbA1c_level > 5.7:
            risk_factors.append("Elevated HbA1c")
        if blood_glucose_level > 140:
            risk_factors.append("High Blood Glucose")
        if hypertension == "Yes":
            risk_factors.append("Hypertension")
        if heart_disease == "Yes":
            risk_factors.append("Heart Disease")
        
        if risk_factors:
            st.warning("Risk Factors Detected: " + ", ".join(risk_factors))
