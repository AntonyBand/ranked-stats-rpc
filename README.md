# Ranked Stats RPC
Discord Rich Presence integration that shows statisctics of any player in MCSR Ranked.
![preview.gif](./assets/preview.gif)

Now it can only show:

- Current Elo
- Best completion time (PB)
- Average completion time (AVG)
- Played matches in current season

 ## Installation
 1. Make an application at [Discord Developer Portal](https://discord.com/developers/home). You can name it for example "Ranked Stats" and use [this icon](https://github.com/AntonyBand/ranked-stats-rpc/blob/main/assets/ranked_icon.png?raw=true) if you want.
 
 2. Open "General Information" section in the app settings and copy the Client ID. We'll use it for later.
 
 3. Install latest [Python](https://python.org) version.

 4. Install all the dependencies using  `pip install requests pypresence dotenv`  in the terminal
 
 4. Clone this repo (Click "Code"  and the "Download ZIP" or using your favorite method).
 
 5. Extract the archive where you want to keep the program.
 
 8. In the folder rename .env.example to .env.
 
 9. Insert your Client ID and nickname in the .env file.
 
 10. Run using  `python main.py` in the terminal.

 ### Honorable mentions
  - Thanks to [@NaddyMC](https://github.com/nadoms) for help in understanding the MCSR Ranked API
