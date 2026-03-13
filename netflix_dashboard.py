import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
import cufflinks as cf
from netflix_analysis import pie,hist,bar
st.title("Netflix Data Analysis Dashboard")
page = st.sidebar.radio(
    "Navigation",
    ['About Project','Graphs']
)

if page == 'About Project':
    st.title("About Project")
    st.subheader("Project Overview:")
    st.write("""This project focuses on analyzing the Netflix dataset (net.csv) to uncover trends and patterns in the content available on the platform. By utilizing Python and its data science libraries, I processed the raw data to extract meaningful insights regarding content types, global production, and genre distribution.

What I Did (Technical Workflow):

Data Preprocessing & Cleaning:

Handling Missing Values: I identified and filled missing data in critical columns like director, cast, country, and description using a placeholder ('unknown') to ensure the integrity of the analysis.

Data Integrity: I implemented logic to check for and remove duplicate records, ensuring the visualizations were based on unique entries.

Exploratory Data Analysis (EDA):

Content Distribution: I analyzed the ratio between Movies and TV Shows to understand Netflix’s library focus.

Geographic Trends: I identified the top 10 countries responsible for producing the most content on the platform.

Data Visualization:

Interactive Charts: Using Plotly Express, I created interactive Pie charts and Bar graphs to make the data more readable and engaging.

Web Integration: I utilized the Streamlit framework to build a user-friendly interface for displaying these insights.

Tech Stack Used:

Language: Python

Libraries: Pandas, NumPy (Data Manipulation), Plotly, Matplotlib, Seaborn (Visualization)

Deployment/UI: Streamlit

Key Insights:

A clear visual breakdown of Movies vs. TV Shows.

Identification of the United States and India as leading content producers.

A clean, interactive dashboard to explore Netflix's global content footprint.""")
    
elif page == 'Graphs':
    st.plotly_chart(pie)
    st.write("Most of the Netflix content consists of movies compared to TV shows.")
    st.plotly_chart(hist)
    st.write("Most Netflix content was released after 2015 showing rapid platform growth.")
    st.plotly_chart(bar)

    st.write("The United States produces the highest amount of Netflix content.")

