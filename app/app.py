import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

data = pd.read_csv('/Users/florian/Documents/GitHub/Streamlit Exercise/Gapminder Data/data.csv')

st.title('Florians Streamlit App')
st.write('Below you can find the Gapminder data.')

year = st.sidebar.slider('Select Year', min_value=1990, max_value=2019, step=1)

country = st.sidebar.multiselect('Select Countries', data.country.unique())

select = data[data['year']==year]

subset_df = select.loc[lambda d: d['country'].isin(country)]

sns.scatterplot(data=subset_df, x=np.log(data['GNI']), y='life expectancy', size='population', hue='country', legend='full')
st.pyplot()