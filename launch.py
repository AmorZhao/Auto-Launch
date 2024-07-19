import os
import webbrowser

filepaths = [
    '"C:/Users/AMZ/AppData/Local/Programs/Notion/Notion.exe"',  # Notion 
    '"C:/Program Files/Docker/Docker/Docker Desktop.exe"',  # Docker
    '"C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE"',  # Outlook
    '"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"',  # Edge
    '"C:/Program Files/Slack/slack.exe"',  #Slack
    '"C:/Users/AMZ/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/JetBrains Toolbox/Rider.lnk"',  # Rider
    '"C:/Users/AMZ/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Microsoft Teams.lnk"'  # Teams

]
for filepath in filepaths:
    os.startfile(filepath)

webbrowser.open('https://tapas-live.azurewebsites.net/user/44')

exit()
