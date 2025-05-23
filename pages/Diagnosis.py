import streamlit as st
import config

st.set_page_config(
    page_title="Dr-Know",
    page_icon="🩺",
)

st.title("Dr Know")
st.header("Personalized Healthcare Diagnostics")

st.markdown(
    """
    Use the sidebar and different sections to outline your demographic, health characteristics and healthcare issue.
    """
)

with st.sidebar:
    gender_selection = st.radio("Select Gender",['Male','Female'])
    marital_selection = st.selectbox("Select Martial Status",('Single', 'Married', 'Divorced', 'Widowed'),index=None,placeholder='None')
    health_behaviour_selection = st.multiselect("Health Behaviours",('Sexually Active', 'Tobacco Use', 'Alochol Use', 'Cannibis Use', 'Regular Exercise'),default=None, placeholder=None)
    medical_background_selection = st.multiselect("Medical Background",('Heart Disease', 'Hypertension', 'Arthritis', 'Epilepsy', 'Diabetes', 'High Cholesterol', 'High Blood Pressure', 'Stroke', 'Asthma', 'Kidney Disease', 'Cancer'),default=None, placeholder=None)


with st.container():
    