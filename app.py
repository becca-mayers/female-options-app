#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 08:32:11 2022

@author: rebecca
"""

from sqlite3 import connect
from copy import deepcopy
from math import floor
import streamlit as st
from numpy import mean
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
                  'About': 'Check out beccamayers.com for more info about the developer.'})

#%% Reduce header padding; Hide hamburger + footer; Reduce footer padding
hide_streamlit_style = """
                        <style>
                            div.block-container {padding-top:1rem;}
                            #MainMenu {visibility: hidden;}
                            footer {visibility: hidden;, padding-top:0rem; padding-bottom:0rem;}
                        </style>
                        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#%% Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css('app.css')

#%% Data
@st.cache
def get_data():
    '''Fetch records from local sqlite db.
    Returns: Pandas Dataframe'''
    conn = connect('db.sqlite') 
    cur = conn.cursor()

    cur.execute('''SELECT * from nhis''')
    nhis_columns = ['Income', 'Weight', 'isObese', 'Marital_Status', 'isHispanic', 'Race', 'Gender', 'Age', 'Height', 'height_feet', 'height_inches']
    nhis_df = pd.DataFrame(cur.fetchall(), columns = nhis_columns)

    return nhis_df

# Format income slider labels for $$
def cashify(val) -> str:
    '''Transforms income integer into normalized monetary string formatting.
    Params: interger value
    Returns: formatted monetary str'''
    return '${:,}'.format(val) 

# Format height slider labels for height
def heightify(val):
    '''Transforms height in inches to normalized height notation (ex. 4'11")
    Returns: str'''
    feet = floor(val / 12)
    inches = int(val - (feet * 12))
    height_string = str(feet) + "'" + str(inches) + '"' 
    return height_string

# Make 25% & 75% Slider ranges
def get_slider_ranges(var_list):
    '''Get 25th decile
    Params: var_list - list of unique numeric values for a given variable
    Returns: slider_value - tuple'''
    decile25 = floor(len(var_list) * .25)
    slider_value = (var_list[decile25], var_list[-decile25])
    return slider_value

def reindex_df(df):
    '''Returns the dataframe's index to an integer range starting from 0
    Params: pandas dataframe
    Returns: transformed pandas dataframe'''
    return df.reset_index().drop('index', axis = 1)
        
#%% Base vars
df = get_data()
age_range = df['Age'].drop_duplicates().sort_values().tolist()
race_options = df['Race'].drop_duplicates().sort_values().tolist()
income_range = df['Income'].drop_duplicates().sort_values().tolist() 

# Height range initially set to Male gender only to align with default Male gender selection
initial_male_df = df.loc[df['Gender'] == 'Male']
initial_male_df = reindex_df(initial_male_df)
st.session_state.height_range = initial_male_df['Height'].drop_duplicates().sort_values().tolist()

#-----------------------------------------------------------------------------#
#%% Begin App

# Header credits
header = '[About](https://www.github.com/becca-mayers/female-options-app) | [Contact](mail-to:rebecca.here.live@gmail.com)'
st.markdown(header, unsafe_allow_html = True)

st.markdown('''---''')

# Header/Subheader
st.markdown('# Female Options Calculator')
st.markdown('## What are the chances of finding the man of my dreams?')
st.markdown('The accurate alternative to the [Female Delusional Calculator](https://www.igotstandardsbro.com).')

# Hero image
kissing_frogs = Image.open('imgs/kissing-frogs.png')
st.image(kissing_frogs)
st.write('Image Source [NBC News](https://www.nbcnews.com/better/lifestyle/how-be-better-online-dating-according-psychology-ncna979791). Data Sourced from the [2020 CDC National Health Interview Survey (NHIS)](https://www.cdc.gov/nchs/nhis/2020nhis.htm)  data.')

st.markdown('''---''')

# Filter Widgets

#%% Preferences & Exclusions
ccol1, ccol2, ccol3, col4 = st.columns(4)
with ccol1:
    st.write('**Partner Gender Preference**')
with ccol2:
    st.write('')
with ccol3:
    st.write('**Exclusions**')
with col4:
    st.write('')
    
pcol1, pcol2, pcol3, pcol4 = st.columns(4)
with pcol1:    
    # Male Partner
    male_partner_checkbox = st.checkbox('Male', value = True, key = 'male_partner_checkbox')

