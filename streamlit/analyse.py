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
from branca.element import Template, MacroElement
import requests
import json
import altair as alt

st.set_page_config(page_title='Analyse Élections législatives 2024', page_icon='📊', layout='wide', initial_sidebar_state='auto')
def show():
    temp_df = pd.read_csv('/Users/tomheising/Desktop/Data Vizualisation Project /Data/final_df.csv')

    ENScpt = DSVcpt = DVCcpt = DVGcpt = DVDcpt = FIcpt = HORcpt = 0
    LRcpt = REGcpt = RNcpt = SOCcpt = UDIcpt = UGcpt = UXDcpt = 0

    for index, row in temp_df.iterrows():
        if row['Elu 1'] == 'élu':
            nuance1 = row['Nuance candidat 1']
            if nuance1 == 'ENS':
                ENScpt += 1
            elif nuance1 == 'DSV':
                DSVcpt += 1
            elif nuance1 == 'DVC':
                DVCcpt += 1
            elif nuance1 == 'DVG':
                DVGcpt += 1
            elif nuance1 == 'DVD':
                DVDcpt += 1
            elif nuance1 == 'FI':
                FIcpt += 1
            elif nuance1 == 'HOR':
                HORcpt += 1
            elif nuance1 == 'LR':
                LRcpt += 1
            elif nuance1 == 'REG':
                REGcpt += 1
            elif nuance1 == 'RN':
                RNcpt += 1
            elif nuance1 == 'SOC':
                SOCcpt += 1
            elif nuance1 == 'UDI':
                UDIcpt += 1
            elif nuance1 == 'UG':
                UGcpt += 1
            elif nuance1 == 'UXD':
                UXDcpt += 1
                    
        elif row['Elu 2'] == 'élu':
            nuance2 = row['Nuance candidat 2']
            if nuance2 == 'ENS':
                ENScpt += 1
            elif nuance2 == 'DSV':
                DSVcpt += 1
            elif nuance2 == 'DVC':
                DVCcpt += 1
            elif nuance2 == 'DVG':
                DVGcpt += 1
            elif nuance2 == 'DVD':
                DVDcpt += 1
            elif nuance2 == 'FI':
                FIcpt += 1
            elif nuance2 == 'HOR':
                HORcpt += 1
            elif nuance2 == 'LR':
                LRcpt += 1
            elif nuance2 == 'REG':
                REGcpt += 1
            elif nuance2 == 'RN':
                RNcpt += 1
            elif nuance2 == 'SOC':
                SOCcpt += 1
            elif nuance2 == 'UDI':
                UDIcpt += 1
            elif nuance2 == 'UG':
                UGcpt += 1
            elif nuance2 == 'UXD':
                UXDcpt += 1
                    
        elif row['Elu 3'] == 'élu':
            nuance3 = row['Nuance candidat 3']
            if nuance3 == 'ENS':
                ENScpt += 1
            elif nuance3 == 'DSV':
                DSVcpt += 1
            elif nuance3 == 'DVC':
                DVCcpt += 1
            elif nuance3 == 'DVG':
                DVGcpt += 1
            elif nuance3 == 'DVD':
                DVDcpt += 1
            elif nuance3 == 'FI':
                FIcpt += 1
            elif nuance3 == 'HOR':
                HORcpt += 1
            elif nuance3 == 'LR':
                LRcpt += 1
            elif nuance3 == 'REG':
                REGcpt += 1
            elif nuance3 == 'RN':
                RNcpt += 1
            elif nuance3 == 'SOC':
                SOCcpt += 1
            elif nuance3 == 'UDI':
                UDIcpt += 1
            elif nuance3 == 'UG':
                UGcpt += 1
            elif nuance3 == 'UXD':
                UXDcpt += 1

        elif row['Elu 4'] == 'élu':
            nuance4 = row['Nuance candidat 4']
            if nuance4 == 'ENS':
                ENScpt += 1
            elif nuance4 == 'DSV':
                DSVcpt += 1
            elif nuance4 == 'DVC':
                DVCcpt += 1
            elif nuance4 == 'DVG':
                DVGcpt += 1
            elif nuance4 == 'DVD':
                DVDcpt += 1
            elif nuance4 == 'FI':
                FIcpt += 1
            elif nuance4 == 'HOR':
                HORcpt += 1
            elif nuance4 == 'LR':
                LRcpt += 1
            elif nuance4 == 'REG':
                REGcpt += 1
            elif nuance4 == 'RN':
                RNcpt += 1
            elif nuance4 == 'SOC':
                SOCcpt += 1
            elif nuance4 == 'UDI':
                UDIcpt += 1
            elif nuance4 == 'UG':
                UGcpt += 1
            elif nuance4 == 'UXD':
                UXDcpt += 1

        elif row['Elu 5'] == 'élu':
            nuance5 = row['Nuance candidat 5']
            if nuance5 == 'ENS':
                ENScpt += 1
            elif nuance5 == 'DSV':
                DSVcpt += 1
            elif nuance5 == 'DVC':
                DVCcpt += 1
            elif nuance5 == 'DVG':
                DVGcpt += 1
            elif nuance5 == 'DVD':
                DVDcpt += 1
            elif nuance5 == 'FI':
                FIcpt += 1
            elif nuance5 == 'HOR':
                HORcpt += 1
            elif nuance5 == 'LR':
                LRcpt += 1
            elif nuance5 == 'REG':
                REGcpt += 1
            elif nuance5 == 'RN':
                RNcpt += 1
            elif nuance5 == 'SOC':
                SOCcpt += 1
            elif nuance5 == 'UDI':
                UDIcpt += 1
            elif nuance5 == 'UG':
                UGcpt += 1
            elif nuance5 == 'UXD':
                UXDcpt += 1
                
        elif row['Elu 6'] ==' élu':
            nuance6 = row['Nuance candidat 6']
            if nuance6 == 'ENS':
                ENScpt += 1
            elif nuance6 == 'DSV':
                DSVcpt += 1
            elif nuance6 == 'DVC':
                DVCcpt += 1
            elif nuance6 == 'DVG':
                DVGcpt += 1
            elif nuance6 == 'DVD':
                DVDcpt += 1
            elif nuance6 == 'FI':
                FIcpt += 1
            elif nuance6 == 'HOR':
                HORcpt += 1
            elif nuance6 == 'LR':
                LRcpt += 1
            elif nuance6 == 'REG':
                REGcpt += 1
            elif nuance6 == 'RN':
                RNcpt += 1
            elif nuance6 == 'SOC':
                SOCcpt += 1
            elif nuance6 == 'UDI':
                UDIcpt += 1
            elif nuance6 == 'UG':
                UGcpt += 1
            elif nuance6 == 'UXD':
                UXDcpt += 1

        elif row['Elu 7'] == 'élu':
            nuance7 = row['Nuance candidat 7']
            if nuance7 == 'ENS':
                ENScpt += 1
            elif nuance7 == 'DSV':
                DSVcpt += 1
            elif nuance7 == 'DVC':
                DVCcpt += 1
            elif nuance7 == 'DVG':
                DVGcpt += 1
            elif nuance7 == 'DVD':
                DVDcpt += 1
            elif nuance7 == 'FI':
                FIcpt += 1
            elif nuance7 == 'HOR':
                HORcpt += 1
            elif nuance7 == 'LR':
                LRcpt += 1
            elif nuance7 == 'REG':
                REGcpt += 1
            elif nuance7 == 'RN':
                RNcpt += 1
            elif nuance7 == 'SOC':
                SOCcpt += 1
            elif nuance7 == 'UDI':
                UDIcpt += 1
            elif nuance7 == 'UG':
                UGcpt += 1
            elif nuance7 == 'UXD':
                UXDcpt += 1
                
        elif row['Elu 8'] == 'élu':
            nuance8 = row['Nuance candidat 8']
            if nuance8 == 'ENS':
                ENScpt += 1
            elif nuance8 == 'DSV':
                DSVcpt += 1
            elif nuance8 == 'DVC':
                DVCcpt += 1
            elif nuance8 == 'DVG':
                DVGcpt += 1
            elif nuance8 == 'DVD':
                DVDcpt += 1
            elif nuance8 == 'FI':
                FIcpt += 1
            elif nuance8 == 'HOR':
                HORcpt += 1
            elif nuance8 == 'LR':
                LRcpt += 1
            elif nuance8 == 'REG':
                REGcpt += 1
            elif nuance8 == 'RN':
                RNcpt += 1
            elif nuance8 == 'SOC':
                SOCcpt += 1
            elif nuance8 == 'UDI':
                UDIcpt += 1
            elif nuance8 == 'UG':
                UGcpt += 1
            elif nuance8 == 'UXD':
                UXDcpt += 1

        elif row['Elu 9'] == 'élu':
            nuance9 = row['Nuance candidat 9']
            if nuance9 == 'ENS':
                ENScpt += 1
            elif nuance9 == 'DSV':
                DSVcpt += 1
            elif nuance9 == 'DVC':
                DVCcpt += 1
            elif nuance9 == 'DVG':
                DVGcpt += 1
            elif nuance9 == 'DVD':
                DVDcpt += 1
            elif nuance9 == 'FI':
                FIcpt += 1
            elif nuance9 == 'HOR':
                HORcpt += 1
            elif nuance9 == 'LR':
                LRcpt += 1
            elif nuance9 == 'REG':
                REGcpt += 1
            elif nuance9 == 'RN':
                RNcpt += 1
            elif nuance9 == 'SOC':
                SOCcpt += 1
            elif nuance9 == 'UDI':
                UDIcpt += 1
            elif nuance9 == 'UG':
                UGcpt += 1
            elif nuance9 == 'UXD':
                UXDcpt += 1
            
        elif row['Elu 10'] == 'élu':
            nuance10 = row['Nuance candidat 10']
            if nuance10 == 'ENS':
                ENScpt += 1
            elif nuance10 == 'DSV':
                DSVcpt += 1
            elif nuance10 == 'DVC':
                DVCcpt += 1
            elif nuance10 == 'DVG':
                DVGcpt += 1
            elif nuance10 == 'DVD':
                DVDcpt += 1
            elif nuance10 == 'FI':
                FIcpt += 1
            elif nuance10 == 'HOR':
                HORcpt += 1
            elif nuance10 == 'LR':
                LRcpt += 1
            elif nuance10 == 'REG':
                REGcpt += 1
            elif nuance10 == 'RN':
                RNcpt += 1
            elif nuance10 == 'SOC':
                SOCcpt += 1
            elif nuance10 == 'UDI':
                UDIcpt += 1
            elif nuance10 == 'UG':
                UGcpt += 1
            elif nuance10 == 'UXD':
                UXDcpt += 1

        elif row['Elu 11'] == 'élu':
            nuance11 = row['Nuance candidat 11']
            if nuance11 == 'ENS':
                ENScpt += 1
            elif nuance11 == 'DSV':
                DSVcpt += 1
            elif nuance11 == 'DVC':
                DVCcpt += 1
            elif nuance11 == 'DVG':
                DVGcpt += 1
            elif nuance11 == 'DVD':
                DVDcpt += 1
            elif nuance11 == 'FI':
                FIcpt += 1
            elif nuance11 == 'HOR':
                HORcpt += 1
            elif nuance11 == 'LR':
                LRcpt += 1
            elif nuance11 == 'REG':
                REGcpt += 1
            elif nuance11 == 'RN':
                RNcpt += 1
            elif nuance11 == 'SOC':
                SOCcpt += 1
            elif nuance11== 'UDI':
                UDIcpt += 1
            elif nuance11 == 'UG':
                UGcpt += 1
            elif nuance11 == 'UXD':
                UXDcpt += 1

        elif row['Elu 12'] == 'élu':
            nuance12 = row['Nuance candidat 12']
            if nuance12 == 'ENS':
                ENScpt += 1
            elif nuance12 == 'DSV':
                DSVcpt += 1
            elif nuance12 == 'DVC':
                DVCcpt += 1
            elif nuance12 == 'DVG':
                DVGcpt += 1
            elif nuance12 == 'DVD':
                DVDcpt += 1
            elif nuance12 == 'FI':
                FIcpt += 1
            elif nuance12 == 'HOR':
                HORcpt += 1
            elif nuance12 == 'LR':
                LRcpt += 1
            elif nuance12 == 'REG':
                REGcpt += 1
            elif nuance12 == 'RN':
                RNcpt += 1
            elif nuance12 == 'SOC':
                SOCcpt += 1
            elif nuance12 == 'UDI':
                UDIcpt += 1
            elif nuance12 == 'UG':
                UGcpt += 1
            elif nuance12 == 'UXD':
                UXDcpt += 1

        elif row['Elu 13'] == 'élu':
            nuance13 = row['Nuance candidat 13']
            if nuance13 == 'ENS':
                ENScpt += 1
            elif nuance13 == 'DSV':
                DSVcpt += 1
            elif nuance13 == 'DVC':
                DVCcpt += 1
            elif nuance13 == 'DVG':
                DVGcpt += 1
            elif nuance13 == 'DVD':
                DVDcpt += 1
            elif nuance13 == 'FI':
                FIcpt += 1
            elif nuance13 == 'HOR':
                HORcpt += 1
            elif nuance13 == 'LR':
                LRcpt += 1
            elif nuance13 == 'REG':
                REGcpt += 1
            elif nuance13 == 'RN':
                RNcpt += 1
            elif nuance13 == 'SOC':
                SOCcpt += 1
            elif nuance13 == 'UDI':
                UDIcpt += 1
            elif nuance13 == 'UG':
                UGcpt += 1
            elif nuance13 == 'UXD':
                UXDcpt += 1
                
        elif row['Elu 14'] == 'élu':
            nuance14 = row['Nuance candidat 14']
            if  nuance14 == 'ENS':
                ENScpt += 1
            elif  nuance14 == 'DSV':
                DSVcpt += 1
            elif  nuance14 == 'DVC':
                DVCcpt += 1
            elif  nuance14 == 'DVG':
                DVGcpt += 1
            elif  nuance14 == 'DVD':
                DVDcpt += 1
            elif nuance14 == 'FI':
                FIcpt += 1
            elif nuance14 == 'HOR':
                HORcpt += 1
            elif nuance14 == 'LR':
                LRcpt += 1
            elif nuance14 == 'REG':
                REGcpt += 1
            elif nuance14 == 'RN':
                RNcpt += 1
            elif nuance14 == 'SOC':
                SOCcpt += 1
            elif nuance14 == 'UDI':
                UDIcpt += 1
            elif nuance14 == 'UG':
                UGcpt += 1
            elif nuance14 == 'UXD':
                UXDcpt += 1
    
    male_count = (
    temp_df[temp_df['Sexe candidat 1'] == 'MASCULIN']['Elu 1'].count() +
    temp_df[temp_df['Sexe candidat 2'] == 'MASCULIN']['Elu 2'].count() +
    temp_df[temp_df['Sexe candidat 3'] == 'MASCULIN']['Elu 3'].count() +
    temp_df[temp_df['Sexe candidat 4'] == 'MASCULIN']['Elu 4'].count() +
    temp_df[temp_df['Sexe candidat 5'] == 'MASCULIN']['Elu 5'].count() +
    temp_df[temp_df['Sexe candidat 6'] == 'MASCULIN']['Elu 6'].count() +
    temp_df[temp_df['Sexe candidat 7'] == 'MASCULIN']['Elu 7'].count() +
    temp_df[temp_df['Sexe candidat 8'] == 'MASCULIN']['Elu 8'].count() +
    temp_df[temp_df['Sexe candidat 9'] == 'MASCULIN']['Elu 9'].count() +
    temp_df[temp_df['Sexe candidat 10'] == 'MASCULIN']['Elu 10'].count() +
    temp_df[temp_df['Sexe candidat 11'] == 'MASCULIN']['Elu 11'].count() +
    temp_df[temp_df['Sexe candidat 12'] == 'MASCULIN']['Elu 12'].count() +
    temp_df[temp_df['Sexe candidat 13'] == 'MASCULIN']['Elu 13'].count() +
    temp_df[temp_df['Sexe candidat 14'] == 'MASCULIN']['Elu 14'].count()
    )   

    female_count = (
    temp_df[temp_df['Sexe candidat 1'] == 'FEMININ']['Elu 1'].count() +
    temp_df[temp_df['Sexe candidat 2'] == 'FEMININ']['Elu 2'].count() +
    temp_df[temp_df['Sexe candidat 3'] == 'FEMININ']['Elu 3'].count() +
    temp_df[temp_df['Sexe candidat 4'] == 'FEMININ']['Elu 4'].count() +
    temp_df[temp_df['Sexe candidat 5'] == 'FEMININ']['Elu 5'].count() +
    temp_df[temp_df['Sexe candidat 6'] == 'FEMININ']['Elu 6'].count() +
    temp_df[temp_df['Sexe candidat 7'] == 'FEMININ']['Elu 7'].count() +
    temp_df[temp_df['Sexe candidat 8'] == 'FEMININ']['Elu 8'].count() +
    temp_df[temp_df['Sexe candidat 9'] == 'FEMININ']['Elu 9'].count() +
    temp_df[temp_df['Sexe candidat 10'] == 'FEMININ']['Elu 10'].count() +
    temp_df[temp_df['Sexe candidat 11'] == 'FEMININ']['Elu 11'].count() +
    temp_df[temp_df['Sexe candidat 12'] == 'FEMININ']['Elu 12'].count() +
    temp_df[temp_df['Sexe candidat 13'] == 'FEMININ']['Elu 13'].count() +
    temp_df[temp_df['Sexe candidat 14'] == 'FEMININ']['Elu 14'].count()
    )
    
    parties = ['ENS', 'DSV', 'DVC', 'DVG', 'DVD', 'FI', 'HOR', 'LR', 'REG', 'RN', 'SOC', 'UDI', 'UG', 'UXD']
    counts = [ENScpt, DSVcpt, DVCcpt, DVGcpt, DVDcpt, FIcpt, HORcpt, LRcpt, REGcpt, RNcpt, SOCcpt, UDIcpt, UGcpt, UXDcpt]

    
    data = pd.DataFrame({
    'Parties': parties,
    'Counts': counts
    })
    
    df = pd.DataFrame({
    'Sexe': ['Masculin', 'Féminin'],
    'Nombre': [male_count,female_count]
    })
    st.markdown("<h1 style='color: white;'>Introduction</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: white;'>Le dataset des résultats du second tour des élections législatives 2024 par commune contient des informations détaillées sur le scrutin à l’échelle des communes françaises. Ce dataset inclut notamment les résultats des différents candidats, classés par parti politique, ainsi que des statistiques telles que les taux de participation, les pourcentages d’abstention et les votes blancs ou nuls. En analysant ces données, il est possible de dresser un portrait détaillé des préférences électorales des citoyens à l’échelle locale, de comprendre la dynamique des résultats, et d’étudier les tendances politiques régionales ou nationales.</p>", unsafe_allow_html=True)
   
    st.markdown("<h2 style='color: white;'>Répartition des candidats par sexe et par parti</h2>", unsafe_allow_html=True)
    # Function to generate the histogram for a given candidate number
    def generate_histogram(candidate_number):
        # Générer et retourner le graphique sans l'afficher directement
        fig = px.histogram(
            temp_df, 
            x=f'Sexe candidat {candidate_number}', 
            color=f'Nuance candidat {candidate_number}', 
            title=f'Répartition des candidats {candidate_number} par sexe et par parti',
            height=600
        )
        return fig

    # Créer un menu déroulant pour sélectionner le candidat
    candidate_number = st.selectbox(
        'Sélectionner un candidat',
        options=[None] + [i for i in range(1, 15)],  # Supposons qu'il y ait 14 candidats
        format_func=lambda x: 'Sélectionner un candidat' if x is None else f'Candidat {x}'
    )

    # Création de deux colonnes pour afficher les graphiques côte à côte
    col3, col4 = st.columns(2)


    with col4:
        if candidate_number is not None:
            fig_histogram = generate_histogram(candidate_number)
            st.plotly_chart(fig_histogram)  
        else:
            st.write("Veuillez sélectionner un candidat pour afficher l'histogramme.")

    # Deuxième graphique : Répartition des votes par parti
    with col3:
        fig_bar_plot = px.bar(data, x='Parties', y='Counts', color='Parties', title="Répartition des votes par parti", 
                    height=600, width=800, template="plotly_dark")
        fig_bar_plot.update_layout(title_font=dict(size=24)) 
        st.plotly_chart(fig_bar_plot)
            
    col1, col2 = st.columns(2)
