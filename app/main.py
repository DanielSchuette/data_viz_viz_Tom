import os
import streamlit as st
import pandas as pd
# Import matplotlib
import matplotlib.pyplot as plt
import altair as alt
from plotly.subplots import make_subplots


st.header("Barley Visualization & Analysis")
data: pd.DataFrame = pd.read_csv("./data/barley_data.csv")
st.dataframe(data)


# Add header for the boxplot visualization
st.header("Yield Distribution by Year")

# Create a Plotly boxplot
import plotly.express as px

# Create boxplot grouped by year
fig = px.box(
    data,
    x='year',
    y='yield',
    color='year',
    title='Distribution of Barley Yields by Year',
    labels={'yield': 'Yield', 'year': 'Year'},
    height=500
)

# Update layout for better appearance
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Yield',
    showlegend=False,
    boxmode='group'
)

# Add p-value annotation in the middle of the plot
fig.add_annotation(
    x=0.5,  # Center of x-axis (0 to 1 range)
    y=0.9,  # Near the top of the plot
    xref="paper",
    yref="paper",
    text="p-value = 0.0003",
    showarrow=False,
    font=dict(size=14, color="black", family="Arial, sans-serif"),
    bgcolor="rgba(255, 255, 255, 0.7)",
    bordercolor="black",
    borderwidth=1,
    borderpad=4
)

# Display the boxplot
st.plotly_chart(fig, use_container_width=True)



# Compute mean yield by variety and site
mean_yield_by_variety_site = data.groupby(['variety', 'site'])['yield'].mean().reset_index()
varieties = mean_yield_by_variety_site['variety'].unique()
num_varieties = len(varieties)
cols = 2

# Define a color palette
color_palette = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Import plotly
import plotly.graph_objects as go

# Add header for the visualization section
st.header("Mean Yield by Variety and Site")

# Loop over varieties in groups of two (cols)
for i in range(0, num_varieties, cols):
    current_varieties = varieties[i:i+cols]
    
    # Create plotly subplots
    fig = make_subplots(
        rows=1, 
        cols=len(current_varieties),
        subplot_titles=current_varieties
    )
    
    # Find max yield for consistent y-axis
    subset = mean_yield_by_variety_site[
        mean_yield_by_variety_site['variety'].isin(current_varieties)
    ]
    max_yield = subset['yield'].max() * 1.15  # Add 15% padding
    
    # Plot each variety
    for j, variety in enumerate(current_varieties):
        variety_data = mean_yield_by_variety_site[mean_yield_by_variety_site['variety'] == variety]
        
        # Create bar chart
        fig.add_trace(
            go.Bar(
                x=variety_data['site'],
                y=variety_data['yield'],
                text=variety_data['yield'].round(2),
                textposition='outside',
                marker_color=color_palette[(i+j) % len(color_palette)]
            ),
            row=1, col=j+1
        )
        
        # Set y-axis range
        fig.update_yaxes(range=[0, max_yield], title_text='Mean Yield' if j == 0 else '', row=1, col=j+1)
        
    # Update layout
    fig.update_layout(
        showlegend=False,
        height=700,
        width=1200,
        xaxis_tickangle=-45
    )
    
    st.plotly_chart(fig, use_container_width=True)
