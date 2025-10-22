import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="🚀",
    layout="wide"
)

# Title and description
st.title("🚀 Welcome to Streamlit!")
st.markdown("This is a sample app demonstrating various Streamlit features.")

# Sidebar
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Enter your name:", "User")
st.sidebar.write(f"Hello, {user_name}!")

# Tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["📊 Data & Charts", "🎨 Widgets", "📝 Text Elements", "📁 File Upload"])

# Tab 1: Data and Charts
with tab1:
    st.header("Data Visualization")
    
    # Generate sample data
    df = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': np.random.randint(100, 500, 6),
        'Expenses': np.random.randint(50, 300, 6)
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sample Data")
        st.dataframe(df, use_container_width=True)
        
    with col2:
        st.subheader("Line Chart")
        st.line_chart(df.set_index('Month'))
    
    # Interactive Plotly chart
    st.subheader("Interactive Bar Chart")
    fig = px.bar(df, x='Month', y=['Sales', 'Expenses'], barmode='group')
    st.plotly_chart(fig, use_container_width=True)

# Tab 2: Widgets
with tab2:
    st.header("Interactive Widgets")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Slider
        age = st.slider("Select your age:", 0, 100, 25)
        st.write(f"You selected: {age}")
        
        # Select box
        option = st.selectbox(
            "Choose your favorite color:",
            ["Red", "Green", "Blue", "Yellow"]
        )
        st.write(f"Your favorite color is: {option}")
        
        # Checkbox
        agree = st.checkbox("I agree to the terms")
        if agree:
            st.success("Thank you for agreeing!")
    
    with col2:
        # Radio buttons
        genre = st.radio(
            "Select your favorite genre:",
            ["Comedy", "Drama", "Action", "Sci-Fi"]
        )
        st.write(f"You selected: {genre}")
        
        # Date input
        date = st.date_input("Select a date:")
        st.write(f"Selected date: {date}")
        
        # Number input
        number = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
        st.write(f"You entered: {number}")

# Tab 3: Text Elements
with tab3:
    st.header("Text and Formatting")
    
    st.subheader("This is a subheader")
    st.write("This is regular text using st.write()")
    st.markdown("**Bold text** and *italic text* with markdown")
    st.code("print('Hello, Streamlit!')", language="python")
    
    st.info("This is an info message")
    st.success("This is a success message")
    st.warning("This is a warning message")
    st.error("This is an error message")

# Tab 4: File Upload
with tab4:
    st.header("File Upload Example")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df_uploaded = pd.read_csv(uploaded_file)
        st.write("File uploaded successfully!")
        st.dataframe(df_uploaded.head(), use_container_width=True)
        st.write(f"Shape: {df_uploaded.shape[0]} rows, {df_uploaded.shape[1]} columns")

# Footer
st.divider()
st.caption("Built with Streamlit 🎈")
