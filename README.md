# spotify-always-discover-weekly

As a regular user of Spotify I take advantage of their discover weekly feature. Every week new songs suited to my tastes are put into a playlist and replaced the following week. I often forget to save songs from that playlist and dramatically lose them forever. Using Spotify's API this Python script takes your current discover weekly songs and adds them into a new playlist called 'Constantly Discovering Weekly'
I use Pythonanywhere.com to run this script for free once a week to solve this problem. The script gets an OAuth token from spotify, you must paste the url redirect into console after authorisation

## Dependencies
You must pip install 'spotipy' to use this script. This can be done in Pythonanywhere.com's bash console.
http://spotipy.readthedocs.io/en/latest/

## What to change
You need to change line 46 to replace your own unique playlist id for your Discover Weekly playlist. This can be found in the URL here: https://www.spotify.com/discoverweekly/
