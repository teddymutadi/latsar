import streamlit as st

st.write("""
# Aplikasi Luas Segitiga 
Ini adalah aplikasi menghitung luas segita
sederhana menggunakan Streamlit
""")

alas = st.number_input("Masukkan Alas:", 0)
tinggi = st.number_input("Masukkan Tinggi:", 0)
hitung = st.button("Hitung Luas")

if hitung:
   luas = 0.5 * alas * tinggi
   st.write("Luas segitiganya adalah:", luas)
   st.success(f"Luas segitiganya adalah {luas}")
   st.balloons()