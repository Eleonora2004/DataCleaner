import streamlit as st
import pandas as pd
from src.cleaner import DataCleaner

st.title("🧼 Data Cleaner App")

uploaded_file = st.file_uploader("Upload a CSV file to clean", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Original Data")
    st.write(df)

    cleaner = DataCleaner(df)

    fill_method = st.selectbox("Fill missing values using:", ["mean", "median", "drop"])
    drop_duplicates = st.checkbox("Drop duplicate rows", value=True)
    encode_categorical = st.checkbox("Encode categorical variables", value=True)

    df_cleaned = cleaner.clean(
        fill_missing=fill_method,
        drop_duplicates=drop_duplicates,
        encode_categorical=encode_categorical
    )

    st.subheader("Cleaned Data")
    st.write(df_cleaned)

    csv = df_cleaned.to_csv(index=False).encode("utf-8")
    st.download_button("Download Cleaned CSV", csv, "cleaned_data.csv", "text/csv")
