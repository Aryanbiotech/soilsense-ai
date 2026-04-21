import streamlit as st
import pandas as pd

st.set_page_config(page_title="SoilSense AI+", layout="wide")

# Styling
st.markdown("""
<style>
.main {
    background-color: #f5f7f9;
}
h1 {
    color: #1b5e20;
}
.stButton>button {
    background-color: #2e7d32;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🌱 SoilSense AI+")
st.subheader("Bio Integrated Soil Decision System")

# Voice Assistant
st.subheader("🎤 Smart Assistant")
voice_query = st.text_input("Ask about crop or soil")

# Input Layout
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen",0,150,50)
    P = st.number_input("Phosphorus",0,150,50)
    K = st.number_input("Potassium",0,150,50)
    ph = st.number_input("pH",0.0,14.0,6.5)
    soc = st.number_input("Soil Organic Carbon",0.0,2.0,0.6)

with col2:
    temp = st.number_input("Temperature",0,50,25)
    humidity = st.number_input("Humidity",0,100,60)
    rainfall = st.number_input("Rainfall",0,300,100)
    micro = st.number_input("Microbial Activity",1,10,5)
    previous_crop = st.selectbox(
        "Previous Crop",
        ["wheat","rice","pea","potato","maize"]
    )

# Functions
def recommend_crop():
    if rainfall > 220 and humidity > 75:
        return "Rice"
    elif ph < 6.0 and temp < 28:
        return "Potato"
    elif N > 90 and temp > 22:
        return "Maize"
    elif humidity > 80 and rainfall > 150:
        return "Jute"
    elif P > 60 and K > 60:
        return "Sugarcane"
    else:
        return "Wheat"

def soil_score():
    score = 100

    if N < 60:
        score -= 15
    if P < 40:
        score -= 15
    if K < 40:
        score -= 15
    if ph < 6 or ph > 7.5:
        score -= 20
    if soc < 0.75:
        score -= 15
    if micro < 6:
        score -= 20

    return max(score,0)

# Main Button
if st.button("Analyze Soil"):

    crop = recommend_crop()
    score = soil_score()

    st.success(f"Recommended Crop: {crop}")
    st.metric("Soil Health Score", score)

    if score > 85:
        st.info("Healthy Soil")
    elif score > 65:
        st.warning("Moderate Soil")
    else:
        st.error("Poor Soil")

    # Recommendations
    st.subheader("Recommendations")

    if soc < 0.5:
        st.write("✅ Add compost")

    if micro < 4:
        st.write("✅ Use biofertilizer")

    if previous_crop.lower() == crop.lower():
        st.write("✅ Change crop rotation")

    st.write("✅ Optimize irrigation")

    # Chart
    chart_data = pd.DataFrame({
        "Nutrient": ["Nitrogen","Phosphorus","Potassium"],
        "Value": [N,P,K]
    })

    st.subheader("NPK Nutrient Chart")
    st.bar_chart(chart_data.set_index("Nutrient"))

    # Voice Assistant
    if voice_query:
        st.subheader("Assistant Response")

        if "crop" in voice_query.lower():
            st.write(f"Recommended crop is {crop}")

        elif "soil" in voice_query.lower():
            st.write(f"Soil health score is {score}")

        else:
            st.write("Please ask about crop or soil.")

    # Download Report
    report = f"""
SoilSense AI+ Report

Recommended Crop: {crop}
Soil Health Score: {score}

Nitrogen: {N}
Phosphorus: {P}
Potassium: {K}
pH: {ph}
Organic Carbon: {soc}
Microbial Activity: {micro}
Previous Crop: {previous_crop}
"""

    st.download_button(
        label="Download Soil Report",
        data=report,
        file_name="SoilSense_Report.txt",
        mime="text/plain"
    )
