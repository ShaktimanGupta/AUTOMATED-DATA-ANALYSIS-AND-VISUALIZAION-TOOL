import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------
# Page Config
# ------------------------
st.set_page_config(
    page_title="Automated CSV Data Analysis",
    layout="wide",
    page_icon="📊"
)

# ------------------------
# CSS Styling
# ------------------------
st.markdown("""
    <style>
        /* Title */
        .css-10trblm {
            color: #2C3E50;
            text-align: center;
            font-size: 38px !important;
            font-weight: bold;
        }
        /* Metric values */
        div[data-testid="stMetricValue"] {
            font-size: 26px;
            font-weight: bold;
            color: #16A085;
        }
        /* Background */
        .stApp {
            background-color: #F8F9FA;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------
# Title
# ------------------------
st.title("📊 Automated CSV Data Analysis and Visualization")
st.write("Upload a CSV file with columns: `Product`, `Category`, `Region`, `Price`, `Quantity`, `Month`")

# ------------------------
# File Upload
# ------------------------
uploaded_file = st.file_uploader("📂 Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    st.success("✅ CSV file loaded successfully!")

    # ------------------------
    # Add Total Sales
    # ------------------------
    df["Total_Sales"] = df["Price"] * df["Quantity"]

    # ------------------------
    # Summary Metrics
    # ------------------------
    st.subheader("📊 Dataset Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🧮 Rows", f"{len(df)}")
    with col2:
        st.metric("📑 Columns", f"{len(df.columns)}")
    with col3:
        st.metric("💰 Total Sales", f"{df['Total_Sales'].sum():,.2f}")

    # ------------------------
    # Sample Data
    # ------------------------
    st.subheader("📋 Sample Data")
    st.dataframe(df.head())

    # ------------------------
    # Summary Statistics
    # ------------------------
    st.subheader("📊 Summary Statistics")
    st.dataframe(df.describe())

    # ------------------------
    # Charts in Tabs
    # ------------------------
    st.subheader("📈 Data Visualizations")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["🏆 Top Products", "🥧 Category Sales", "🌍 Region Sales", "📅 Monthly Sales", "🔥 Correlation"]
    )

    # Top Products
    with tab1:
        top_products = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).head(5).reset_index()
        fig1 = px.bar(top_products, x="Product", y="Total_Sales", text="Total_Sales",
                      title="Top 5 Products by Total Sales", color="Total_Sales",
                      color_continuous_scale="Blues")
        fig1.update_traces(texttemplate='%{text:.2s}', textposition="outside")
        st.plotly_chart(fig1, use_container_width=True)

    # Category Sales
    with tab2:
        category_sales = df.groupby("Category")["Total_Sales"].sum().reset_index()
        fig2 = px.pie(category_sales, names="Category", values="Total_Sales",
                      title="Sales Distribution by Category", hole=0.4,
                      color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig2, use_container_width=True)

    # Region Sales
    with tab3:
        region_sales = df.groupby("Region")["Total_Sales"].sum().reset_index()
        fig3 = px.bar(region_sales, x="Region", y="Total_Sales", text="Total_Sales",
                      title="Sales by Region", color="Total_Sales", color_continuous_scale="Viridis")
        fig3.update_traces(texttemplate='%{text:.2s}', textposition="outside")
        st.plotly_chart(fig3, use_container_width=True)

    # Monthly Sales
    with tab4:
        month_sales = df.groupby("Month")["Total_Sales"].sum().reset_index()
        fig4 = px.line(month_sales, x="Month", y="Total_Sales", markers=True,
                       title="Sales Trend Over Months", line_shape="spline")
        st.plotly_chart(fig4, use_container_width=True)

    # Correlation Heatmap
    with tab5:
        corr = df.select_dtypes(include="number").corr()
        fig5 = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r",
                         title="Correlation Heatmap")
        st.plotly_chart(fig5, use_container_width=True)
