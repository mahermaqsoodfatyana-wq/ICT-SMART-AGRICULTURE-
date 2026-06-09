import streamlit as st

st.set_page_config(
    page_title="ICT in Smart Agriculture",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 ICT in Smart Agriculture")
st.subheader("Smart Farming Solution for Modern Agriculture")

st.markdown("""
### About Project
Information and Communication Technology (ICT) plays a vital role in modern agriculture.
This project highlights how technology such as drones, sensors, IoT, GPS, and data analytics
can improve crop production, reduce costs, and help farmers make better decisions.

### Key Technologies
- 🚁 Smart Drones
- 🌡️ IoT Sensors
- 📡 GPS Monitoring
- ☁️ Cloud Computing
- 📊 Data Analytics
- 🤖 AI-Based Farming

### Benefits
- Increased Crop Yield
- Efficient Water Usage
- Early Disease Detection
- Reduced Labor Costs
- Precision Agriculture
""")

st.header("Smart Agriculture Dashboard")

soil_moisture = st.slider("Soil Moisture (%)", 0, 100, 65)
temperature = st.slider("Temperature (°C)", 0, 50, 28)
humidity = st.slider("Humidity (%)", 0, 100, 70)

st.write("### Current Field Status")

if soil_moisture < 40:
    st.warning("⚠️ Soil moisture is low. Irrigation recommended.")
else:
    st.success("✅ Soil moisture level is good.")

if temperature > 35:
    st.warning("⚠️ High temperature detected.")
else:
    st.success("✅ Temperature is within normal range.")

st.header("Project Team")

st.markdown("""
1. **Maqsood Ahmad (25ME142)**
2. **M. Abdullah (25ME162)**
3. **M. Haseeb (25ME154)**
4. **Azmat u Allah (25ME198)**
5. **Syed Sabih Gillani (25ME226)**
""")

st.header("Future Scope")

st.markdown("""
- Real-time drone monitoring
- AI-based crop disease detection
- Weather prediction system
- Automated irrigation control
- Farmer support platform
""")

st.success("ICT in Smart Agriculture Project Successfully Running on Streamlit Cloud 🚀")
