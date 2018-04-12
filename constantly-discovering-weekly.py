import sys
import spotipy
import pprint
import os
import subprocess
import spotipy.util as util

# Space seperated permissions to request from Spotify
scope = "user-library-read playlist-modify-public playlist-modify-private"

# Checks if the 'Constantly Discovering Weekly' playlist already exists
def does_playlist_exist(username,sp):
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'] == 'Constantly Discovering Weekly':
            return True
    return False

# Creates a playlist named 'Constantly Discovering Weekly'
def create_playlist(username, sp):
    sp.trace = False
    playlist_name = 'Constantly Discovering Weekly'
    playlist_description = 'A collection of all your discover weeklys'
    sp.user_playlist_create(username, playlist_name, True)  # True indicates it is a public playlist

# Returns id of 'Constantly Discovering Weekly' playlist
def get_playlist_id(username,sp):
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'] == 'Constantly Discovering Weekly':
            pprint.pprint(playlist)
            return playlist['id']

# Gets the track ids in this weeks regular Discover Weekly Playlist
def get_track_ids(tracks):
    track_ids=[]
    for i, item in enumerate(tracks['items']):
        track = item['track']
        track_ids.append(track['id'])
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], # Print the songs added in console
            track['name']))
    return track_ids

# Get the playlist id of the regular Discover Weekly playlist
def add_new_songs(username,sp,playlist_id):
    results = sp.user_playlist('spotify','37i9dQZEVXcH8BYBRPSV2S')
    tracks = results['tracks']
    track_ids = get_track_ids(tracks)
    sp.user_playlist_add_tracks(username,playlist_id,track_ids)

def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()

    # Authorisation token
    token = util.prompt_for_user_token(username, scope, client_id='a6776200ad364d2b9769641366361baf',
                                       client_secret='201fe92a3ef54dd486284ebfdbea555c',
                                       redirect_uri='https://bobbymcgonigle.github.io')

    # Once token is okay, check if playlist exists already, create if neccessary and add songs
    if token:
        sp = spotipy.Spotify(auth=token)
        if does_playlist_exist(username,sp) == False:
            create_playlist(username, sp)
            add_new_songs('spotify', sp, get_playlist_id(username,sp))
            print('Created new playlist and added this weeks Discover Weekly Songs')
        else:
            playlist_id = get_playlist_id(username,sp)
            print('Playlist exists already with id: ' + playlist_id)
            print('Adding the following songs:')
            add_new_songs('spotify', sp, playlist_id)
        sp.trace = False
    else:
        print("Can't get token for", username)
main()