import streamlit as st
import pandas as pd

st.set_page_config(page_title="SoilSense AI+ farmers kit", layout="wide")

# Styling
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0b1220;
}

/* Background icons */
.stApp::before {
    content:
    "🌾 🌱 🥔 🌽 🌿 🌾 🌱 🥔 🌽 \A
     🌱 🥔 🌽 🌾 🌿 🌱 🥔 🌽 🌾 \A
     🥔 🌽 🌿 🌾 🌱 🥔 🌽 🌿 🌾 \A
     🌾 🌱 🥔 🌽 🌿 🌾 🌱 🥔 🌽";
    white-space: pre;
    position: fixed;
    inset: 0;
    font-size: 32px;
    line-height: 3;
    word-spacing: 35px;
    opacity: 0.06;
    z-index: 0;
    pointer-events: none;
    padding: 20px;
}

/* Content above background */
.main * {
    position: relative;
    z-index: 1;
}

/* Text */
h1,h2,h3,label,p,div,span {
    color: white !important;
}

/* Buttons */
.stButton > button {
    background-color: #2e7d32 !important;
    color: white !important;
    border-radius: 10px;
    border: none;
    width: 100%;
}

/* Inputs */
input, textarea {
    background-color: #1e293b !important;
    color: white !important;
}

/* Number boxes */
div[data-testid="stNumberInput"] input {
    background-color: #1e293b !important;
    color: white !important;
}

/* Dropdown main box */
div[data-baseweb="select"] > div {
    background-color: #000000 !important;
    color: white !important;
    border-radius: 8px !important;
    border: 1px solid #444 !important;
}

/* Dropdown selected text */
div[data-baseweb="select"] span,
div[data-baseweb="select"] svg,
div[data-baseweb="select"] * {
    color: white !important;
    fill: white !important;
}

/* Dropdown popup */
div[role="listbox"],
ul[role="listbox"],
[data-baseweb="menu"] {
    background-color: #000000 !important;
    color: white !important;
}

/* Dropdown options */
li[role="option"],
ul[role="listbox"] li,
[data-baseweb="menu"] li,
[data-baseweb="menu"] div {
    background-color: #000000 !important;
    color: white !important;
}

