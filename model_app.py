import streamlit as st
import joblib

model = joblib.load("regression.joblib")

# Streamlit title
st.title("House Price Prediction")

with st.form(key='house_form'):
    size = st.number_input("Size of the house (in sq meters):", min_value=10, max_value=1000, step=1)
    bedrooms = st.number_input("Number of bedrooms:", min_value=1, max_value=10, step=1)
    garden = st.selectbox("Does the house have a garden?", ("No", "Yes"))

    # Submit button
    submit_button = st.form_submit_button(label='Predict')

# Retrieve the information and pass it to the model via the predict function
if submit_button:
    # Convert 'Yes'/'No' to 1/0 for garden
    garden_value = 1 if garden == "Yes" else 0

    # Create input array for the model
    input_data = [[size, bedrooms, garden_value]]

    # Get the prediction from the model
    prediction = model.predict(input_data)

    # Display the prediction result using st.write
    st.write(f"Predicted House Price: ${prediction[0]:,.2f}")
