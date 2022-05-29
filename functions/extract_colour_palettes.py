from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

#TODO: Add docstrings to functions

user_agent = UserAgent()

def extract_team_legend(team_url):
    """
    """
    team_wiki = team_url.get("href")
    team_page = f"https://en.wikipedia.org{team_wiki}"
    team_page = requests.get(team_page,
         headers={'User-Agent':str(user_agent.chrome)})
    team_page_content = BeautifulSoup(team_page.content, features="html.parser")
    team_legend = team_page_content.select(".legend-color")
    return team_legend

def extract_colour_palette(legend_details):
    team_colour_palette = [{"team_number": team_number, "colour_number": colour_number, "colour": style.get("style")} for team_number, css_details in enumerate(legend_details) for colour_number, style in enumerate(css_details)]
    return team_colour_palette