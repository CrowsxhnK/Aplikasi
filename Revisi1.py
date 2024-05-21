import streamlit as st

def nama_senyawa(anion, kation):
    nama_anion = {
        "Cl": "Klorida",
        "Br": "Bromida",
        "I": "Iodida",
        "O": "Oksida",
        "S": "Sulfida",
        "PO4": "Fosfat",
        "NO3": "Nitrat",
        "NO2": "Nitrit",
        "CH3COO": "Asetat",
        "ClO": "Hipoklorit",
        "ClO2": "Klorit",
        "ClO3": "Klorat",
        "CN": "Sianida",
        "OH": "Hidroksida",
        "SO3": "Sulfit",
        "SO4": "Sulfat",
        "CO3": "Karbonat",
        "SiO3": "Silikat",
        "CrO4": "Kromat",
        "Cr2O7": "Dikromat",
        "BrO": "Hipobromit",
        "BrO3": "Bromat",
        "C2O4": "Oksalat",
        "PO3": "Fosfit",
        "AsO3": "Arsenit",
        "AsO4": "Arsenat",
        "SbO3": "Antimonit",
        "SbO4": "Antimonat",
        "S2O3": "Tiosulfat",
        "MnO4": "Permanganat",
        "F": "Fluorida"
    }

    nama_kation = {
        "Na": "Natrium",
        "K": "Kalium",
        "Ca": "Kalsium",
        "Mg": "Magnesium",
        "Fe": "Besi",
        "Ag": "Perak",
        "NH4": "Amonium",
        "H": "Asam",
        "Sr": "Stronsium",
        "Ba": "Barium",
        "Al": "Aluminium",
        "Zn": "Seng",
        "Ni": "Nikel",
        "Sn": "Timah",
        "Pb": "Timbal",
        "Hg": "Raksa",
        "Cu": "Tembaga",
        "Au": "Emas",
        "Pt": "Platina"
    }

    if anion in nama_anion and kation in nama_kation:
        nama_senyawa = nama_kation[kation] + " " + nama_anion[anion]
        return nama_senyawa

# Buat di Streamlit
st.title("Mengubah Simbol Anion dan Kation menjadi Nama Senyawa")

# mengubah background
st.markdown(""" <style>.stApp {background-color: #ADD8E6;");
        background-size: cover;}</style>""", unsafe_allow_html=True)

# Sidebar menu
menu = st.sidebar.selectbox("Pilih Menu", ("Mengubah Simbol", "Pengertian Anion dan Kation", "Anggota","Tabel Periodik"))

if menu == "Mengubah Simbol":
    st.write("Pilih simbol anion dan kation untuk mendapatkan nama senyawa yang sesuai.")
    
    nama_anion = {
        "Cl": "Klorida",
        "Br": "Bromida",
        "I": "Iodida",
        "O": "Oksida",
        "S": "Sulfida",
        "PO4": "Fosfat",
        "NO3": "Nitrat",
        "NO2": "Nitrit",
        "CH3COO": "Asetat",
        "ClO": "Hipoklorit",
        "ClO2": "Klorit",
        "ClO3": "Klorat",
        "CN": "Sianida",
        "OH": "Hidroksida",
        "SO3": "Sulfit",
        "SO4": "Sulfat",
        "CO3": "Karbonat",
        "SiO3": "Silikat",
        "CrO4": "Kromat",
        "Cr2O7": "Dikromat",
        "BrO": "Hipobromit",
        "BrO3": "Bromat",
        "C2O4": "Oksalat",
        "PO3": "Fosfit",
        "AsO3": "Arsenit",
        "AsO4": "Arsenat",
        "SbO3": "Antimonit",
        "SbO4": "Antimonat",
        "S2O3": "Tiosulfat",
        "MnO4": "Permanganat",
        "F": "Fluorida"
    }

    nama_kation = {
        "Na": "Natrium",
        "K": "Kalium",
        "Ca": "Kalsium",
        "Mg": "Magnesium",
        "Fe": "Besi",
        "Ag": "Perak",
        "NH4": "Amonium",
        "H": "Asam",
        "Sr": "Stronsium",
        "Ba": "Barium",
        "Al": "Aluminium",
        "Zn": "Seng",
        "Ni": "Nikel",
        "Sn": "Timah",
        "Pb": "Timbal",
        "Hg": "Raksa",
        "Cu": "Tembaga",
        "Au": "Emas",
        "Pt": "Platina"
    }

    kation = st.selectbox("Pilih simbol kation:", list(nama_kation.keys()))
    anion = st.selectbox("Pilih simbol anion:", list(nama_anion.keys()))
    
    if st.button("Hasil"):
        result = nama_senyawa(anion, kation)
        st.success("Nama senyawa: {}".format(result))
    st. image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDBlOXo0bnFlb29rbnphajR1dmgydDA3bmI3MDM1MGNlbTIxeDN5bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/r89IF7dudGBRz1RCUx/giphy.gif",width=200)

