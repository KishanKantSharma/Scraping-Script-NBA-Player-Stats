# Scraping-Script-NBA-Player-Stats


This Python script allows you to scrape NBA player statistics from the 2024 season from the Basketball Reference website. 
It uses the `requests` and `BeautifulSoup` libraries to extract data from the website and saves the information in a CSV file.

## Prerequisites

Before running the script, make sure you have the necessary Python libraries installed. You can install them using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Run the script:

```bash
python nba_player_stats_scraper.py
```

4. The script will fetch the data from the website and save it as a CSV file named `nba_player_stats_2021.csv`.

## CSV File

The generated CSV file contains the following columns:

- Player
- Pos (Position)
- Age
- Team
- G (Games Played)
- GS (Games Started)
- MP (Minutes Played per Game)
- FG (Field Goals Made per Game)
- FGA (Field Goals Attempted per Game)
- FG% (Field Goal Percentage)
- 3P (3-Point Field Goals Made per Game)
- 3PA (3-Point Field Goals Attempted per Game)
- 3P% (3-Point Field Goal Percentage)
- 2P (2-Point Field Goals Made per Game)
- 2PA (2-Point Field Goals Attempted per Game)
- 2P% (2-Point Field Goal Percentage)
- eFG% (Effective Field Goal Percentage)
- FT (Free Throws Made per Game)
- FTA (Free Throws Attempted per Game)
- FT% (Free Throw Percentage)
- ORB (Offensive Rebounds per Game)
- DRB (Defensive Rebounds per Game)
- TRB (Total Rebounds per Game)
- AST (Assists per Game)
- STL (Steals per Game)
- BLK (Blocks per Game)
- TOV (Turnovers per Game)
- PF (Personal Fouls per Game)
- PTS (Points per Game)

The filtered CSV file Contains the following columns: 

- Player
- Age
- Team
- Position
- Games_played
- Free_Throws
- Total_Rebounds
- Assists
- Steals
- Blocks
- Fouls
- Points

## Contributing

Feel free to contribute to this project by creating pull requests or reporting issues.