with pcol2:
    # Female Partner
    female_partner_checkbox = st.checkbox('Female', value = False, key = 'female_partner_checkbox')
           
with pcol3:
    # Exclude obese
    obesity_checkbox = st.checkbox('*Exclude Obese*', value = False, key = 'obesity_checkbox')

with pcol4:
    # Exclude married
    married_checkbox = st.checkbox('*Exclude Married*', value = True, key = 'married_checkbox')
    
#%% Gender preference -> Height range        
# Update height range for female partners
if (st.session_state.female_partner_checkbox is True) & (st.session_state.male_partner_checkbox is False):
    female_df = df.loc[df['Gender'] == 'Female']
    female_df = reindex_df(female_df)
    st.session_state.height_range = female_df['Height'].drop_duplicates().sort_values().tolist()

#%% Gender preference warning
if (st.session_state.male_partner_checkbox is False) & (st.session_state.female_partner_checkbox is False):
   
    # Stop the forward momentum of the application
    st.warning('Must select at least one partner gender preference.')   
    st.markdown('''---''')
    
else:
    
    #%% Continue on with application    
    st.markdown('''---''')
    
    #%% Age silder
    age_slider = st.select_slider('**Age Range**', 
                                  options = age_range, 
                                  value = get_slider_ranges(age_range), 
                                  key = 'age_slider',
                                  label_visibility = 'visible')
    
    st.markdown('''---''')
    
    height_slider = st.select_slider('**Height Range**', 
                                      options = st.session_state.height_range, 
                                      value = get_slider_ranges(st.session_state.height_range), 
                                      format_func = heightify,
                                      key = 'height_slider',
                                      label_visibility = 'visible')
    
    st.markdown('''---''')
    
    #%% Income Slider    
    income_slider = st.slider('**Minimum Annual Income**', 
                                min_value = min(income_range),
                                max_value = max(income_range),
                                value = int(mean(income_range)),
                                format = '$%.0f',
                                key = 'income_slider',
                                label_visibility = 'visible')
    
    st.markdown('''---''')
    
    #%% Race Multiselect 
    race_multiselect = st.multiselect('**Race**',
                                      options = race_options, 
                                      default = race_options,
                                      key = 'race_multiselect',
                                      label_visibility = 'visible')    
    
    st.markdown('''---''')
    
    #%% Options Button  
    bcol1, bcol2, bcol3 = st.columns(3)
    
    with bcol1:
        st.write('')
    
    with bcol2:
        options_placeholder = st.empty()
        options_button = options_placeholder.button('What Are My Options?')
    
    with bcol3:
        st.write('')

    if options_button:
    
        # Make a copy of the raw df to work with
        opt_df = deepcopy(df)
        
        # Run initial checks
        
        if len(st.session_state.race_multiselect) == 0:
            st.error('Must select one or more race types to continue.')
            st.stop()
        
        elif (st.session_state.female_partner_checkbox == False) & (st.session_state.male_partner_checkbox == False):
            st.error('Must select at least one partner\'s gender.')
            st.stop()
        
        else:
        
            #Filter for male partner gender
            if st.session_state.male_partner_checkbox is False:
                opt_df = opt_df.loc[opt_df['Gender'] != 'Male']
                opt_df = reindex_df(opt_df)
            
            #Filter for female partner gender
            if st.session_state.female_partner_checkbox is False:
                opt_df = opt_df.loc[opt_df['Gender'] != 'Female']
                opt_df = reindex_df(opt_df)
                    
            # Married percentages
            total_married = len(opt_df[opt_df['Marital_Status'] == 'Married'])
            percent_married = round((total_married / len(opt_df)) * 100, 1)
            percent_not_married = 100 - percent_married
            
            #Handled for excluding married
            if st.session_state.married_checkbox is True:
                opt_df = opt_df.loc[opt_df['Marital_Status'] != 'Married']
                opt_df = reindex_df(opt_df)
          
            # Declare original dating pool size
            dating_pool_length = len(opt_df)
            
            #%% Filters for Age, Height, Income, Race, & Obesity
    
            #Filter for age
            #selected_age_tuple = st.session_state.age_slider
            opt_df = opt_df.loc[(opt_df['Age'] >= st.session_state.age_slider[0]) & (opt_df['Age'] <= st.session_state.age_slider[1])]
            opt_df = reindex_df(opt_df)
            
            #Filter for height
            selected_height_tuple = st.session_state.height_slider
            opt_df = opt_df.loc[(opt_df['Height'] >= st.session_state.height_slider[0]) & (opt_df['Height'] <= st.session_state.height_slider[1])]
            opt_df = reindex_df(opt_df)
    
            #Filter for income
            #selected_income = st.session_state.income_slider
            opt_df = opt_df.loc[opt_df['Income'] >= st.session_state.income_slider]
            opt_df = reindex_df(opt_df)
    
            #Filter for race
            #selected_race_list = st.session_state.race_multiselect
            opt_df = opt_df.loc[opt_df['Race'].isin(st.session_state.race_multiselect)]
            opt_df = reindex_df(opt_df)
            
            # Get obesity percentage 
            total_obese = len(opt_df[opt_df['isObese'] == 'Yes'])
            percent_obese = round((total_obese / len(opt_df)) * 100, 1)
            percent_not_obese = 100 - percent_obese
            
            #Handle for excluding obese
            if st.session_state.obesity_checkbox is True:
                opt_df = opt_df.loc[opt_df['isObese'] != 'Yes']
                opt_df = reindex_df(opt_df)
            
            percentage_of_dating_pool = (len(opt_df) / dating_pool_length) * 100
            rounded_percentage_of_dating_pool = round(percentage_of_dating_pool, 2)
            
            #%% Display Results
            options_placeholder.empty()
            
            with st.expander('*Results*', expanded = True):
                results_text = '<p style="text-align:center; font-family:serif; font-size: 30px; font-style:italic;"><span style="color:Green;">{}%</span> of your dating pool</p>'.format(str(rounded_percentage_of_dating_pool))
                st.markdown(results_text, unsafe_allow_html=True)
              
            #%% Display Details 
            with st.expander('*Percentage of Total Available Selection*', expanded = True):
    
                dcol0, dcol1, dcol2, dcol3, dcol4 = st.columns(5)
                
                # Age
                with dcol0:
                    age_str = str(st.session_state.age_slider[0]) + '-' + str(st.session_state.age_slider[1])
                    age_selection_len = st.session_state.age_slider[1] - st.session_state.age_slider[0]
                    age_selection_total = max(age_range) - min(age_range)
                    age_percentage = round((age_selection_len / age_selection_total) * 100, 1)
                    st.metric('Age', str(age_percentage) + '%')
                    
                # Race
                with dcol1:
                    race_str = str(len(st.session_state.race_multiselect)) + ' of ' + str(len(race_options))
                    race_selection_len = len(st.session_state.race_multiselect)
                    race_selection_total = len(race_options)
                    race_percentage = round((race_selection_len / race_selection_total) * 100, 1)
                    st.metric('Race', str(race_percentage) + '%')
                
                # Income
                with dcol2:
                    income_diff = max(income_range) - st.session_state.income_slider
                    income_percentage = round((income_diff / max(income_range) * 100), 1)
                    st.metric('Income', str(income_percentage) + '%')
                
                # Height
                with dcol3:
                    height_selection = st.session_state.height_slider[1] - st.session_state.height_slider[0]
                    height_total = df['Height'].max() - df['Height'].min()
                    height_percentage = round((height_selection / height_total) * 100, 1)
                    st.metric('Height', str(height_percentage) + '%')
                    
                # Obesity
                with dcol4:
                    if st.session_state.obesity_checkbox is True:
                        st.metric('Exclude Obesity', str(percent_not_obese) + '%')
                    elif st.session_state.obesity_checkbox is False:
                        st.metric('Include Obesity', '100%')
    
                st.markdown('''---''')   
                st.markdown('*Note: For informational purposes only. Make a change to any of your current selections to play with your dating pool results.*')
            
    st.markdown('''---''')

#%% Footer
mcol1, mcol2, mcol3 = st.columns([2, 3, 2])

with mcol1:
    st.write('')

with mcol2:  
    # Footer credits
    footer = '[About](https://www.github.com/becca-mayers/female-options-app) | [Contact](mail-to:rebecca.here.live@gmail.com) | Created with 💙 by [Rebecca Mayers](https://www.beccamayers.com)'
    st.markdown(footer, unsafe_allow_html = True)

with mcol3:
    st.write('')
