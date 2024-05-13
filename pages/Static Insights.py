import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title ("Airline Insights✈️")
st.divider()

df_eda = pd.read_csv(r"Airline_review_clean.csv")
top_10 = df_eda['airline_name'].value_counts().head(10).reset_index()['airline_name'].to_list()

fig = px.bar(df_eda[df_eda['airline_name'].isin(top_10)].groupby(['airline_name', 'recommended'])['index'].count().reset_index(), y='airline_name', x='index', color='recommended', barmode='group', text_auto=True, template='plotly_dark', labels={'airline_name':'Airline Name', 'index':'Count', 'recommended':'Recommended'}, title='Top 10 Airlines Recommendation') 
st.plotly_chart(fig, use_container_width=True)
st.divider()

fig = px.histogram(df_eda, x='overall_rating', color='recommended', barmode='group', labels={'overall_rating':'Rating', 'recommended':'Recommended'}, title='Rating vs Recommendation' ,text_auto=True, template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.divider()

column1,column2 = st.columns(2)
fig = px.bar(df_eda.groupby('seat_type')['index'].count().reset_index(), x='seat_type', y='index', color='seat_type', template='plotly_dark', labels={'seat_type':'Seat Type', 'index':'Count'}, title='Seat Type Count', text_auto=True)
column1.plotly_chart(fig, use_container_width=True)
fig = px.sunburst(df_eda, path=['type_of_traveller', 'seat_type'], values='index', color='type_of_traveller', title='Types of Traveller vs Seat Type', labels={'type_of_traveller':'Type of Traveller', 'seat_type':'Seat Type', 'index':'Count'}, template='plotly_dark')
column2.plotly_chart(fig, use_container_width=True)
st.divider()

fig = px.bar(df_eda.groupby('type_of_traveller')['index'].count().reset_index(), x='type_of_traveller', y='index', color='type_of_traveller', template='plotly_dark', labels={'type_of_traveller':'Type of Traveller', 'index':'Count'}, title='Type of Traveller Count', text_auto=True)
st.plotly_chart(fig, use_container_width=True)
st.divider()

fig = px.bar(df_eda.groupby('recommended')['index'].count().reset_index(), x='recommended', y='index',labels={'recommended':'Recommended', 'index':'Count'}, title='Recommendation Count', text_auto=True, color='recommended', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.divider()
