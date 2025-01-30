import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset directly within the app
def load_data():
    return pd.read_csv("HR-Employee-Attrition.csv")  # Ensure this file is in the app directory

# Navigation state
if "page" not in st.session_state:
    st.session_state.page = "intro"

def go_to_analysis():
    st.session_state.page = "analysis"

if st.session_state.page == "intro":
    # Introductory Page
    st.title("HR Employee Attrition Analysis")
    st.write("This app provides insights into employee attrition trends using HR data.")
    st.write("Click below to start the analysis.")
    st.button("Run Analysis", on_click=go_to_analysis)
else:
    # Load dataset
    df = load_data()
    
    st.title("HR Employee Attrition Analysis")
    
    # Show dataset preview
    st.subheader("Dataset Preview")
    st.write(df.head())
    
    # Basic dataset information
    st.subheader("Dataset Information")
    st.write(df.describe())
    
    # Visualization: Attrition Count
    st.subheader("Attrition Count")
    fig, ax = plt.subplots()
    sns.countplot(x='Attrition', data=df, ax=ax)
    st.pyplot(fig)
    
    # Visualization: Age Distribution
    st.subheader("Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['Age'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)
    
    # Visualization: Monthly Income Distribution
    st.subheader("Monthly Income Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['MonthlyIncome'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)
    
    # Visualization: Job Role Count
    st.subheader("Job Role Count")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(y='JobRole', data=df, order=df['JobRole'].value_counts().index, ax=ax)
    st.pyplot(fig)
    
    # Visualization: Education Field Count
    st.subheader("Education Field Count")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(y='EducationField', data=df, order=df['EducationField'].value_counts().index, ax=ax)
    st.pyplot(fig)
    
    # Visualization: Years at Company Distribution
    st.subheader("Years at Company Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['YearsAtCompany'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)
    
    # Visualization: Gender Distribution
    st.subheader("Gender Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x='Gender', data=df, ax=ax)
    st.pyplot(fig)
    
    # Visualization: Department Breakdown
    st.subheader("Department Breakdown")
    fig, ax = plt.subplots()
    sns.countplot(x='Department', data=df, ax=ax)
    st.pyplot(fig)
    
    # Visualization: Work-Life Balance Rating
    st.subheader("Work-Life Balance Rating")
    fig, ax = plt.subplots()
    sns.countplot(x='WorkLifeBalance', data=df, ax=ax)
    st.pyplot(fig)
    