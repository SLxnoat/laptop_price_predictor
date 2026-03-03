# 💻 Laptop Price Predictor (End-to-End ML Project)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://laptop-price-predictor-xnoat.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange?style=flat-square&logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=flat-square&logo=pandas)

Buying a laptop is a complex decision with hundreds of configurations. This project uses **Machine Learning** to help users estimate the market price of a laptop based on hardware specifications.

## 🚀 Live Demo
You can try the live application here:  
🔗 **[Laptop Price Predictor Web App](https://laptop-price-predictor-xnoat.streamlit.app/)**

---

## 📸 Screenshots
<p align="center">
  <img src="https://github.com/SLxnoat/laptop_price_predictor/blob/main/app_screenshot.png" width="700" alt="App Preview">
</p>
*(Note: Replace this image link with a screenshot of YOUR actual app once you upload it to GitHub)*

---

## 📊 Project Highlights
- **Target:** Predict laptop prices in a continuous range (Regression).
- **Algorithm:** Random Forest Regressor.
- **Accuracy (R2 Score):** `0.887` (Top tier performance).
- **Error (MAE):** `0.157` (On log-transformed values).

### ⚙️ Feature Engineering
- **PPI Calculation:** Extracted Pixels Per Inch from Screen Resolution and Size.
- **CPU/GPU Cleaning:** Simplified complex text data into meaningful Brand categories.
- **Storage Splitting:** Separated Memory into dedicated HDD and SSD columns.

---

## 🛠️ Installation & Usage

### 1. Clone the repository
```
  git clone [https://github.com/SLxnoat/laptop_price_predictor.git](https://github.com/SLxnoat/laptop_price_predictor.git)
  cd laptop_price_predictor
```
### 2. Create a Virtual Environment
````
  python -m venv env
````
On Windows:
````
  .\env\Scripts\activate
````
### 3. Install Dependencies
```
pip install -r requirements.txt
````
### 4. Run the App
```
streamlit run app.py
````
## 📂 Repository Structure
```text
├── data/
│   ├── laptop_data.csv          # Raw dataset
│   └── cleaned_laptop_data.csv  # Preprocessed dataset
├── notebooks/
│   ├── data_Preprocessing.ipynb # Data cleaning steps
│   └── model_building.ipynb     # Model training & evaluation
├── app.py                       # Streamlit Web Application
├── pipe.pkl                     # Trained ML Pipeline
├── df.pkl                       # Processed DataFrame for UI
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
````
## 🧠 Lessons Learned
Handling skewed data using Log Transformation.

Building Scikit-Learn Pipelines for seamless data flow from raw input to prediction.

Deploying ML models into a production-ready Streamlit environment.

<p align="center">Made with ❤️ by Mayura Bandara</p>
