import streamlit as st
from streamlit import runtime 
import pandas as pd
import numpy as np
import pickle

st.title('Sports Prediction Group 35')

model = r"C:\Users\Martha Agyeman\Desktop\Intro to AI\XGBmodel_gs_model.pkl"

md = pickle.load(open(model, 'rb'))



potential= st.number_input('potential')
value_eur= st.number_input('value_eur')
wage_eur= st.number_input('wage_eur')
age= st.number_input('age')
international_reputation= st.number_input('international_reputation')
release_clause_eur= st.number_input('release_clause_eur')
shooting= st.number_input('shooting')
passing= st.number_input('passing')
dribbling= st.number_input('dribbling')
physic= st.number_input('physic')
attacking_crossing= st.number_input('attacking_crossing')
attacking_short_passing= st.number_input('attacking_short_passing')
skill_curve= st.number_input('skill_curve')
skill_long_passing = st.number_input('skill_long_passing ')
skill_ball_control= st.number_input('skill_ball_control')
movement_reactions= st.number_input('movement_reactions')
power_shot_power= st.number_input('power_shot_power')
power_long_shots= st.number_input('power_long_shots')
mentality_aggression= st.number_input('mentality_aggression')
mentality_vision= st.number_input('mentality_vision')
mentality_composure = st.number_input('mentality_composure ')


prediction = md.predict([[potential, value_eur, wage_eur, age, international_reputation, release_clause_eur, shooting, passing, dribbling, physic, attacking_crossing,
                            attacking_short_passing, skill_curve, skill_long_passing, skill_ball_control, movement_reactions, power_shot_power, power_long_shots,
                            mentality_aggression, mentality_vision, mentality_composure]])


if st.button('Predict'):
    st.write("The predicted overall for your player is ", prediction[0])