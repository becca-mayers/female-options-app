#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 08:32:11 2022

@author: rebecca
"""

from sqlite3 import connect
import streamlit as st
from PIL import Image
import pandas as pd


#%% Page Configs & Styling

st.set_page_config(
    page_title = 'Female Options Calculator',
    page_icon = '🤹‍♀️',
    layout = 'wide',
    initial_sidebar_state = 'collapsed',
    menu_items = {'Get Help': 'https://www.extremelycoolapp.com/help',
                  'Report a bug': "https://www.extremelycoolapp.com/bug",
                  'About': 'Check out beccamayers.com for more info about the developer.'}
    )

# Hide hamburger + footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load button CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css('app.css')

#%% Data

@st.cache
def get_data():
    '''Fetch records from local sqlite db.
    Returns: Pandas Dataframe
    '''
    conn = connect('db.sqlite') 
    cur = conn.cursor()
    
    cur.execute('''SELECT * from demographics''')
    df_columns = ['Age', 'Sex', 'Marital_Status', 'Hispanic', 'Race', 'Income']
    return pd.DataFrame(cur.fetchall(), columns = df_columns)

@st.cache    
def get_height():
    '''Generate a list of height inputs for the height slider.
    Returns: list
    '''
    #make height
    height_range = []
    hx = [4,5,6]
    h2 = (range(1,13))
    for x in hx:  
        for two in h2:
            ss = (str(x) + "'" + str(two) + '"')
            height_range.append(ss)
    return height_range 

# Format slider string for $$
def cashify(val) -> str:
    return '${:,.2f}'.format(val)

#%% Base vars
df = get_data()
height_range = get_height()
age_range = df['Age'].drop_duplicates().sort_values().tolist()
race_options = df['Race'].drop_duplicates().sort_values().tolist()
income_range = df['Income'].drop_duplicates().sort_values().tolist() 
obesity_percentage = 31.7

#-----------------------------------------------------------------------------#
#%% Begin App

# Header/Subheader
st.markdown('# Female Options Calculator')
st.markdown('## What are the chances of finding the man of my dreams?')
st.markdown('The accurate alternative to the [Female Delusional Calculator](https://www.igotstandardsbro.com).')

# Hero image
kissing_frogs = Image.open('kissing-frogs.png')
st.image(kissing_frogs)

st.write('Data Sourced from the 2020 [US Census Annual Social and Economic Supplement (ASEC)](https://www.census.gov/data/datasets/time-series/demo/cps/cps-asec.2020.html#list-tab-YY1CQJF340IKCHJEXH)  data and the [Center for Disease Control and Prevention (CDC) Behavioral Risk Factor Surveillance System](https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Behavioral/hn4x-zwk7).')
st.markdown('''---''')

#%% Filter Widgets

# Age silder
age_slider = st.select_slider('**Age Range**', 
                              options = age_range, 
                              value = (age_range[15], age_range[-40]), 
                              key = 'age_slider',
                              label_visibility = 'visible')

st.markdown('''---''')

# Height silder
height_slider = st.select_slider('**Height Range**', 
                                  options = height_range, 
                                  value = (height_range[20], height_range[-10]), 
                                  key = 'height_slider',
                                  label_visibility = 'visible')

st.markdown('''---''')

# Income slider    
income_slider = st.select_slider('**Income Range**', 
                                  options = income_range, 
                                  value = (income_range[0], income_range[-10]), 
                                  format_func = cashify,
                                  key = 'income_slider',
                                  label_visibility = 'visible')

st.markdown('''---''')

col1, col2, col3 = st.columns([3, 1, 2])

with col1:
   
    # Race Multiselect 
    race_multiselect = st.multiselect('**Race**',
                                      options = race_options, 
                                      default = race_options,
                                      key = 'race_multiselect',
                                      label_visibility = 'visible')
with col2:
    
    st.write('')

with col3:
    
    st.write('')

    # Exclude obese
    exclude_obese = st.checkbox('*Exclude Obese*', value = False)

    if exclude_obese:
        #drop 31.7% of the dataframe
        drop_n_rows = int(len(df) * .317)
        print(drop_n_rows)
        df = df.reset_index()
        print(len(df))
        df = df[drop_n_rows:]
        print(len(df))

    # Exclude married
    exclude_married = st.checkbox('*Exclude Married*', value = False)
    
    if exclude_married:
        df = df.loc[df['Marital_Status'] != 'Married']
    
st.markdown('''---''')
    
bcol1, bcol2, bcol3 = st.columns(3)

with bcol1:
    st.write('')

with bcol2:
    st.button('What Are My Options?')

with bcol3:
    st.write('')

# Option results
#hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good',bar_value = 0)

st.markdown('''---''')

mcol1, mcol2, mcol3 = st.columns([1, 3, 1])

with mcol1:
    st.write('')

with mcol2:
    
    
    # Footer credits
    footer = '[About](https://www.github.com/becca-mayers/female-options-app) | [Contact](mail-to:rebecca.here.live@gmail.com) | Created with 💙 by [Rebecca Mayers](https://www.beccamayers.com) | Image Source [NBC News](https://www.nbcnews.com/better/lifestyle/how-be-better-online-dating-according-psychology-ncna979791)'
    st.markdown(footer, unsafe_allow_html = True)

with mcol3:
    st.write('')
