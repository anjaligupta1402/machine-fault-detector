# Machine Fault Detector 🔧

## About
An AI-based machine fault detection system that uses sound analysis to identify potential faults in machines. It helps in predictive maintenance by detecting issues early, reducing downtime and maintenance costs.

## Features
- Analyzes machine sound/audio data
- Detects abnormal patterns indicating faults
- Early warning for predictive maintenance
- Simple web interface for easy use

## Tech Stack
- Python
- Streamlit (Web App Interface)
- Scikit-learn (Machine Learning Model)
- Soundfile & Scipy (Audio Processing)
- NumPy, Joblib

## How It Works
1. Machine sound file is uploaded/recorded
2. Audio features are extracted using Soundfile & Scipy
3. Trained ML model (scikit-learn) analyzes the pattern
4. System predicts whether the machine is normal or faulty

## How to Run
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Future Scope
- Real-time fault detection
- Integration with IoT sensors
- Dashboard for monitoring multiple machines
