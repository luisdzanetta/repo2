import math
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#Define a configuração da página
st.set_page_config(page_title="Calculadora de Mínimo Efeito Detectável",
                   page_icon="https://www.google.com/url?sa=i&url=https%3A%2F%2Flogospng.org%2Flogo-banco-bradesco%2F&psig=AOvVaw3K43MPXg0ebPMPgDe6xJl_&ust=1682620842369000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCOie2ZyZyP4CFQAAAAAdAAAAABAD",
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

roboto = {"fontname": "Roboto", "size": "11"}
roboto_light = {"fontname": "Roboto", "size": "10", "weight": "light"}
roboto_title = {"fontname": "Roboto", "size": "12", "weight": "bold"}
roboto_small = {"fontname": "Roboto", "size": "7.5", "weight": "light"}

font = {"family": "sans-serif", "sans-serif": "roboto", "size": 11}

plt.rc("font", **font)


# Define the inputs using Streamlit widgets
sample_per_variant = st.number_input("Amostra por variante por semana:", value=1000, step=100, min_value=100, max_value=1000000)
base_conversion = st.number_input("Conversão do controle (%):", value=1.0, step=0.1, min_value=0.1, max_value=100.0) / 100
num_weeks = st.slider("Número de semanas do experimento", value=4, step=1, min_value=1, max_value=20)

# Define the MDE function
def calculate_mde(p, n):
    return math.sqrt((1/p - 1)/(n/16))


# Calculate the MDE for each week and store the data in a list of dictionaries
mde_data = []
for week in range(1, num_weeks+1):
    total_sample = sample_per_variant * week
    mde = calculate_mde(base_conversion, total_sample)
    mde_data.append({'Experiment week number': week, 'Total sample per variant': total_sample, 'Sample per variant': sample_per_variant, 'MDE': mde*100})

# Convert the list of dictionaries to a Pandas dataframe
mde_df = pd.DataFrame(mde_data)

# Display the table
st.write(mde_df)

# Plot the graph
fig, ax = plt.subplots()
ax.plot(mde_df['Experiment week number'], mde_df['MDE'])
ax.set(xlabel='Experiment week number', ylabel='MDE', title='MDE over time')
st.pyplot(fig)
