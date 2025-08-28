import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Disease Trend Visualizer", page_icon="🌍", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_excel("disease_outbreaks_HDX.xlsx", sheet_name="Data")
    return df

data = load_data()

# Sidebar
st.sidebar.title("📊 Disease Trend Visualizer")
page = st.sidebar.radio("Go to", ["Home", "Year-wise Trends", "Country-wise Trends"])

# HOME PAGE
# HOME PAGE
# HOME PAGE
if page == "Home":
    st.title("🌍 Disease Trend Visualizer")
    st.markdown(
        """
        Welcome! This app helps you *v  isualize global disease outbreak trends*.
        Explore the data by *Year-wise* or *Country-wise* analysis using the sidebar.
        """
    )

    st.image(
    "https://images.unsplash.com/photo-1584036561566-baf8f5f1b144?auto=format&fit=crop&w=1050&q=80",
    use_container_width=True,
    caption="Global Disease Outbreaks"
)


    st.markdown("### 🔹 Key Highlights")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Outbreaks", f"{data['id_outbreak'].nunique()}")
    col2.metric("Total Diseases", f"{data['Disease'].nunique()}")
    col3.metric("Total Countries", f"{data['Country'].nunique()}")

    st.markdown("---")
    st.subheader("📊 Sample Data Preview")
    st.dataframe(data.head(10))

    st.markdown(
        """
        💡 *Tip:* Use the sidebar to navigate between *Year-wise Trends* and *Country-wise Trends*.
        You can filter by disease and see trends over time or across countries.
        """
    )
# YEAR-WISE TRENDS
elif page == "Year-wise Trends":
    st.title("📈 Year-wise Disease Trends")

    # Dropdown for disease filter
    disease_list = ["All"] + sorted(data["Disease"].dropna().unique().tolist())
    selected_disease = st.selectbox("Select Disease", disease_list)

    df_year = data.copy()
    if selected_disease != "All":
        df_year = df_year[df_year["Disease"] == selected_disease]

    year_counts = df_year.groupby("Year")["id_outbreak"].count()

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    year_counts.plot(kind="bar", ax=ax)
    ax.set_ylabel("Number of Outbreaks")
    ax.set_title(f"Outbreaks per Year ({selected_disease})")
    st.pyplot(fig)

# COUNTRY-WISE TRENDS
elif page == "Country-wise Trends":
    st.title("🌍 Country-wise Disease Trends")

    # Dropdown for disease filter
    disease_list = ["All"] + sorted(data["Disease"].dropna().unique().tolist())
    selected_disease = st.selectbox("Select Disease", disease_list, key="country")

    df_country = data.copy()
    if selected_disease != "All":
        df_country = df_country[df_country["Disease"] == selected_disease]

    country_counts = df_country["Country"].value_counts().head(15)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    country_counts.plot(kind="barh", ax=ax)
    ax.set_xlabel("Number of Outbreaks")
    ax.set_ylabel("Country")
    ax.set_title(f"Top 15 Countries with Outbreaks ({selected_disease})")
    st.pyplot(fig)