import streamlit as st
import pickle as pkl
import numpy as np

model = pkl.load(open("model.pkl","rb"))

st.title('Farmer Helper')

x1 = st.slider('Temperature of the field', 8.82, 43.67)
x2 = st.slider('Humidity of the field', 18.09, 99.98)
x3= st.slider('PH value of the field',4.50, 7.99)	
x4 = st.slider('Rain Fall of the field', 40.35, 298.56)
x5 = st.slider('Nitrate of the field', 20.00, 120.0)	
x6 = st.slider('phropus of the field',10.0, 125.07)
x7 = st.slider('potashm of the field', 10.0, 200.00)

x = np.array([[x1,x2,x3,x4,x5,x6,x7]])
ans = model.predict(x)
st.text(ans)