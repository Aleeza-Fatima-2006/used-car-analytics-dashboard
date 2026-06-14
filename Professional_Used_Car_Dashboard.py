import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    # Replace with your actual CSV file name
    df = pd.read_csv("used_cars.csv")
    return df

def main():
    st.title("🚗 Professional Used Car Dashboard")

    try:
        df = load_data()
    except Exception as e:
        st.error("Dataset not found or error loading CSV.")
        st.info("Make sure your CSV file is named 'used_cars.csv'")
        return

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    if "company" in df.columns:
        st.subheader("Cars by Company")
        company_counts = df['company'].value_counts()

        fig, ax = plt.subplots()
        ax.pie(company_counts, labels=company_counts.index, autopct='%1.1f%%')
        ax.axis("equal")
        st.pyplot(fig)

    if "price" in df.columns:
        st.subheader("Price Distribution")
        fig, ax = plt.subplots()
        ax.hist(df['price'].dropna(), bins=20)
        st.pyplot(fig)
