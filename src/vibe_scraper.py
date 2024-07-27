import requests
from bs4 import BeautifulSoup

def scrape_vibes():
    url = "https://vibes.lol"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    vibe_elements = soup.find_all('div', class_='vibe')
    vibes = [vibe.text.strip() for vibe in vibe_elements]
    
    return vibes

def get_random_vibe():
    vibes = scrape_vibes()
    if vibes:
        return random.choice(vibes)
    return "No vibes found"