# Premier graphique : Répartition des Élus par Sexe
    with col1:
        st.markdown("<h2 style='color: white;'>Répartition des Élus par sexe</h2>", unsafe_allow_html=True)
        fig_pie1 = px.pie(
            df, 
            values='Nombre', 
            names='Sexe', 
            color='Sexe',
            color_discrete_map={'Masculin': '#66b3ff', 'Féminin': '#ff9999'},
            hole=0.4,  
            height=700, 
            width=800, 
            template="plotly_dark"
        )
        st.plotly_chart(fig_pie1)

# Deuxième graphique : Répartition des Élus par Partie %
    with col2:
        st.markdown("<h2 style='color: white;'>Répartition des Élus par Partie %</h2>", unsafe_allow_html=True)
        fig_pie2 = px.pie(
            data,
            names='Parties',
            values='Counts',
            color='Parties',
            height=700, 
            width=800, 
            template="plotly_white"
        )
        fig_pie2.update_traces(textinfo='percent+label', textfont_size=15)
        
        
        # Affiche le graph dans 2ème colonne
        st.plotly_chart(fig_pie2)
        
    temp_df['% Abstentions'] = temp_df['% Abstentions'].astype(str)
    temp_df['% Abstentions'] = temp_df['% Abstentions'].str.replace('%', '').str.replace(',', '.').astype(float)
    abstention_data = temp_df.groupby('Libellé département')['% Abstentions'].mean().reset_index()
    st.markdown("<h2 style='color: white;'>Pourcentage d'Abstention par Département</h2>", unsafe_allow_html=True)

    abstention_chart = alt.Chart(abstention_data).mark_bar().encode(
        x=alt.X('Libellé département', title='Département', sort='-y'),
        y=alt.Y('% Abstentions', title="Pourcentage d'Abstention"),
        color=alt.Color('% Abstentions', scale=alt.Scale(scheme='viridis'), legend=None),
        tooltip=['Libellé département', '% Abstentions']
    ).properties(
        width=1000,
        height=400
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_title(
        fontSize=16
    ).interactive()

    st.altair_chart(abstention_chart, use_container_width=True)
    
    
    #temp_df['% Abstentions'] = temp_df['% Abstentions'].astype(str)
    #temp_df['% Abstentions'] = temp_df['% Abstentions'].str.replace('%', '').str.replace(',', '.').astype(float)
    #abstention_data = temp_df.groupby('Libellé département')['% Abstentions'].mean().reset_index()
    st.markdown("<h2 style='color: white;'>Carte de la France avec le pourcentage d'abstention par département</h2>", unsafe_allow_html=True)
    geo_json_data = requests.get("https://france-geojson.gregoiredavid.fr/repo/departements.geojson").json()


    m = folium.Map(location=[46.603354, 1.888334], zoom_start=5)

  
    folium.Choropleth(
        geo_data=geo_json_data,
        data=abstention_data,
        columns=['Libellé département', '% Abstentions'],  
        key_on='feature.properties.nom',  
        fill_color='YlGnBu',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Pourcentage d'Abstention"
    ).add_to(m)

    
    for feature in geo_json_data['features']:
        dept_name = feature['properties']['nom']
        taux_abstention = abstention_data.loc[abstention_data['Libellé département'] == dept_name, '% Abstentions'].values
        if len(taux_abstention) > 0:
            feature['properties']['taux_abstention'] = taux_abstention[0]
        else:
            feature['properties']['taux_abstention'] = 'Non disponible'

    folium.GeoJson(
        geo_json_data,
        style_function=lambda feature: {
            'fillOpacity': 0,
            'weight': 0.5,
            'color': 'black'
        },
        tooltip=folium.GeoJsonTooltip(
            fields=['nom', 'taux_abstention'],  
            aliases=['Département: ', 'Taux d\'abstention: '],  
            localize=True
        )
    ).add_to(m)

    st_data = st_folium(m, width=800, height=700)
   

        