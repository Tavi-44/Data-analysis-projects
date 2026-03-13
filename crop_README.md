This project aims to assist farmers and agricultural stakeholders in estimating Crop Production and Revenue based on factors like Area, Fertilizers, and Pesticides. It features a Machine Learning pipeline and an interactive dashboard for real-time predictions.

Features
Data Preprocessing: Handled skewed data using Log Transformations for better model accuracy.

Machine Learning Pipeline: Implemented and compared multiple models including Linear Regression, Random Forest, and Gradient Boosting.

Interactive Dashboard: Developed a user-friendly UI using Streamlit to allow users to input parameters and see instant predictions.

Visual Insights: Created visualizations using Plotly and Matplotlib to show feature importance and production trends.

Tech Stack
Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly

Framework: Streamlit (For Dashboard)

Project Structure
ml_pipeline.py: Script for data cleaning, model training, and evaluation.

app1.py: The main script to run the Streamlit dashboard.

crop_revenue.csv: The dataset containing agricultural records (Area, Production, Rainfall, etc.).
