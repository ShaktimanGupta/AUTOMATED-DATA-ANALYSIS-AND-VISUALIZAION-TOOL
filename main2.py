import streamlit as st
import pandas as pd
import plotly.express as px
import io

# ------------------------
# Page Config
# ------------------------
st.set_page_config(
    page_title="Dynamic CSV Data Analysis",
    layout="wide",
    page_icon="📊"
)

# ------------------------
# CSS for Custom Styling
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
        /* Metric cards */
        div[data-testid="stMetricValue"] {
            font-size: 28px;
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
st.title("📊 Dynamic CSV Data Analysis & Visualization")
st.markdown("### Upload any CSV file and explore data with interactive dashboards 🚀")

# ------------------------
# File Upload
# ------------------------
uploaded_file = st.file_uploader("📂 Upload your CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # ------------------------
    # Sidebar Filters
    # ------------------------
    st.sidebar.header("🔍 Filters")
    cols = df.columns.tolist()

    product_col = st.sidebar.selectbox("Product Column", ["None"] + cols, index=0)
    category_col = st.sidebar.selectbox("Category Column", ["None"] + cols, index=0)
    region_col = st.sidebar.selectbox("Region Column", ["None"] + cols, index=0)
    price_col = st.sidebar.selectbox("Price Column", ["None"] + cols, index=0)
    quantity_col = st.sidebar.selectbox("Quantity Column", ["None"] + cols, index=0)
    month_col = st.sidebar.selectbox("Month Column", ["None"] + cols, index=0)

    # ------------------------
    # Data Preview
    # ------------------------
    st.subheader("📋 Data Preview")
    st.dataframe(df.head())

    # ------------------------
    # Add Total Sales
    # ------------------------
    if price_col != "None" and quantity_col != "None":
        df["Total_Sales"] = df[price_col] * df[quantity_col]

    # ------------------------
    # Summary Stats
    # ------------------------
    st.subheader("📊 Summary Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🧮 Rows", f"{len(df)}")
    with col2:
        st.metric("📑 Columns", f"{len(df.columns)}")
    with col3:
        if "Total_Sales" in df:
            st.metric("💰 Total Sales", f"{df['Total_Sales'].sum():,.2f}")

    st.dataframe(df.describe(include="all"))

    # ------------------------
    # Tabs for Visuals
    # ------------------------
    st.subheader("📈 Data Visualizations")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["🏆 Top Products", "🥧 Category Sales", "🌍 Region Sales", "📅 Monthly Sales", "🔥 Correlation"]
    )

    with tab1:
        if product_col != "None" and "Total_Sales" in df:
            top_products = df.groupby(product_col)["Total_Sales"].sum().sort_values(ascending=False).head()
            fig_top = px.bar(top_products, x=top_products.index, y=top_products.values, text=top_products.values,
                             labels={"x": "Product", "y": "Total Sales"}, title="Top 5 Products")
            fig_top.update_traces(textposition="outside", marker_color="#3498DB")
            st.plotly_chart(fig_top, use_container_width=True)

    with tab2:
        if category_col != "None" and "Total_Sales" in df:
            category_sales = df.groupby(category_col)["Total_Sales"].sum().reset_index()
            fig1 = px.pie(category_sales, names=category_col, values="Total_Sales",
                          title="Sales Distribution by Category", hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig1, use_container_width=True)

    with tab3:
        if region_col != "None" and "Total_Sales" in df:
            region_sales = df.groupby(region_col)["Total_Sales"].sum().reset_index()
            fig2 = px.bar(region_sales, x=region_col, y="Total_Sales", text="Total_Sales",
                          title="Sales by Region", color="Total_Sales", color_continuous_scale="Viridis")
            fig2.update_traces(texttemplate='%{text:.2s}', textposition="outside")
            st.plotly_chart(fig2, use_container_width=True)

    with tab4:
        if month_col != "None" and "Total_Sales" in df:
            month_sales = df.groupby(month_col)["Total_Sales"].sum().reset_index()
            fig3 = px.line(month_sales, x=month_col, y="Total_Sales", markers=True,
                           title="Sales Trend Over Months", line_shape="spline")
            st.plotly_chart(fig3, use_container_width=True)

    with tab5:
        corr = df.select_dtypes(include="number").corr()
        if not corr.empty:
            fig4 = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r", title="Correlation Heatmap")
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.info("No numeric columns available for correlation.")
