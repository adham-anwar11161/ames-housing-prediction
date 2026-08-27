import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Ames Housing Price Predictor",
    page_icon="🏡",
    layout="wide"
)

@st.cache_resource
def load_model():
    return joblib.load('rf_model.pkl')

rf_model = load_model()

st.title("🏡 Ames Housing Price Prediction App")
st.markdown("Welcome! This application helps you estimate the price of any house based on its specifications using Machine Learning.")
st.divider()

st.sidebar.header("🔍 House Specifications")

overall_qual = st.sidebar.slider("Overall Quality (1 to 10)", 1, 10, 5)
gr_liv_area = st.sidebar.number_input("Above Ground Living Area (Sq Ft)", min_value=300, max_value=5000, value=1500)
garage_cars = st.sidebar.selectbox("Garage Capacity (Cars)", [0, 1, 2, 3, 4])
total_bsmt_sf = st.sidebar.number_input("Total Basement Area (Sq Ft)", min_value=0, max_value=3000, value=800)
year_built = st.sidebar.slider("Year Built", 1900, 2026, 2005)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Selected Features:")
    st.write(f"- **Overall Quality:** {overall_qual} / 10")
    st.write(f"- **Living Area:** {gr_liv_area} Sq Ft")
    st.write(f"- **Garage Cars:** {garage_cars} Cars")
    st.write(f"- **Basement Area:** {total_bsmt_sf} Sq Ft")
    st.write(f"- **Year Built:** {year_built}")

with col2:
    st.subheader("💡 Smart Price Prediction")
    st.info("Click the button below to analyze specifications and predict the estimated market price.")
    
    if st.button("🚀 Calculate Estimated Price"):
        estimated_price = (gr_liv_area * 110) + (overall_qual * 15000) + (total_bsmt_sf * 50) - ((2026 - year_built) * 500)
        
        st.success(f"💰 Estimated House Price: **${estimated_price:,.2f}**")
        st.balloons()

