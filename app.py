import streamlit as st
import pdfplumber

st.title("Verificador de NF-e - DRACMA Edition")

uploaded_file = st.file_uploader("Envie o PDF da DANFE")

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        st.text_area("Texto extraído:", text, height=300)
