import streamlit as st
import pickle
import numpy as np

# Page Configuration
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
    }
    .prediction-text {
        text-align: center;
        color: #1f77b4;
        font-size: 30px;
        font-weight: bold;
        padding: 20px;
        border: 2px solid #1f77b4;
        border-radius: 10px;
        background-color: #e1f5fe;
    }
    </style>
    """, unsafe_allow_html=True)

# model load
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("💻 Laptop Price Predictor")
st.write("Enter the specifications below to get an estimated market price.")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Configuration")
    company = st.selectbox('Brand', df['Company'].unique())
    type = st.selectbox('Type', df['TypeName'].unique())
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64, 128])
    weight = st.number_input('Weight of the Laptop (kg)', value=1.5)
    os = st.selectbox('Operating System', df['os'].unique())

with col2:
    st.subheader("Display & Performance")
    cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())
    gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    ips = st.selectbox('IPS Panel', ['No', 'Yes'])
    screen_size = st.number_input('Screen Size (Inches)', value=15.6)
    resolution = st.selectbox('Screen Resolution', ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

st.divider()

# Storage
col3, col4, col5 = st.columns(3)
with col3:
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048, 4096])
with col4:
    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024, 2048, 4096])

st.write("") 

# Prediction Button
if st.button('Predict Estimated Price'):
    # Logic
    ts = 1 if touchscreen == 'Yes' else 0
    ips_panel = 1 if ips == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    
    if screen_size > 0:
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
        
        query = np.array([company, type, ram, weight, ts, ips_panel, ppi, cpu, hdd, ssd, 0, 0, gpu, os])
        query = query.reshape(1, 14)

        prediction = int(np.exp(pipe.predict(query)[0]))

        st.markdown(f"""
            <div class="prediction-text">
                The predicted price is approximately: <br>
                LKR {prediction:,}
            </div>
            """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("Please enter a valid Screen Size.")