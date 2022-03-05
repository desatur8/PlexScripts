# PlexScripts

The script consists of 3 files:

* plex_config.py <br />
  ```This is where you will add your settings that the two scripts will use```
* Unwatched.py <br />
  ```A script that will add first unwatched episode of a given plex collection to a playlist, and randomize the playlist```
* Reruns.py <br />
  ```A script that will add previoulsy watched episodes of a given plex collection to a playlist, and randomize the playlist```


# plex_config.py
PLEX_URL = http://x.x.x.x:32400 ```url of your plex server``` <br />
PLEX_TOKEN = 123ABcdEf567 ```url of your plex server```<br />
NUMBER_OF_SHOWS = 5 ```total number of episodes that will be in the final playlist```<br />
NUMBER_OF_DAYS_TO_NOT_RERUN = 30 ```if a episode was already played in the past xx days, it wont be added```<br />
<br />
# Unwatched.py
The following can be changed in the script
<br />
COLLECTION_NAME = 'Evening Watching' ```name of the collection in Plex that is to be used to populate the playlists``` <br />
MY_PLAYLIST = 'TEST' ```The name of the playlist that will be created``` <br />
LIBRARY_NAME = 'TV Shows' ```The name of the library where the TV Shows are located in Plex``` <br />
NUMBER_OF_EP_OVERRIDE = 0 ```If you want to override the number of shows to be added to a different number than in the config``` <br />
<br />
# Reruns.py
```For reruns, a collection or individual shows can be named. If manual adding of show names are used, change collection name to 0 COLLECTION_NAME = 'Sitcoms'```
SHOWS_TO_ADD = 'The Big Bang Theory,Gary Unmarried,Two and a half men,3rd rock from the sun,scrubs,rules of engagement'
COLLECTION_NAME = 'Sitcoms'
#The name of the wanted playlist in Plex
MY_PLAYLIST = 'Sitcoms - Reruns - Test'
#The name of the Library in Plex
LIBRARY_NAME = 'TV Shows'
#The Number of episdodes for the playlist is defined in plex_config, but can be overidden here. Change 0 to the number of episodes wanted in the playlist
NUMBER_OF_EP_OVERRIDE = 0
