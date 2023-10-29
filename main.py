import streamlit as st 
import pandas as pd
import plotly.express as px 


st.title("In Search for Happiness")

x_axis_option = st.selectbox("Select the data for the X-axis",
                            ("GDP", "Happiness", "Generosity"))
y_axis_option = st.selectbox("Select the data for the Y-axis",
                            ("GDP", "Happiness", "Generosity"))


# Retrieve required data 
def get_data(x_axis_data, y_axis_data):
    df = pd.read_csv("happy.csv")
    x_axis_data_list = df[x_axis_data.lower()].tolist()
    y_axis_data_list = df[y_axis_data.lower()].tolist()
    return x_axis_data_list, y_axis_data_list

x_axis, y_axis = get_data(x_axis_option, y_axis_option)


# Adding a plotly chart
st.subheader(f"{x_axis_option} and {y_axis_option}")
figure = px.scatter(x=x_axis, y= y_axis, labels={"x": x_axis_option, "y": y_axis_option})
st.plotly_chart(figure)

