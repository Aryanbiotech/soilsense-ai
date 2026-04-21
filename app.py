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
import streamlit as st

st.set_page_config(page_title="SoilSense AI+", layout="wide")

st.title("🌱 SoilSense AI+")
st.subheader("Bio Integrated Soil Decision System")

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

def recommend_crop():
    if rainfall > 200:
        return "Rice"
    elif ph < 6:
        return "Potato"
    elif N > 80:
        return "Maize"
    elif humidity > 75:
        return "Jute"
    else:
        return "Wheat"

def soil_score():
    score = 100

    if N < 40:
        score -= 10
    if P < 30:
        score -= 10
    if K < 30:
        score -= 10
    if ph < 5.5 or ph > 8:
        score -= 15
    if soc < 0.5:
        score -= 15
    if micro < 4:
        score -= 15

    return max(score,0)

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

    st.subheader("Recommendations")

    if soc < 0.5:
        st.write("✅ Add compost")

    if micro < 4:
        st.write("✅ Use biofertilizer")

    if previous_crop.lower() == crop.lower():
        st.write("✅ Change crop rotation")

    st.write("✅ Optimize irrigation")
