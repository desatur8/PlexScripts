#Update these:
#Add shows by name OR a already defined collection
#If you want to use shows by name, type out shows name seperated by a , and change Collection name to COLLECTION_NAME = 0
#SHOWS_TO_ADD = 'The Big Bang Theory,Gary Unmarried,Two and a half men,3rd rock from the sun,scrubs'
SHOWS_TO_ADD = 'The Big Bang Theory,Gary Unmarried,Two and a half men,3rd rock from the sun,scrubs,rules of engagement'
COLLECTION_NAME = 'Sitcoms'
#The name of the wanted playlist in Plex
MY_PLAYLIST = 'Sitcoms - Reruns - Test'
#The name of the Library in Plex
LIBRARY_NAME = 'TV Shows'
#The Number of episdodes for the playlist is defined in plex_config, but can be overidden here. Change 0 to the number of episodes wanted in the playlist
NUMBER_OF_EP_OVERRIDE = 0


import os, operator, time, sys, datetime, re
import requests
import random
from plexapi.server import PlexServer
import configparser
from datetime import date

# Leave all this alone!

#import settings
plex_config = configparser.ConfigParser()
plex_config.read("plex_config.ini")
baseurl = plex_config.get('plex_config', 'PLEX_URL')
token = plex_config.get('plex_config', 'PLEX_TOKEN')
days = int(plex_config.get('plex_config', 'NUMBER_OF_DAYS_TO_NOT_RERUN'))
NumberOfEpisodes = int(plex_config.get('plex_config', 'NUMBER_OF_SHOWS'))
NumberOfRepeats = int(plex_config.get('plex_config', 'NUMBER_OF_REPEATS'))
NumberOfEpAlreadyAdded = 0

plex = PlexServer(baseurl, token)
episode_list = []
episode_list_five = []
tv_shows_section = plex.library.section(LIBRARY_NAME)

old_episodes_playlist = []

TODAY = date.today()

if(COLLECTION_NAME == 0):
    print('using show name')
    # delete the playlist if it already exists
    for playlist in plex.playlists():
        if playlist.title == MY_PLAYLIST:
            print('{} already exists. Deleting and rebuilding.'.format(MY_PLAYLIST))
            playlist.delete()

    tv_shows = SHOWS_TO_ADD.split(',')

    for show in tv_shows:
        NumberOfEpAlreadyAdded = 0
        plex_current_show = plex.library.section(LIBRARY_NAME).get(show)
        for episode in plex_current_show.episodes():
            if not episode.lastViewedAt:
                old_episodes_playlist.append(episode)
            else:
                days_since_played = (TODAY - episode.lastViewedAt.date()).days
            if days_since_played > days:
                old_episodes_playlist.append(episode)
else:
    # delete the playlist if it already exists
    for playlist in plex.playlists():
        if playlist.title == MY_PLAYLIST:
            print('{} already exists. Deleting and rebuilding.'.format(MY_PLAYLIST))
            playlist.delete()

    for collection in tv_shows_section.collection(COLLECTION_NAME):
        tv_shows = collection.title  
        plex_current_show = plex.library.section(LIBRARY_NAME).get(tv_shows)
        for episode in plex_current_show.episodes():
            if not episode.lastViewedAt:
                old_episodes_playlist.append(episode)
            else:
                days_since_played = (TODAY - episode.lastViewedAt.date()).days
            if days_since_played > days:
                old_episodes_playlist.append(episode)
    
#shuffle the playlist
random.shuffle(old_episodes_playlist)

#determine how many episodes to add and create the playlist
if(NUMBER_OF_EP_OVERRIDE > 0):
    final_playlist = old_episodes_playlist[:NUMBER_OF_EP_OVERRIDE]
    print('Adding {} shows to playlist.'.format(len(final_playlist)))
    plex.createPlaylist(MY_PLAYLIST, items=final_playlist)
else:
    final_playlist = old_episodes_playlist[:NumberOfEpisodes]
    print('Adding {} shows to playlist.'.format(len(final_playlist)))
    plex.createPlaylist(MY_PLAYLIST, items=final_playlist)




