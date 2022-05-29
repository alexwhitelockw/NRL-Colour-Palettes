from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from functions.extract_colour_palettes import extract_team_legend
from functions.extract_colour_palettes import extract_colour_palette
import pandas as pd
import re
import requests

if __name__ == "__main__":

    # Base Request to obtain Wikipedia team links

    base_url = "https://en.wikipedia.org/wiki/National_Rugby_League"

    user_agent = UserAgent()

    base_url_request = requests.get(base_url, headers={'User-Agent':str(user_agent.chrome)})

    base_content = BeautifulSoup(base_url_request.content, features="html.parser")

    team_table = base_content.select(".navigation-not-searchable+ .wikitable th a")  # Table with NRL team page links

    team_links = [team_link for team_link in team_table if not team_link.find("img")]  # Differentiate team page links from logo image links

    team_links = [{"team_number": team_number, "team_name": team_link.get("title"),  "team_link": team_link} for team_number, team_link in enumerate(team_links)]  # Create an index value for each team in list (for future joins)

    # Extract colour palette details from each Wikipedia page

    team_legends = [extract_team_legend(link["team_link"]) for link in team_links]  # Extract legend from the Team page

    team_colour_palettes = extract_colour_palette(team_legends)  # Pull the background colour from the legend itself

    for team_colour in team_colour_palettes:  # Tidy CSS by obtaining background-colour and replacing colon
        background_colour = re.search(":[A-z0-9# ]+", team_colour["colour"]).group() 
        background_colour = re.sub(":", "", background_colour)
        team_colour["colour"] = background_colour

    # Output to CSV

    pd.DataFrame.from_dict(team_links).to_csv("data/colour_palette/team_names.csv", index=False)
    pd.DataFrame.from_dict(team_colour_palettes).to_csv("data/colour_palette/team_colour_palette.csv", index=False)
