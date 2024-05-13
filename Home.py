import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title ("Welcome to Airline Reviews EDA ✈️")
st.image("https://wallpapers.com/images/hd/sunset-silhouette-airplane-brh2gmlmjhnj74dv.webp")

df = pd.read_csv("Airline_review_clean.csv")

st.markdown('''Welcome to the fascinating Airline Reviews Dataset from airlinequality.com! This incredible resource contains valuable insights waiting to be explored. Let's embark on this exciting journey together to discover customer sentiments, analyze trends over time, predict ratings, and more, all aimed at improving airline experiences and creating happier passengers.
\nHere's a description for each column in the provided table:

Index: This column appears to be an index for the rows in the dataset. It assigns a unique identifier to each row.

Airline Name: This column contains the names of the airlines being reviewed by customers.

Overall Rating: This column represents the overall rating given by customers for the respective airline. Ratings are typically given on a scale, such as 1 to 10, where 1 is the lowest and 10 is the highest.

Review Date: This column denotes the date when the review was posted by the customer.

Verified: This column indicates whether the review was verified by the platform or service where the review was submitted. A value of True suggests that the review has been verified, while False suggests it may not have been verified.

Type Of Traveller: This column specifies the type of traveler who provided the review, such as solo leisure travelers, couples on leisure trips, business travelers, etc.

Seat Type: This column describes the type of seat or class the passenger flew in, such as Economy Class, Business Class, or First Class.

Date Flown: This column indicates the date when the flight was taken by the passenger.

Seat Comfort: This column reflects the rating provided by the customer regarding the comfort of the seat during the flight.

Cabin Staff Service: This column represents the rating given by the customer for the service provided by the cabin staff during the flight.

Food & Beverages: This column denotes the rating given by the customer for the quality of food and beverages served during the flight.

Ground Service: This column indicates the rating provided by the customer for the ground services of the airline, which may include check-in, boarding procedures, and baggage handling among others.

Value For money: This column represents the rating given by the customer for the value they received in relation to the price paid for the flight or services provided by the airline.

recommended: This column indicates whether the customer recommends the airline based on their experience. A value of True suggests a recommendation, while False suggests otherwise.

Year: This column specifies the year in which the review was made or the flight was taken.

Source : [Kaggle](https://www.kaggle.com/datasets/juhibhojani/airline-reviews)
''')

st.subheader('Sample Dataset')
if st.checkbox('Show Dataset'):
    st.dataframe(df.head(10))

