import streamlit as st
import pandas as pd

st.set_page_config(page_title="SoilSense AI+", layout="wide")

# Styling
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0b1220;
}

/* Full page faded icons */
.stApp::before {
    content:
    "🌾 🌱 🥔 🌽 🌿 🌾 🌱 🥔 🌽 🌿 \A
     🌱 🥔 🌽 🌾 🌿 🌱 🥔 🌽 🌾 🌿 \A
     🥔 🌽 🌿 🌾 🌱 🥔 🌽 🌿 🌾 🌱 \A
     🌾 🌱 🥔 🌽 🌿 🌾 🌱 🥔 🌽 🌿";
    white-space: pre;
    position: fixed;
    inset: 0;
    font-size: 34px;
    line-height: 3;
    word-spacing: 40px;
    opacity: 0.07;
    z-index: 0;
    pointer-events: none;
    padding: 20px;
}

/* Keep content above */
.main * {
    position: relative;
    z-index: 1;
}

/* Text */
h1, h2, h3, label, p, div, span {
    color: white !important;
}

/* Buttons */
.stButton > button {
    background-color: #2e7d32 !important;
    color: white !important;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    border: none;
}

/* Inputs */
input, textarea {
    background-color: #1e293b !important;
    color: white !important;
}

/* Dropdown container */
div[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    color: white !important;
}

/* Selected text inside dropdown */
div[data-baseweb="select"] * {
    color: white !important;
    fill: white !important;
}

/* Dropdown menu popup options */
ul[role="listbox"] {
    background-color: #1e293b !important;
}

ul[role="listbox"] li {
    color: white !important;
}

/* Number inputs */
div[data-testid="stNumberInput"] input {
    background-color: #1e293b !important;
    color: white !important;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background-color: #1e293b !important;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🌱 SoilSense AI+")

language = st.selectbox(
    "Select Language / भाषा / ਭਾਸ਼ਾ",
    ["English", "Hindi", "Punjabi"]
)

def tr(en, hi, pa):
    if language == "Hindi":
        return hi
    elif language == "Punjabi":
        return pa
    return en

st.subheader(
    tr(
        "Bio Integrated Soil Decision System",
        "जैव एकीकृत मृदा निर्णय प्रणाली",
        "ਜੈਵ ਇਕੀਕ੍ਰਿਤ ਮਿੱਟੀ ਫੈਸਲਾ ਪ੍ਰਣਾਲੀ"
    )
)

st.subheader(
    tr(
        "🎤 Smart Assistant",
        "🎤 स्मार्ट सहायक",
        "🎤 ਸਮਾਰਟ ਸਹਾਇਕ"
    )
)

voice_query = st.text_input(
    tr(
        "Ask about crop or soil",
        "फसल या मिट्टी के बारे में पूछें",
        "ਫਸਲ ਜਾਂ ਮਿੱਟੀ ਬਾਰੇ ਪੁੱਛੋ"
    )
)

# Input Layout
col1, col2 = st.columns(2)

with col1:
    N = st.number_input(tr("Nitrogen","नाइट्रोजन","ਨਾਈਟ੍ਰੋਜਨ"),0,150,50)

    P = st.number_input(tr("Phosphorus","फास्फोरस","ਫਾਸਫੋਰਸ"),0,150,50)

    K = st.number_input(tr("Potassium","पोटैशियम","ਪੋਟਾਸਿਯਮ"),0,150,50)

    ph = st.number_input(tr("pH","पीएच","ਪੀਐਚ"),0.0,14.0,6.5)

    soc = st.number_input(
        tr("Soil Organic Carbon","मृदा कार्बन","ਮਿੱਟੀ ਕਾਰਬਨ"),
        0.0,2.0,0.6
    )
with col2:
    temp = st.number_input(
        tr("Temperature","तापमान","ਤਾਪਮਾਨ"),
        0,50,25
    )

    humidity = st.number_input(
        tr("Humidity","आर्द्रता","ਨਮੀ"),
        0,100,60
    )

    rainfall = st.number_input(
        tr("Rainfall","वर्षा","ਬਰਸਾਤ"),
        0,300,100
    )

    micro = st.number_input(
        tr("Microbial Activity","सूक्ष्मजीव सक्रियता","ਸੂਖਮਜੀਵ ਸਰਗਰਮੀ"),
        1,10,5
    )

    previous_crop = st.selectbox(
        tr("Previous Crop","पिछली फसल","ਪਿਛਲੀ ਫਸਲ"),
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
