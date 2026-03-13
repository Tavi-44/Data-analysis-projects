import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import cufflinks as cf

net = pd.read_csv('net.csv.csv')
pd.set_option('display.max_columns', None)
(pd.isna(net))
net['director'] = net['director'].fillna('unknown')
net['cast'] = net['cast'].fillna('unknown')
net['country'] = net['country'].fillna('unknown')
net['description'] = net['description'].fillna('unknown')
net['listed_in'] = net['listed_in'].fillna('unknown')
(net.drop_duplicates)
#print(net.head(10))
type_count =(net.value_counts(net['type']))
pie = px.pie(
    names = type_count.index,
    values= type_count.values,
    title= "Movies vs TV Shows on Netflix",
    color_discrete_sequence=px.colors.sequential.RdBu
)
#pie.show()

country_counts = net['country'].value_counts().head(10)

country_counts = net['country'].value_counts().head(10)

bar = px.bar(
    x=country_counts.index, 
    y=country_counts.values,
    title="Top 10 Countries with Most Content",
    labels={'x': 'Country', 'y': 'Number of Titles'},
    color=country_counts.values,          
    color_continuous_scale='Rainbow'   
)
bar.show()


hist = px.histogram(
    net,
    x="release_year",
    nbins=30,
    title="Distribution of Netflix Content by Release Year",
    color_discrete_sequence=px.colors.sequential.Rainbow
)

#hist.show()

