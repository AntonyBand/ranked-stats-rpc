from dotenv import load_dotenv
from os import getenv
from pypresence import Presence
from pypresence.types import ActivityType
from requests import get
from time import sleep

# Ranked API variables
nickname = "Feinberg"
endpoint = "https://api.mcsrranked.com/"
uuid = get(f"{endpoint}users/{nickname}").json()["data"]["uuid"]

# Main functions
def get_matches_played(): # Get number of ranked matches
    global played
    played = get(f"{endpoint}users/{nickname}").json()["data"]["statistics"]["season"]["playedMatches"]["ranked"]
    return(f"{played} matches")

def get_average(played: int): # Get average completion time
    total_ms = 0
    completions = 0
    last_id = None
    remaining = played

    while remaining > 0:
        query_size = min(remaining, 100)
        params = {
            "count": query_size,
            "type": 2
        }
        if last_id != None:
            params["before"] = last_id
        response = get(f"{endpoint}users/{nickname}/matches", params=params).json()["data"]

        for match in response:
            if (
                match["result"]["uuid"] == uuid
                and not match["forfeited"]
                and not match["decayed"]
            ):
                total_ms += match["result"]["time"]
                completions += 1
            last_id = match["id"]

        remaining -= len(response)
    average = total_ms / completions
    m = int(average // 60000)
    s = int(average % 60000) // 1000
    return f"Average - {m}:{s:02d}"

def get_elo():
    ranks = [
        (400, "Coal I"), (500, "Coal II"), (600, "Coal III"),
        (700, "Iron I"), (800, "Iron II"), (900, "Iron III"),
        (1000, "Gold I"), (1100, "Gold II"), (1200, "Gold III"),
        (1300, "Emerald I"), (1400, "Emerald II"), (1500, "Emerald III"),
        (1650, "Diamond I"), (1800, "Diamond II"), (2000, "Diamond III"),
    ]
    elo = get(f"{endpoint}users/{nickname}").json()["data"]["eloRate"]
    if elo is None:
        return("Unrated")
    if elo >= 2000:
        return(f"Netherite - {elo}")
    for limit, name in ranks:
        if elo < limit:
            return(f"{name} - {elo}")

def get_pb():
    pb_ms = get(f"{endpoint}users/{nickname}").json()["data"]["statistics"]["total"]["bestTime"]["ranked"]
    m = int(pb_ms // 60000)
    s = int(pb_ms % 60000) // 1000
    return(f"PB - {m}:{s:02d}")


# Rich Presence init
_ = load_dotenv() # Load CLIENT_ID variable from .env
rpc = Presence(getenv("CLIENT_ID"))
rpc.connect()

# Get all stats once
stats = {
    "elo": get_elo(),
    "matches": get_matches_played(),
    "pb":  get_pb(),
    "avg": get_average(played),
}
# Main Loop
while True:
    timer = 0
    # Update stats from API every 3 minutes
    if timer >= 180:
        matches = get_matches_played()
        average = get_average(played)
        elo = get_elo()
        pb = get_pb()
        timer = 0
        print("Stats updated!")

    for value in stats.values():
        rpc.update(
            activity_type=ActivityType.LISTENING,
            details=f"- {nickname} -",
            details_url="https://mcsrranked.com/stats/AntonyBand",
            state=value,
            instance=True
        )
        sleep(5)
    timer += 5
