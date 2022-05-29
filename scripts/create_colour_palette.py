import pandas as pd

# Read Colour Palette Files
team_names = pd.read_csv("data/colour_palette/team_names.csv")
team_colour_palette = pd.read_csv("data/colour_palette/team_colour_palette.csv")

team_colour_palette = team_names.merge(
        team_colour_palette,
        on="team_number"
    )

