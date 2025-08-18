import streamlit as st

st.title("📐 Kalkulator Luas Persegi Panjang")

# Input panjang dan lebar
panjang = st.number_input("Masukkan panjang (cm):", min_value=0.0, step=0.1)
lebar = st.number_input("Masukkan lebar (cm):", min_value=0.0, step=0.1)

# Hitung luas
if st.button("Hitung Luas"):
    luas = panjang * lebar
    st.success(f"Luas persegi panjang adalah: {luas} cm²")
    st.write("👉 Rumus: **Luas = Panjang × Lebar**")
