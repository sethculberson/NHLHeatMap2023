import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.font_manager as font_manager
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter

font_path = "/Users/sethculberson/Library/Fonts/Gotham-Black.otf"
font_props = font_manager.FontProperties(fname=font_path)
background_color='#0C0D0E'

data_to_track = ["shooterName","xGoal","xCordAdjusted","yCordAdjusted","shotOnEmptyNet","shotDistance"]

df = pd.read_csv('data/shots_2023.csv')

#cleaning data
filtered_df = df[data_to_track]
filtered_df = filtered_df[filtered_df["shotOnEmptyNet"]==0]
filtered_df = filtered_df[filtered_df["shotDistance"] <= 89]
filtered_df = filtered_df[filtered_df["xCordAdjusted"] <= 89]

[x,y] = np.round(np.meshgrid(np.linspace(0,100,100),np.linspace(-42.5,42.5,85)))
x_goals = griddata((filtered_df["xCordAdjusted"],filtered_df["yCordAdjusted"]),filtered_df["xGoal"],(x,y),method ="cubic",fill_value=0)
x_goals_smooth = gaussian_filter(x_goals,sigma=3)

fig = plt.figure(figsize=(5,6),facecolor="w",edgecolor="k")
plt.imshow(x_goals_smooth,origin="lower")
plt.colorbar(orientation="horizontal",pad=0.05)
plt.title("Expected Goals by Shot Location",font=font_props)
plt.axis("off")
plt.show()