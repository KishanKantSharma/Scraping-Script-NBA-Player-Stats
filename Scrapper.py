import requests
from bs4 import BeautifulSoup
import csv

# Prompt for the NBA season year
print("Which NBA Season Data you want: ")
Year = input()  # Expecting YYYY format

# URL of the website containing NBA player stats
url = f"https://www.basketball-reference.com/leagues/NBA_{Year}_per_game.html"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'per_game_stats'})

    if table:
        csv_filename = f"nba_player_stats_{Year}.csv"

        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)

            header = [th.text for th in table.thead.findAll('th')]
            writer.writerow(header)

            rows = table.tbody.findAll('tr')
            for row in rows:
                data = [td.text for td in row.findAll('td')]
                writer.writerow(data)

        print(f"Scraped NBA player stats and saved to {csv_filename}")
    else:
        print("Error: Could not find the stats table on the page.")
else:
    print(f"Error: Failed to retrieve data. Status code {response.status_code}")
