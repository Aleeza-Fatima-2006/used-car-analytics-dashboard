import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("used_cars.csv")
    return df

def main():
    st.set_page_config(page_title="Used Car Dashboard", layout="wide")

    st.title("🚗 Professional Used Car Dashboard")

    try:
        df = load_data()
    except Exception:
        st.error("❌ Dataset not found or cannot be loaded.")
        st.info("Make sure your file is named: used_cars.csv")
        return

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    # Company chart
    if "company" in df.columns:
        st.subheader("🏭 Cars by Company")

        company_counts = df["company"].value_counts()

        fig, ax = plt.subplots()
        ax.pie(company_counts, labels=company_counts.index, autopct="%1.1f%%")
        ax.axis("equal")

        st.pyplot(fig)

    # Price chart
    if "price" in df.columns:
        st.subheader("💰 Price Distribution")

        fig, ax = plt.subplots()
        ax.hist(df["price"].dropna(), bins=20)

        st.pyplot(fig)


# IMPORTANT: Streamlit entry point
if __name__ == "__main__":
    main()
