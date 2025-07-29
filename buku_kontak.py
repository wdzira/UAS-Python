import streamlit as st
import requests

BASE_URL = "https://bukukontak.streamlit.app"

# Kelas
class bukuKontak:
    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

    def __str__(self):
        return f"Nama: {self.nama}, Nomor: {self.nomor}"

# Data disimpan di list session_state
if 'dataKontak' not in st.session_state:
    st.session_state.dataKontak = []

# Tampilan
st.title("Buku Kontak")

st.write("### Pilihan Menu")
st.write("1. Tambah Kontak")
st.write("2. Lihat Kontak")
st.write("3. Cari Kontak")  
st.write("4. Hapus Kontak")

menu = st.text_input("Pilih Menu (1-4): ")

# Fungsi Menu
if menu == "1":
    st.subheader("Tambah Kontak")
    nama = st.text_input("Masukkan Nama")
    nomor = st.text_input("Masukkan Nomor")
    if st.button("Simpan"):
        if nama and nomor:
            kntk = bukuKontak(nama, nomor)
            st.session_state.dataKontak.append(kntk)
            st.success("Kontak Berhasil Ditambahkan!")
        else:
            st.warning("Harap isi semua kolom")
            
elif menu == "2":
    st.subheader("Daftar Kontak")  
    if st.session_state.dataKontak:
        for i, kntk in enumerate(st.session_state.dataKontak, 1):
            st.write(f"{i}. {kntk}")
    else:
        st.info("Belum ada kontak.")

elif menu == "3":
    st.subheader("Cari Kontak")
    search_term = st.text_input("Masukkan nama atau nomor yang dicari:")
    if search_term:
        results = []
        for kontak in st.session_state.dataKontak:
            if (search_term.lower() in kontak.nama.lower()) or (search_term in kontak.nomor):
                results.append(kontak)
        
        if results:
            st.success(f"Ditemukan {len(results)} kontak:")
            for i, result in enumerate(results, 1):
                st.write(f"{i}. {result}")
        else:
            st.warning("Tidak ditemukan kontak yang sesuai.")
            
elif menu == "4":
    st.subheader("Hapus Kontak")
    if st.session_state.dataKontak:
        # Tampilkan daftar kontak dengan radio button
        kontak_list = [f"{i+1}. {kontak.nama} - {kontak.nomor}" for i, kontak in enumerate(st.session_state.dataKontak)]
        selected = st.radio("Pilih kontak yang akan dihapus:", kontak_list)
        
        if st.button("Hapus Kontak"):
            index = kontak_list.index(selected)
            deleted_kontak = st.session_state.dataKontak.pop(index)
            st.success(f"Kontak {deleted_kontak.nama} berhasil dihapus!")
    else:
        st.info("Belum ada kontak yang bisa dihapus.")

elif menu != "":
    st.warning("Masukkan angka sesuai menu.")
