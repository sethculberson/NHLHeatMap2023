from hockey_rink import NHLRink
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as font_manager

font_path = "/Users/sethculberson/Library/Fonts/Gotham-Black.otf"
font_props = font_manager.FontProperties(fname=font_path)
background_color='#0C0D0E'

data_to_track = ["teamCode","xCord","yCord","shooterName","goal","time"]

df = pd.read_csv('data/shots_2023.csv')
filtered_df = df[data_to_track]
goal_scored = filtered_df[filtered_df['goal']==1]

print(goal_scored)