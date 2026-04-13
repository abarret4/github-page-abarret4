import numpy as np
import pandas as pd
import plotly.express as px

fields = [
    "Film",
    "Year",
    "Writer",
    "Director",
    "Producer",
    "Location"
]

phl_films = pd.read_csv("films.csv", usecols=fields)