import matplotlib.pyplot as plt
import pandas as pd
import hockey_rink

plt.rcParams["toolbar"] = "None"

data_to_track = ["shooterName","xGoal","goal","xCordAdjusted","yCordAdjusted","shotOnEmptyNet","shotDistance"]

df = pd.read_csv('data/shots_2023.csv')

#cleaning data
filtered_df = df[data_to_track]
filtered_df = filtered_df[filtered_df["shotOnEmptyNet"]==0]
filtered_df = filtered_df[filtered_df["shotDistance"] <= 89]
filtered_df = filtered_df[filtered_df["xCordAdjusted"] <= 89]

def plot_shots_by_name(text):
    rink = hockey_rink.Rink(rotation=90)
    player_name = text
    filtered_df = df[data_to_track]
    filtered_df = filtered_df[filtered_df["shooterName"]==player_name]
    
    goals = filtered_df[filtered_df["goal"]==1]
    misses = filtered_df[filtered_df["goal"]==0]

    fig, axes = plt.subplots(1,1,figsize=(6,8))

    rink.scatter(x=goals["xCordAdjusted"], y=goals["yCordAdjusted"], color="green",alpha=0.8,s=goals["xGoal"]*240+20, ax=axes,plot_range="ozone",draw_kw={"display_range": "ozone"})
    rink.scatter(x=misses["xCordAdjusted"], y=misses["yCordAdjusted"], color="red",alpha=0.2, s=misses["xGoal"]*240+20,ax=axes,plot_range="ozone",draw_kw={"display_range": "ozone"})
    plt.show()

plot_shots_by_name("Connor McDavid")