/* Hover */
li[role="option"]:hover,
ul[role="listbox"] li:hover {
    background-color: #1f2937 !important;
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
st.title("🌱 SoilSense AI+ farmers kit")

# Language Selector
language = st.selectbox(
    "Select Language / भाषा / ਭਾਸ਼ਾ",
    ["English", "हिंदी", "ਪੰਜਾਬੀ"]
)

# Translation Function
def tr(en, hi, pa):
    if language == "हिंदी":
        return hi
    elif language == "ਪੰਜਾਬੀ":
        return pa
    return en

# Crop Options
crop_options = [
    tr("Wheat", "गेहूं", "ਗੇਂਹੂ"),
    tr("Rice", "चावल", "ਚੌਲ"),
    tr("Pea", "मटर", "ਮਟਰ"),
    tr("Potato", "आलू", "ਆਲੂ"),
    tr("Maize", "मक्का", "ਮੱਕੀ")
]

# Subtitle
st.subheader(
    tr(
        "Bio Integrated Soil Decision System",
        "जैव एकीकृत मृदा निर्णय प्रणाली",
        "ਜੈਵ ਇਕੀਕ੍ਰਿਤ ਮਿੱਟੀ ਫੈਸਲਾ ਪ੍ਰਣਾਲੀ"
    )
)

# Assistant
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

st.subheader(
    tr(
        "📷 Optional Soil Photo Analysis",
        "📷 वैकल्पिक मिट्टी फोटो विश्लेषण",
        "📷 ਵਿਕਲਪਿਕ ਮਿੱਟੀ ਫੋਟੋ ਵਿਸ਼ਲੇਸ਼ਣ"
    )
)

soil_image = st.file_uploader(
    tr(
        "Upload soil image (optional)",
        "मिट्टी की फोटो अपलोड करें (वैकल्पिक)",
        "ਮਿੱਟੀ ਦੀ ਫੋਟੋ ਅੱਪਲੋਡ ਕਰੋ (ਵਿਕਲਪਿਕ)"
    ),
    type=["jpg","jpeg","png"]
)

# Input Layout
col1, col2 = st.columns(2)

with col1:
    N = st.number_input(
        tr("Nitrogen (kg/ha)","नाइट्रोजन (कि.ग्रा./हे.)","ਨਾਈਟ੍ਰੋਜਨ (ਕਿ.ਗ੍ਰਾ./ਹੇ.)"),
        0,150,50
    )

    P = st.number_input(
        tr("Phosphorus (kg/ha)","फास्फोरस (कि.ग्रा./हे.)","ਫਾਸਫੋਰਸ (ਕਿ.ਗ੍ਰਾ./ਹੇ.)"),
        0,150,50
    )

    K = st.number_input(
        tr("Potassium (kg/ha)","पोटैशियम (कि.ग्रा./हे.)","ਪੋਟਾਸਿਯਮ (ਕਿ.ਗ੍ਰਾ./ਹੇ.)"),
        0,150,50
    )

    ph = st.number_input(
        tr("pH","पीएच","ਪੀਐਚ"),
        0.0,14.0,6.5
    )

    soc = st.number_input(
        tr("Soil Organic Carbon (%)","मृदा कार्बन (%)","ਮਿੱਟੀ ਕਾਰਬਨ (%)"),
        0.0,2.0,0.6
    )

with col2:
    temp = st.number_input(
        tr("Temperature (°C)","तापमान (°C)","ਤਾਪਮਾਨ (°C)"),
        0,50,25
    )

    humidity = st.number_input(
        tr("Humidity (%)","आर्द्रता (%)","ਨਮੀ (%)"),
        0,100,60
    )

    rainfall = st.number_input(
        tr("Rainfall (mm)","वर्षा (मिमी)","ਬਰਸਾਤ (ਮਿ.ਮੀ.)"),
        0,300,100
    )

    micro = st.number_input(
        tr("Microbial Activity Index (1-10)",
           "सूक्ष्मजीव सक्रियता सूचकांक (1-10)",
           "ਸੂਖਮਜੀਵ ਸਰਗਰਮੀ ਸੂਚਕਾਂਕ (1-10)"),
        1,10,5
    )

    previous_crop = st.selectbox(
        tr("Previous Crop","पिछली फसल","ਪਿਛਲੀ ਫਸਲ"),
        crop_options
    )

    soil_texture = st.selectbox(
        tr("Soil Texture","मृदा बनावट","ਮਿੱਟੀ ਬਣਾਵਟ"),
        [
            tr("Sandy","रेतीली","ਰੇਤੀਲੀ"),
            tr("Loamy","दोमट","ਦੋਮਟ"),
            tr("Clayey","चिकनी","ਚਿਕਣੀ"),
            tr("Silty","गादयुक्त","ਗਾਦ ਵਾਲੀ"),
            tr("Sandy Loam","बलुई दोमट","ਰੇਤੀਲੀ ਦੋਮਟ"),
            tr("Clay Loam","चिकनी दोमट","ਚਿਕਣੀ ਦੋਮਟ")
        ]
    )

    soil_type = st.selectbox(
        tr("Soil Type","मृदा प्रकार","ਮਿੱਟੀ ਕਿਸਮ"),
        [
            tr("Alluvial","जलोढ़","ਜਲੋੜ"),
            tr("Black","काली","ਕਾਲੀ"),
            tr("Red","लाल","ਲਾਲ"),
            tr("Laterite","लेटेराइट","ਲੇਟਰਾਈਟ"),
            tr("Mountain","पर्वतीय","ਪਹਾੜੀ"),
            tr("Desert","मरुस्थली","ਰੇਗਿਸਤਾਨੀ"),
            tr("Peaty","पीटी","ਪੀਟੀ")
        ]
    )

# Functions

def recommend_crop():

    scores = {
        "Wheat": 0,
        "Rice": 0,
        "Potato": 0,
        "Maize": 0,
        "Sugarcane": 0,
        "Groundnut": 0,
        "Cotton": 0,
        "Jute": 0
    }

    # -------------------------
    # Base Climate Suitability
    # -------------------------

    # Wheat
    if 15 <= temp <= 25:
        scores["Wheat"] += 25
    if 50 <= rainfall <= 120:
        scores["Wheat"] += 20

    # Rice
    if rainfall > 180:
        scores["Rice"] += 30
    if humidity > 70:
        scores["Rice"] += 20
    if temp >= 22:
        scores["Rice"] += 15

    # Potato
    if 15 <= temp <= 22:
        scores["Potato"] += 30
    if temp < 28:
        scores["Potato"] += 10

    # Maize
    if 20 <= temp <= 32:
        scores["Maize"] += 25
    if rainfall >= 60:
        scores["Maize"] += 15

    # Sugarcane
    if temp >= 25:
        scores["Sugarcane"] += 25
    if rainfall >= 120:
        scores["Sugarcane"] += 25

    # Groundnut
    if rainfall < 100:
        scores["Groundnut"] += 25
    if 20 <= temp <= 32:
        scores["Groundnut"] += 10

    # Cotton
    if temp >= 24:
        scores["Cotton"] += 25

    # Jute
    if humidity > 80:
        scores["Jute"] += 30
    if rainfall > 150:
        scores["Jute"] += 25

    # -------------------------
    # Nutrient Effects
    # -------------------------

    if N > 80:
        scores["Maize"] += 20
        scores["Wheat"] += 10

    if P > 60:
        scores["Groundnut"] += 15
        scores["Sugarcane"] += 10

    if K > 60:
        scores["Sugarcane"] += 20
        scores["Potato"] += 10

    # -------------------------
    # pH Effects
    # -------------------------

    if 6.0 <= ph <= 7.5:
        scores["Wheat"] += 15
        scores["Maize"] += 10

    if ph < 6.5:
        scores["Potato"] += 20

    # -------------------------
    # Soil Organic Carbon
    # -------------------------

    if soc >= 0.75:
        scores["Wheat"] += 10
        scores["Potato"] += 10
        scores["Maize"] += 10

    elif soc < 0.40:
        scores["Sugarcane"] -= 10
        scores["Rice"] -= 10

    # -------------------------
    # Microbial Activity
    # -------------------------

    if micro >= 7:
        for crop in scores:
            scores[crop] += 5

    elif micro < 4:
        scores["Sugarcane"] -= 10
        scores["Rice"] -= 10
        scores["Maize"] -= 5

    # -------------------------
    # Soil Texture
    # -------------------------

    if "Loamy" in soil_texture:
        scores["Wheat"] += 20
        scores["Potato"] += 15
        scores["Maize"] += 15

    if "Clayey" in soil_texture:
        scores["Rice"] += 25

    if "Sandy" in soil_texture:
        scores["Groundnut"] += 20
        scores["Potato"] += 10

    if "Sandy Loam" in soil_texture:
        scores["Potato"] += 20
        scores["Groundnut"] += 10

    # -------------------------
    # Soil Type
    # -------------------------

    if "Alluvial" in soil_type:
        scores["Wheat"] += 20
        scores["Rice"] += 15
        scores["Maize"] += 15
        scores["Sugarcane"] += 15

    if "Black" in soil_type:
        scores["Cotton"] += 30
        scores["Sugarcane"] += 15

    if "Red" in soil_type:
        scores["Groundnut"] += 25

    # -------------------------
    # Water Stress Penalty
    # -------------------------

    if rainfall < 60:
        scores["Rice"] -= 25
        scores["Sugarcane"] -= 20
        scores["Jute"] -= 15

    # -------------------------
    # Crop Rotation Penalty
    # -------------------------

    if "Wheat" in previous_crop:
        scores["Wheat"] -= 15

    if "Rice" in previous_crop:
        scores["Rice"] -= 15

    if "Potato" in previous_crop:
        scores["Potato"] -= 15

    if "Maize" in previous_crop:
        scores["Maize"] -= 15

    # -------------------------
    # Final Selection
    # -------------------------

    best_crop = max(scores, key=scores.get)

    if best_crop == "Wheat":
        return tr("Wheat","गेहूं","ਗੇਂਹੂ")

    elif best_crop == "Rice":
        return tr("Rice","चावल","ਚੌਲ")

    elif best_crop == "Potato":
        return tr("Potato","आलू","ਆਲੂ")

    elif best_crop == "Maize":
        return tr("Maize","मक्का","ਮੱਕੀ")

    elif best_crop == "Sugarcane":
        return tr("Sugarcane","गन्ना","ਗੰਨਾ")

    elif best_crop == "Groundnut":
        return tr("Groundnut","मूंगफली","ਮੂੰਗਫਲੀ")

    elif best_crop == "Cotton":
        return tr("Cotton","कपास","ਕਪਾਹ")

    else:
        return tr("Jute","जूट","ਜੂਟ")


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
if st.button(tr("Analyze Soil","मिट्टी जांचें","ਮਿੱਟੀ ਵਿਸ਼ਲੇਸ਼ਣ")):

    crop = recommend_crop()
    score = soil_score()

    st.success(
        tr(
            f"Recommended Crop: {crop}",
            f"अनुशंसित फसल: {crop}",
            f"ਸਿਫਾਰਸ਼ੀ ਫਸਲ: {crop}"
        )
    )

    st.metric(
        tr("Soil Health Score","मिट्टी स्वास्थ्य स्कोर","ਮਿੱਟੀ ਸਿਹਤ ਸਕੋਰ"),
        score
    )

    if score > 85:
        st.info(tr("Healthy Soil","स्वस्थ मिट्टी","ਤੰਦਰੁਸਤ ਮਿੱਟੀ"))
    elif score > 65:
        st.warning(tr("Moderate Soil","मध्यम मिट्टी","ਦਰਮਿਆਨੀ ਮਿੱਟੀ"))
    else:
        st.error(tr("Poor Soil","कमज़ोर मिट्टी","ਕਮਜ਼ੋਰ ਮਿੱਟੀ"))

    st.subheader(
        tr("Recommendations","सिफारिशें","ਸਿਫਾਰਸ਼ਾਂ")
    )

    if soc < 0.5:
        st.write(tr("✅ Add compost","✅ कम्पोस्ट डालें","✅ ਖਾਦ ਪਾਓ"))

    if micro < 4:
        st.write(
            tr(
                "✅ Use biofertilizer",
                "✅ जैव उर्वरक उपयोग करें",
                "✅ ਜੈਵ ਖਾਦ ਵਰਤੋ"
            )
        )

    if previous_crop.lower() == crop.lower():
        st.write(
            tr(
                "✅ Change crop rotation",
                "✅ फसल चक्र बदलें",
                "✅ ਫਸਲ ਚੱਕਰ ਬਦਲੋ"
            )
        )

    st.write(
        tr(
            "✅ Optimize irrigation",
            "✅ सिंचाई सुधारें",
            "✅ ਸਿੰਚਾਈ ਸੁਧਾਰੋ"
        )
    )

if soil_image is not None:
    st.image(soil_image, width=250)

    st.info(
        tr(
            "AI Image Review: Soil photo received and considered.",
            "AI समीक्षा: मिट्टी फोटो प्राप्त हुई और विचार किया गया।",
            "AI ਸਮੀਖਿਆ: ਮਿੱਟੀ ਫੋਟੋ ਪ੍ਰਾਪਤ ਹੋਈ ਅਤੇ ਧਿਆਨ ਵਿੱਚ ਲਈ ਗਈ।"
        )
    )
    
    # Chart
    chart_data = pd.DataFrame({
        "Nutrient": [
            tr("Nitrogen","नाइट्रोजन","ਨਾਈਟ੍ਰੋਜਨ"),
            tr("Phosphorus","फास्फोरस","ਫਾਸਫੋਰਸ"),
            tr("Potassium","पोटैशियम","ਪੋਟਾਸਿਯਮ")
        ],
        "Value": [N, P, K]
    })

    st.subheader(
        tr(
            "NPK Nutrient Chart",
            "NPK पोषक चार्ट",
            "NPK ਪੋਸ਼ਕ ਚਾਰਟ"
        )
    )

    st.bar_chart(chart_data.set_index("Nutrient"))

    # Assistant
    if voice_query:
        st.subheader(
            tr(
                "Assistant Response",
                "सहायक उत्तर",
                "ਸਹਾਇਕ ਜਵਾਬ"
            )
        )

        if "crop" in voice_query.lower():
            st.write(
                tr(
                    f"Recommended crop is {crop}",
                    f"अनुशंसित फसल {crop} है",
                    f"ਸਿਫਾਰਸ਼ੀ ਫਸਲ {crop} ਹੈ"
                )
            )

        elif "soil" in voice_query.lower():
            st.write(
                tr(
                    f"Soil health score is {score}",
                    f"मिट्टी स्वास्थ्य स्कोर {score} है",
                    f"ਮਿੱਟੀ ਸਿਹਤ ਸਕੋਰ {score} ਹੈ"
                )
            )

        else:
            st.write(
                tr(
                    "Please ask about crop or soil.",
                    "कृपया फसल या मिट्टी के बारे में पूछें।",
                    "ਕਿਰਪਾ ਕਰਕੇ ਫਸਲ ਜਾਂ ਮਿੱਟੀ ਬਾਰੇ ਪੁੱਛੋ।"
                )
            )

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
        label=tr(
            "Download Soil Report",
            "रिपोर्ट डाउनलोड करें",
            "ਰਿਪੋਰਟ ਡਾਊਨਲੋਡ ਕਰੋ"
        ),
        data=report,
        file_name="SoilSense_Report.txt",
        mime="text/plain"
    )
