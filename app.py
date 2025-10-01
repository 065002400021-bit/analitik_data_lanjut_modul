import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Streamlit Simple App')

# Menambahkan navigasi di sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")

    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Tampilkan data di Streamlit
    st.write(data)



elif page == "Visualisasi":
    st.header("Halaman Visualisasi")
       # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Filter berdasarkan universitas
    selected_university = st.selectbox(
        'Pilih Universitas', 
        data['universitas'].unique()
    )
    filtered_data = data[data['universitas'] == selected_university]

    # Buat visualisasi
    plt.figure(figsize=(12, 6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]

        # Urutkan data berdasarkan 'id' (descending)
        subset = subset.sort_values(by="id", ascending=False)

        plt.plot(
            subset['semester'],
            subset['jumlah'],
            label=prog_studi
        )

    # Tambahkan detail grafik
    plt.title(f"Visualisasi Data untuk {selected_university}")
    plt.xlabel('Semester')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=90)  # rotasi label sumbu x biar lebih jelas
    plt.legend()

    # Tampilkan di Streamlit
    st.pyplot()

fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])
# other plotting actions...
st.pyplot(fig)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12,6))
ax.plot([1,2,3,4], [10,20,25,30])
ax.set_title("Contoh Visualisasi")

st.pyplot(fig)
 
fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])
# other plotting actions...
st.pyplot(fig)