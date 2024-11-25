import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as pg
import folium 
from folium.plugins import MarkerCluster
from branca.element import Template, MacroElement
import requests
import json
import altair as alt
import ipywidgets as widgets
from IPython.display import display, clear_output
import analyse
import about_me
import folium_map

st.markdown("""
    <style>
    /* Fond et police générale */
    .stApp {
        background: linear-gradient(to bottom, #2c3e50, #000000); /* Dégradé de bleu nuit à noir */
        color: #ffffff;
        font-family: 'Helvetica', sans-serif;
    }
    
    /* Titre principal */
    h1 {
        font-size: 3em;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 0.5em;
    }
    
    /* Sous-titres */
    h2 {
        font-size: 2em;
        color: #FFFFFF;
        margin-bottom: 20px;
    }
    
    h3{
        color: #000000;
    }
    
    /* Titre de la sidebar */
    .sidebar .sidebar-content {
        background-color: #222831; /* Changement pour un noir plus élégant */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    .sidebar .sidebar-content h1 {
        color: #ffffff;
        font-size: 1.8em;
        text-align: center;
        margin-bottom: 1em;
    }
    
    /* Style pour les boutons et les options */
    .css-1d391kg, .stSelectbox select {
        background-color: #393e46;
        border: 1px solid #00adb5;
        border-radius: 8px;
        padding: 10px;
        transition: all 0.3s ease-in-out;
        color: #eeeeee;
    }
    
    .css-1d391kg:hover, .stSelectbox:hover select {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* Espacement des containers de graphiques */
    .block-container {
        padding: 2rem 5rem;
    }
    
    /* Style pour les colonnes */
    .stColumn {
        margin-bottom: 2em;
    }
    
    /* Centrage et effet du footer */
    footer {
        text-align: center;
        padding: 10px;
        font-size: 0.8em;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# Titre principal
st.markdown("<h1>Welcome to my Portfolio &#128161;</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title('Menu')
st.sidebar.markdown("""
    <p style='font-size: 1.2em; color: #ccc;'>Sélectionnez une option ci-dessous</p>
""", unsafe_allow_html=True)

# Sélection des pages
page_selection = st.sidebar.selectbox('Choisissez une option', ['About me', 'Analyse Élections législatives 2024', 'Cartes folium'])

# Affichage de la sélection
st.markdown(f"<h2>Vous avez sélectionné : {page_selection}</h2>", unsafe_allow_html=True)

# Couleur de fond spécifique et espacement
page_bg_color = """
    <style>
    .stApp {
        background-color: #ffffff; /* Fond clair */
        color: #333; /* Texte sombre */
        padding: 20px;
    }
    </style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Gestion des pages
if page_selection == 'About me':
    about_me.show()
elif page_selection == 'Analyse Élections législatives 2024':
    analyse.show()
elif page_selection == 'Cartes folium':
    folium_map.show()
    

# Footer
st.markdown("""
    <footer>
        © 2024 - Créé par Tom Heising | Inspiré par la passion et la détermination
    </footer>
""", unsafe_allow_html=True)

    
    