elif menu == "Pengertian Anion dan Kation":
    st.subheader("Pengertian Anion dan Kation")
    st.write("""Pengertian Anion  :""","Nama anion sendiri merupakan asalnya dari bahasa Yunani yaitu “ano”. Artinya naik.Pembentukan anion terjadi saat atom yang bukan logam mendapatkan satu atau lebih elektron. Pertambahan adanya elektron valensi dengan muatan negatif yang merubah atom tersebut.Atom dengan muatan awal netral kemudian menjadi bermuatan negatif. Oleh karena itu, tanda yang dimiliki oleh anion yaitu negatif (-) di bagian samping dari nama atom.Sementara angka yang ada di samping tanda negatif tersebut menunjukkan jumlah elektron yang sudah diterima oleh atom.")
    st.write("""Pengertian Kation  :""","Istilah kation sendiri asalnya dari bahasa Yunani yaitu “kata” yang memiliki arti turun.Pada atom terdapat elektron yang terletak di bagian lapisan sub kulit terluar atau disebut juga sebagai elektron valensi. Kation merupakan atom yang kehilangan satu maupun lebih dari elektron yang ada. Elektron yang hilang tersebut merupakan muatan negatif.Hal tersebut membuat atom yang awalnya memiliki muatan netral menjadi bermuatan positif. Atom dengan muatan positif tersebut yang dinamakan sebagai kation.Kation biasa ditandai dengan simbol positif (+) di bagian samping dari nama atomnya.")

elif menu == "Anggota":
    st.subheader("Disusun Oleh Kelompok 2")
    st.write("""
1. ADINDA NAZWA         (2360058)
2. DANNISA ALZULLA      (2360093)
3. DITYA ABIMANYU       (2360111)
4. M. NAZRIL NASWAN     (2360189)
5. TRISTARANI AZIZAH    (2360279)
    """)
    st.image("https://upload.wikimedia.org/wikipedia/id/thumb/8/82/Logo_Politeknik_AKA_Bogor.png/300px-Logo_Politeknik_AKA_Bogor.png", width=300)

elif menu == "Tabel Periodik":
    st.subheader("Berikut Adalah tabel periodik Serta di golongan berapa anion dan kation tersebut")
    st.image("https://e7.pngegg.com/pngimages/803/931/png-clipart-periodic-table-chemical-element-chemistry-neon-table.png")
    st.subheader("Kation")
    st.write("kation gol 1: Ag+, Hg+, Pb2+")
    st.write("kation gol 2: Cu, Sn 2+, Sn 3+")
    st.write("kation gol 3: Co2+, Ni2+, Fe2+, Fe3+, Cr3+, Al3+, Zn2+, Mn2+")
    st.write("kation gol 4: Ca2+ , Sr2+, dan Ba2+")
    st.write("kation gol 5: K +, Li 3+,Na+ dan Nh4+")

    st.subheader("Anion")
    st.write("Anion dibagi menjadi 3 golongan umum")
    st.write("Golongan Sulfat : SO4-,CO3 2-,PO4 3-,CrO4 2-,C2O4 2-,dan AsO4 3-")
    st.write("Golongan Nitrat:NO3-,NO2-,CLO3-,C2H2O2-,")
    st.write("Golongan Klorida/Halida:CCl-,Br-,I-SCN-,S2-")