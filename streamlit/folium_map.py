import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as pg
import folium 
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
from folium.plugins import FastMarkerCluster
from branca.element import Template, MacroElement
import requests
import json
import altair as alt
from streamlit.components.v1 import html

@st.cache_data
def generate_map(df):
    m1 = folium.Map(location=(48.866667, -2.333333), control_scale=True, zoom_start=6)

    title_html = '''
        <h3 align="center" style="font-size:20px"><b>Carte des Nuances Politiques par Commune (crée par Tom Heising)</b></h3>
        '''
    m1.get_root().html.add_child(folium.Element(title_html))

    # Création du FeatureGroup pour les marqueurs
    #fg = folium.FeatureGroup(name="Icon collection", show=True).add_to(m)

    # Cluster des marqueurs
    marker_cluster = MarkerCluster().add_to(m1)

    # Boucle à travers les données pour ajouter des marqueurs
    for index, row in df.iterrows():
        ville = row['Libellé commune']
        if not pd.isna(row['latitude']) and not pd.isna(row['longitude']):
            location_elu = (row['latitude'], row['longitude'])
            
            # Récupérer la nuance politique des élus
            PP = row['Nuance candidat 1'] if row['Elu 1'] == 'élu' else (
                row['Nuance candidat 2'] if row['Elu 2'] == 'élu' else (
                    row['Nuance candidat 3'] if row['Elu 3'] == 'élu' else (
                        row['Nuance candidat 4'] if row['Elu 4'] == 'élu' else (
                            row['Nuance candidat 5'] if row['Elu 5'] == 'élu' else (
                                row['Nuance candidat 6'] if row['Elu 6'] == 'élu' else (
                                    row['Nuance candidat 7'] if row['Elu 7'] == 'élu' else (
                                        row['Nuance candidat 8'] if row['Elu 8'] == 'élu' else (
                                            row['Nuance candidat 9'] if row['Elu 9'] == 'élu' else (
                                                row['Nuance candidat 10'] if row['Elu 10'] == 'élu' else (
                                                    row['Nuance candidat 11'] if row['Elu 11'] == 'élu' else (
                                                        row['Nuance candidat 12'] if row['Elu 12'] == 'élu' else (
                                                            row['Nuance candidat 13'] if row['Elu 13'] == 'élu' else (
                                                                row['Nuance candidat 14'] if row['Elu 14'] == 'élu' else None
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        
            # Ajouter le marker avec un popup
            folium.Marker(
                location=location_elu,
                popup=folium.Popup(f"Nuance politique : {PP} | commune : {ville}", parse_html=True, max_width=100)
            ).add_to(marker_cluster)

    # Exemple d'un autre marqueur (Paris)
    folium.Marker(
        location=[48.866667, 2.33333],
        popup=folium.Popup("Nuance politique : ENS | commune : Paris", parse_html=True, max_width=100),
    ).add_to(marker_cluster)

    # Ajouter les contrôles de couches
    #folium.LayerControl().add_to(m)

    # Afficher la carte dans Streamlit
    #st_folium(m1, width=1200, height=800)
    return m1._repr_html_()

def show():    
    st.markdown("<h2 style='text-align: center; color: white;'>Carte des Nuances Politiques par Commune</h2>", unsafe_allow_html=True)
    temp_df = pd.read_csv('Data/final_df.csv')
    
    m1 = generate_map(temp_df)
    html(m1, width=1200, height=800)
    

    
"""def show():
    temp_df = pd.read_csv('/Users/tomheising/Desktop/Data Vizualisation Project /Data/final_df.csv')
    
    
    st.markdown("<h2 style='text-align: center; color: white;'>Carte des Nuances Politiques par Commune</h2>", unsafe_allow_html=True)
    m1 = folium.Map(location=(48.866667, -2.333333), control_scale=True, zoom_start=6)

    title_html = '''
        <h3 align="center" style="font-size:20px"><b>Carte des Nuances Politiques par Commune (crée par Tom Heising)</b></h3>
        '''
    m1.get_root().html.add_child(folium.Element(title_html))

    # Création du FeatureGroup pour les marqueurs
    #fg = folium.FeatureGroup(name="Icon collection", show=True).add_to(m)

    # Cluster des marqueurs
    marker_cluster = MarkerCluster().add_to(m1)

    # Boucle à travers les données pour ajouter des marqueurs
    for index, row in temp_df.iterrows():
        ville = row['Libellé commune']
        if not pd.isna(row['latitude']) and not pd.isna(row['longitude']):
            location_elu = (row['latitude'], row['longitude'])
            
            # Récupérer la nuance politique des élus
            PP = row['Nuance candidat 1'] if row['Elu 1'] == 'élu' else (
                row['Nuance candidat 2'] if row['Elu 2'] == 'élu' else (
                    row['Nuance candidat 3'] if row['Elu 3'] == 'élu' else (
                        row['Nuance candidat 4'] if row['Elu 4'] == 'élu' else (
                            row['Nuance candidat 5'] if row['Elu 5'] == 'élu' else (
                                row['Nuance candidat 6'] if row['Elu 6'] == 'élu' else (
                                    row['Nuance candidat 7'] if row['Elu 7'] == 'élu' else (
                                        row['Nuance candidat 8'] if row['Elu 8'] == 'élu' else (
                                            row['Nuance candidat 9'] if row['Elu 9'] == 'élu' else (
                                                row['Nuance candidat 10'] if row['Elu 10'] == 'élu' else (
                                                    row['Nuance candidat 11'] if row['Elu 11'] == 'élu' else (
                                                        row['Nuance candidat 12'] if row['Elu 12'] == 'élu' else (
                                                            row['Nuance candidat 13'] if row['Elu 13'] == 'élu' else (
                                                                row['Nuance candidat 14'] if row['Elu 14'] == 'élu' else None
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        
            # Ajouter le marker avec un popup
            folium.Marker(
                location=location_elu,
                popup=folium.Popup(f"Nuance politique : {PP} | commune : {ville}", parse_html=True, max_width=100)
            ).add_to(marker_cluster)

    # Exemple d'un autre marqueur (Paris)
    folium.Marker(
        location=[48.866667, 2.33333],
        popup=folium.Popup("Nuance politique : ENS | commune : Paris", parse_html=True, max_width=100),
    ).add_to(marker_cluster)

    # Ajouter les contrôles de couches
    #folium.LayerControl().add_to(m)

    # Afficher la carte dans Streamlit
    st_folium(m1, width=1200, height=800)"""
