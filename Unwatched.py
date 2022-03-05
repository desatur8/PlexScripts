# Update these:
#The name of the Collection of shows in Plex
COLLECTION_NAME = 'My Shows'
#The name of the wanted playlist in Plex
MY_PLAYLIST = 'My Shows'
#The name of the Library in Plex
LIBRARY_NAME = 'TV Shows'
#The Number of episdodes for the playlist is defined in plex_config, but can be overidden here. Change 0 to the number of episodes wanted in the playlist
NUMBER_OF_EP_OVERRIDE = 0

import os, operator, time, sys, datetime, re
import requests
import random
from plexapi.server import PlexServer
import configparser

#import settings
plex_config = configparser.ConfigParser()
plex_config.read("plex_config.ini")
baseurl = plex_config.get('plex_config', 'PLEX_URL')
token = plex_config.get('plex_config', 'PLEX_TOKEN')
NumberOfEpisodes = int(plex_config.get('plex_config', 'NUMBER_OF_SHOWS'))

plex = PlexServer(baseurl, token)
episode_list = []
final_playlist = []
tv_shows_section = plex.library.section(LIBRARY_NAME)

#CODE
#check if playlist exists, if it does, remove so that it can be repopulated
for playlist in plex.playlists():
  if playlist.title == MY_PLAYLIST:
     print('{} already exists. Deleting and rebuilding.'.format(MY_PLAYLIST))
     playlist.delete()

#populating shows from the given collection name
for collection in tv_shows_section.collection(COLLECTION_NAME):
  tv_show = collection.title
  current_season = 0
  all_seasons = plex.library.section(LIBRARY_NAME).get(tv_show).seasons()
  total_season = len(all_seasons)
  for i in range(total_season):
      all_eps = all_seasons[i].episodes()
      for episode in all_eps:
          if not episode.isWatched:
            i = total_season + 5
            episode_list += episode
            break
      else:
          continue
      break

random.shuffle(episode_list)

if(NUMBER_OF_EP_OVERRIDE > 0):
  final_playlist = episode_list[:NUMBER_OF_EP_OVERRIDE]
  print('Adding {} shows to playlist.'.format(len(final_playlist)))
  plex.createPlaylist(MY_PLAYLIST, items=final_playlist)
else:
  final_playlist = episode_list[:NumberOfEpisodes]
  print('Adding {} shows to playlist.'.format(len(final_playlist)))
  plex.createPlaylist(MY_PLAYLIST, items=final_playlist)


