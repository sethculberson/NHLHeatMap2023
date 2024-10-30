import matplotlib.pyplot as plt
import pandas as pd
import hockey_rink

#Disabling the toolbar in matplot
plt.rcParams["toolbar"] = "None"

df = pd.read_csv('data/shots_2023.csv')

#Selecting which statistics to analyze out of the data set
data_to_track = ["shooterName","xGoal","goal","xCordAdjusted","yCordAdjusted","shotOnEmptyNet","shotDistance"]

#cleaning the data
filtered_df = df[data_to_track]
filtered_df = filtered_df[filtered_df["shotOnEmptyNet"]==0] #not tracking empty net shots
filtered_df = filtered_df[filtered_df["shotDistance"] <= 89]
filtered_df = filtered_df[filtered_df["xCordAdjusted"] <= 89]

#set up rink and fig, axes
rink = hockey_rink.Rink(rotation=90,net={"visible": False}) #rotating the rink vertically
fig, axes = plt.subplots(1,1,figsize=(6,8))

#In the future, the name will be input by the user, and the heat map will be generated
def plot_shots_by_name(text):
    player_name = text
    playerspecific_df = filtered_df[filtered_df["shooterName"]==player_name]
    
    goals = playerspecific_df[playerspecific_df["goal"]==1]
    misses = playerspecific_df[playerspecific_df["goal"]==0]

    #create scatter plots for makes/misses, with the point size being weighted by the expected goal probability for the shot
    rink.scatter(x=goals["xCordAdjusted"], y=goals["yCordAdjusted"], color="green",alpha=0.8,s=goals["xGoal"]*240+20, ax=axes,plot_range="ozone",draw_kw={"display_range": "ozone"})
    rink.scatter(x=misses["xCordAdjusted"], y=misses["yCordAdjusted"], color="red",alpha=0.2, s=misses["xGoal"]*240+20,ax=axes,plot_range="ozone",draw_kw={"display_range": "ozone"})
    plt.title(f"{player_name} 2023 Shots")
    plt.show()

#example usage of function
plot_shots_by_name("Connor McDavid")