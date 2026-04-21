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

if st.button("Analyze Soil"):

    score = 100

    if ph < 5.5 or ph > 8:
        score -= 15
    if soc < 0.5:
        score -= 15
    if micro < 4:
        score -= 15

    st.success("Recommended Crop: Potato")

    st.metric("Soil Health Score", score)

    if score > 85:
        st.info("Healthy Soil")
    elif score > 65:
        st.warning("Moderate Soil")
    else:
        st.error("Poor Soil")

    st.subheader("Recommendations")
    st.write("✅ Add compost regularly")
    st.write("✅ Use biofertilizer")
    st.write("✅ Follow crop rotation")
