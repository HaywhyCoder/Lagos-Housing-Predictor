# Import required libraries
import joblib
import streamlit as st
import pandas as pd
import numpy as np

# Configure the Streamlit page layout and title
st.set_page_config(page_title="Nigerian Housing Predictor", layout="wide")
st.title("🏡 Nigerian Housing Predictor")
st.write("Get AI-powered predictions for Nigerian housing prices.")

# Create layout columns for input fields
col1, col2, col3 = st.columns(3)

# Input sliders for house specifications
bedrooms = col1.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = col2.slider("Number of Bathrooms", 1, 10, 2)
toilets = col3.slider("Number of Toilets", 1, 10, 2)
parking_spaces = st.slider("Number of Parking Spaces", 1, 10, 2)


# Dropdown for house type selection
title = st.selectbox(
    "What type of house are you interested in?",
    ["Detached Duplex", "Terraced Duplexes", "Detached Bungalow", "Block of Flats",
     "Semi Detached Duplex", "Semi Detached Bungalow", "Terraced Bungalow"],
    index=None,
    placeholder="Select house type...",
)

# Dropdown for location selection in Lagos
location = st.selectbox(
    "where in Lagos are you looking to buy?",
    ["Lekki ","Ajah", "Ikoyi", "Ikeja", "Ibeju Lekki", "Victoria Island (VI)",
     "Magodo", "Ikorodu", "Isheri North", "Surulere", "Agege", "Alimosho",
     "Isolo", "Ipaja", "Yaba", "Ikotun", "Ojodu", "Ifako-Ijaiye", "Maryland",
     "Gbagada", "Amuwo Odofin", "Ogudu", "Ojo", "Ilupeju", "Epe", "Ayobo",
     "Ketu", "Isheri", "Shomolu", "Ejigbo", "Oshodi", "Apapa"],
    index=None,
    placeholder="Select location...",
)

# Create dictionary with user input data
user_input = {
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "toilets": toilets,
    "parking_space": parking_spaces,
    "title": title,
    "town": location
}
# Convert to DataFrame for model input
input_df = pd.DataFrame([user_input])

# Load the pre-trained model pipeline
pipeline = joblib.load("models/my_prediction_pipeline.pkl")

# Create button layout and handle prediction
_, middle, _ = st.columns(3)
if middle.button("Get price", use_container_width=True) and input_df.notna().all(axis=None):
    # Make prediction using the loaded model
    price = pipeline.predict(input_df)[0]
    st.subheader("Predicted Price")
    # Display the predicted price with exponential transformation
    st.write(f"Estimated price for a {bedrooms}-bedroom {title}, with {parking_spaces}-parking space  in {location} is: **₦{np.expm1(price):,.2f}**")
elif input_df.isna().any(axis=None):
    # Show warning if any fields are missing
    st.warning("Please fill in all fields to get a prediction.")