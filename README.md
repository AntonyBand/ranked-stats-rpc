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
 
 3. Go to Releases and grab the latest archive for your system. 
 
 4. Extract the archive wherever it's convenient for you.

 5. Open  `config.ini`  file and enter your nickname and the Client ID. It should look like this
 
 6. Now you can run (Double click on Windows, using terminal on Linux)  `ranked-stats-rpc` file and check your Discord profile.

 ## Troubleshooting
 If you have any issues make sure you did all installation steps correctly

 If the problem still exists, report an [issue](https://github.com/AntonyBand/ranked-stats-rpc/issues/new).

 ### Honorable mentions
  - Thanks to [@NaddyMC](https://github.com/nadoms) for help in understanding the MCSR Ranked API

 ### Compiling yourself
  I used Nuitka for making binaries:  `python -m nuitka --mode=onefile main.py --output-dir=build`
  
### TO-DO
- [x] Make binaries
- [ ] Add system tray support
