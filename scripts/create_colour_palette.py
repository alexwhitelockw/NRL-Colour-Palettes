import pandas as pd

# Read and Merge Colour Palette Files
team_names = pd.read_csv("data/colour_palette/team_names.csv")
team_colour_palette = pd.read_csv("data/colour_palette/team_colour_palette.csv")

team_colour_palette = team_names.merge(
        team_colour_palette,
        on="team_number"
    )

# Correct colour names to hex values

team_colour_palette.loc[:, "colour"] = team_colour_palette["colour"].str.lower()

team_colour_palette.loc[team_colour_palette["colour"] == "maroon", "colour"] = "#800000"
team_colour_palette.loc[team_colour_palette["colour"] == "gold", "colour"] = "#FFD700"
team_colour_palette.loc[team_colour_palette["colour"] == "white", "colour"] = "#FFFFFF"
team_colour_palette.loc[team_colour_palette["colour"] == "skyblue", "colour"] = "#87CEEB"
team_colour_palette.loc[team_colour_palette["colour"] == "black", "colour"] = "#000000"
team_colour_palette.loc[team_colour_palette["colour"] == "dodgerblue", "colour"] = "#1E90FF"
team_colour_palette.loc[team_colour_palette["colour"] == "red", "colour"] = "#FF0000"
team_colour_palette.loc[team_colour_palette["colour"] == "navy", "colour"] = "#1E90FF"
team_colour_palette.loc[team_colour_palette["colour"] == "green", "colour"] = "#008000"
team_colour_palette.loc[team_colour_palette["colour"] == "yellow", "colour"] = "#FFFF00"
team_colour_palette.loc[team_colour_palette["colour"] == "silver", "colour"] = "#C0C0C0"

team_colour_palette.loc[:, "colour"] = team_colour_palette["colour"].str.upper()

# Output Palette to CSV

team_colour_palette[["team_name", "colour_number", "colour"]].to_csv("data/colour_palette/full_nrl_colour_palette.csv", index=False)