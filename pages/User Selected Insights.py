import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title ("Airline Insights✈️")
st.divider()

df_eda = pd.read_csv(r"D:\Data Science\Mid Project\Ahmed\Airline_review_clean.csv")
top_10 = df_eda['airline_name'].value_counts().head(10).reset_index()['airline_name'].to_list()

column1, column2 = st.columns(2)

st.header('')
mit1 = column1.metric(label="Verified Users Rate", value=((df_eda.groupby('verified')['review_date'].count())/(df_eda['review_date'].count())*100).round(2).reset_index()['review_date'][1])
mit2 = column2.metric(label="Not Verified Users Rate", value=((df_eda.groupby('verified')['review_date'].count())/(df_eda['review_date'].count())*100).round(2).reset_index()['review_date'][0])

selected = st.selectbox("Select the column to fillter by :", ['cabin_staff_service', 'ground_service', 'food_&_beverages', 'seat_comfort', 'value_for_money'],key=0)
fig = px.bar(df_eda.groupby(selected)['index'].count().reset_index(), x=selected, y='index', color=selected,template='plotly_dark', labels={'index':'Count'}, title=f'{selected} Count', text_auto=True)
st.plotly_chart(fig, use_container_width=True)
st.divider()

selected = st.selectbox("Select the column to fillter by :", ['cabin_staff_service', 'ground_service', 'food_&_beverages', 'seat_comfort', 'value_for_money'], key=1)
fig = px.bar(df_eda[df_eda.airline_name.isin(top_10)].groupby(['airline_name', selected])['index'].count().reset_index(), y='airline_name', x='index', color=selected, text_auto=True, template='plotly_dark', labels={'airline_name':'Airline Name', 'index':'Count'}, title=f'Top 10 Airlines {selected} Rating')
st.plotly_chart(fig, use_container_width=True)
st.divider()

selected = st.selectbox("Select the column to fillter by :", ['cabin_staff_service', 'ground_service', 'food_&_beverages', 'seat_comfort', 'value_for_money'], key=2)
fig = px.box(df_eda, y=selected, color='recommended', template='plotly_dark', labels={'recommended':'Recommended'}, title=f'{selected} vs Recommendation')
st.plotly_chart(fig, use_container_width=True)
st.divider()

selected = st.selectbox("Select the column to fillter by :", ['cabin_staff_service', 'ground_service', 'food_&_beverages', 'seat_comfort', 'value_for_money'], key=3)
fig = px.line(df_eda.groupby('year')[selected].mean().reset_index(),x="year", y=selected, markers=True, title=f"{selected} by Year", template='plotly_dark', labels={'year':'Year'})
st.plotly_chart(fig, use_container_width=True)
st.divider()

year = st.selectbox('Select Year :', sorted(df_eda['year'].unique().tolist()), key=4)
fig = px.bar(df_eda[df_eda['year'] == year].groupby('type_of_traveller')['index'].count().reset_index(), x='type_of_traveller', y='index', color='type_of_traveller', title=f'Types of Travel in {year}\nThe Count was {df_eda[df_eda["year"] == year]["type_of_traveller"].count()}', text_auto=True, template='plotly_dark', labels={'type_of_traveller':'Type of Traveller', 'index':'Count'})
st.plotly_chart(fig, use_container_width=True)
st.divider()

year = st.selectbox('Select Year :', sorted(df_eda['year'].unique().tolist()), key=5)
fig = px.bar(df_eda[df_eda['year'] == year].groupby('seat_type')['index'].count().reset_index(), x='seat_type', y='index', color='seat_type', title=f'Seat Types in {year}\nThe Count was {df_eda[df_eda["year"] == year]["seat_type"].count()}', text_auto=True, template='plotly_dark', labels={'seat_type':'Seat Type', 'index':'Count'})
st.plotly_chart(fig, use_container_width=True)
st.divider()