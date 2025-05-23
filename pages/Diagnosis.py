import streamlit as st
import config

st.set_page_config(
    page_title="Dr-Know",
    page_icon="🩺",
)

st.title("Dr Know")
st.header("Personalized Healthcare Diagnosis")

st.markdown(
    """
    Use the sidebar and different sections to outline your demographic, health characteristics and healthcare issue.
    """
)

with st.sidebar:
    gender_selection = st.radio("Select Gender",['Male','Female'])
    age_selection = st.selectbox('Select Age', ('0-14 years','15-24 years','25-44 years','45-64 years','75 - 120 years') ,index=None,placeholder='None')
    marital_selection = st.selectbox("Select Martial Status",('Single', 'Married', 'Divorced', 'Widowed'),index=None,placeholder='None')
    health_behaviour_selection = st.multiselect("Health Behaviours",('Sexually Active', 'Tobacco Use', 'Alochol Use', 'Cannibis Use', 'Regular Exercise'),default=None, placeholder=None)
    medical_background_selection = st.multiselect("Medical Background",('Heart Disease', 'Hypertension', 'Arthritis', 'Epilepsy', 'Diabetes', 'High Cholesterol', 'High Blood Pressure', 'Stroke', 'Asthma', 'Kidney Disease', 'Cancer'),default=None, placeholder=None)


with st.container():
    st.subheader("Do you have any known Allergies?")
    allergies_txt = st.text_area(label=" ",value="",placeholder='',key=1)

    st.subheader("Are you taking any medication? If yes list them")
    medication_txt = st.text_area(label=" ",value="",placeholder='',key=2)

    st.subheader("Have you had any past surgeries or hospitalizations?")
    surgery_txt = st.text_area(label=" ",value="",placeholder='',key=3)

    st.subheader("What symptoms or concerns are you experiencing?")
    symptom_txt = st.text_area(label=" ",value="",placeholder='',key=4)

    health_button = st.button("Get Inisghts", type="primary")

    if health_button:
        st.html("<p> </p>")
        st.subheader("Diagnosis")

        prompt_input = ""
        
        response = config.client.models.generate_content(
        model="gemini-2.0-flash",
        contents = prompt_input
        )

        outcome_txt = st.text_area(label=" ",value=response.text,placeholder='', key= 5)
