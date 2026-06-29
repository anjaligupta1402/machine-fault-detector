import streamlit as st
import numpy as np
import joblib
import soundfile as sf
import scipy.signal as signal

model = joblib.load('fault_model.pkl')
st.title('Machine Fault Detector (Sound-Based)')
st.write('Machine ki sound upload karo, AI bataega Normal hai ya Faulty')

uploaded_file = st.file_uploader('Audio file upload karo (.wav)', type=['wav'])

if uploaded_file is not None:
    data, samplerate = sf.read(uploaded_file)
    if len(data.shape) > 1:
        data = data[:, 0]
    n_mfcc = 40
    mfccs = []
    for i in range(n_mfcc):
        mfccs.append(np.mean(data[i::n_mfcc]))
    features = np.array(mfccs).reshape(1, -1)
    prediction = model.predict(features)[0]
    if prediction == 0:
        st.success('Machine Normal hai')
    else:
        st.error('Fault Detected! Machine mein problem ho sakti hai')
