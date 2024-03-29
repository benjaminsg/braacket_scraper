import requests
from bs4 import BeautifulSoup
from config import players
from config import rankings

players = [players.Trail, players.AwesomeVideoGames, players.Twisty, players.Sweat,
           players.Primer, players.TS420]
opponents = players.copy()

ranking = rankings.SpringSummer2023_NE

for player1 in players:
    opponents.pop(0)
    for player2 in opponents:
        if(player1.league != ranking.league or player2.league != ranking.league):
            raise Exception("One or more players leagues do not match ranking league")
        URL = "https://braacket.com/league/" + player1.league.id + "/player/" + player1.id + "?ranking=" + ranking.id + "&player_hth=" + player2.id
        page = requests.get(URL)
        
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="content_body")
        job_elements = results.find_all("td", class_="text-right text-bold")
        
        set_wins = job_elements[0].text
        set_losses = job_elements[2].text
        
        game_wins = job_elements[3].text
        game_losses = job_elements[4].text
        
        print(player1.name + " " + set_wins + " - " + set_losses + " " + player2.name)