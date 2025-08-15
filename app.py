import streamlit as st

st.title("📊 Kalkulator Nilai Rata-rata Peserta Didik")

st.write("Masukkan nilai untuk setiap mata pelajaran, lalu tekan tombol hitung.")

# Input nilai
mtk = st.number_input("Nilai Matematika", min_value=0.0, max_value=100.0, step=0.1)
bindo = st.number_input("Nilai Bahasa Indonesia", min_value=0.0, max_value=100.0, step=0.1)
bing = st.number_input("Nilai Bahasa Inggris", min_value=0.0, max_value=100.0, step=0.1)
ipa = st.number_input("Nilai IPA", min_value=0.0, max_value=100.0, step=0.1)
ips = st.number_input("Nilai IPS", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Hitung Rata-rata"):
    rata = (mtk + bindo + bing + ipa + ips) / 5
    st.write(f"**Rata-rata Nilai:** {rata:.2f}")

    # Kategori kelulusan
    if rata >= 75:
        st.success("✅ Lulus - Nilai Anda sangat baik!")
    elif rata >= 60:
        st.warning("⚠️ Lulus Bersyarat - Perlu peningkatan.")
    else:
        st.error("❌ Tidak Lulus - Tetap semangat belajar!")
