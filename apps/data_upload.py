import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
def app():
    txt1, img = st.columns(2)
    with txt1:
        st.markdown("### About Dataset:")
        st.markdown("###### Sample Sales Data set is downloaded from kaggle. The data includes Order Info, Sales, Customer and Shipping information. In this project I used the Sales data set to provide sales analysis, the main key performance indicators, shipping status monitoring, detailed analysis on countries location as a practice for a streamlit project. In addition to the analytics part, I have added a sales forecast section where the user    can predict the future sales")
        st.markdown('##')
        st.markdown("## Data Upload")
        st.markdown('##')
        # Upload the dataset and save as csv
        st.markdown("#### Upload the sales data set in a csv or excel file for analysis.") 
        st.write("\n")
    with img:
        image = Image.open('forecast.jpg')
        st.image(image)
###### Upload data in csv or excel format ######
    # Code to read a single file 
    st.markdown('##')
    st.markdown('##')
    upload, fig = st.columns(2)
    with upload:
        uploaded_file = st.file_uploader("Choose a file", type = ['csv', 'xlsx'])
        global data
        if uploaded_file is not None:
            try:
                data = pd.read_csv(uploaded_file,sep=",", encoding='Latin-1')
            except Exception as e:
                print(e)
                data = pd.read_excel(uploaded_file)
        ''' Load the data and save the columns with categories as a dataframe. 
        This section also allows changes in the numerical and categorical columns. '''
        if st.button("Load Data"):
            # Save raw data in csv file
            st.dataframe(data)
            data.to_csv('data/sales_data.csv', index=False)
