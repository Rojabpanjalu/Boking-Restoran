import streamlit as st
import requests
import uuid

API_URL = "http://localhost:8000/bookings"

st.title("🍽️ Booking Meja Restoran")

with st.form("booking_form"):
    name = st.text_input("Nama Lengkap")
    phone = st.text_input("Nomor HP")
    date = st.date_input("Tanggal Reservasi")
    time = st.time_input("Jam")
    people = st.number_input("Jumlah Orang", min_value=1, step=1)
    submitted = st.form_submit_button("Booking Sekarang")

    if submitted:
        booking_data = {
            "id": str(uuid.uuid4()),
            "name": name,
            "phone": phone,
            "date": str(date),
            "time": str(time),
            "people": people
        }

        response = requests.post(API_URL, json=booking_data)

        if response.status_code == 200:
            st.success("✅ Booking berhasil!")
            st.json(response.json())
        else:
            st.error("❌ Gagal melakukan booking.")

st.markdown("---")
st.subheader("📋 Riwayat Booking")

if st.button("Lihat Riwayat"):
    res = requests.get(API_URL)
    if res.status_code == 200:
        data = res.json()
        for item in data:
            st.write(f"🧍 {item['name']} | 📅 {item['date']} {item['time']} | 👥 {item['people']} orang")
    else:
        st.error("Gagal mengambil data booking.")
