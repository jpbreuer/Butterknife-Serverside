from flask import json
import requests
from urllib import quote
import keys

__author__ = 'nick'

API_MUSIXMATCH_BASE = 'http://api.musixmatch.com/ws/1.1/'

def get_lyrics(songname):
    search_results =  requests.get("{}{}?q_track={}&f_has_lyrics=1&apikey={}".format(
        API_MUSIXMATCH_BASE,
        "track.search",
        quote(songname),
        keys.musix
    )).json()

    try:
        query_song_id = search_results['message']['body']['track_list'][0]['track']['track_id']
    except:
        abort(404)

    lyrics = requests.get("{}{}?track_id={}&apikey={}".format(
        API_MUSIXMATCH_BASE,
        "track.lyrics.get",
        query_song_id,
        keys.musix
    )).json()['message']['body']['lyrics']

    lyrics['song_name'] = search_results['message']['body']['track_list'][0]['track']['track_name']

    return json.jsonify(lyrics)

def get_lyrics_artist(artist, songname):
    search_results =  requests.get("{}{}?q_track={}&q_artist={}&f_has_lyrics=1&apikey={}".format(
        API_MUSIXMATCH_BASE,
        "track.search",
        quote(songname),
        quote(artist),
        keys.musix
    )).json()

    try:
        query_song_id = search_results['message']['body']['track_list'][0]['track']['track_id']
    except:
        abort(404)

    lyrics = requests.get("{}{}?track_id={}&apikey={}".format(
        API_MUSIXMATCH_BASE,
        "track.lyrics.get",
        query_song_id,
        keys.musix
    )).json()['message']['body']['lyrics']

    lyrics['song_name'] = search_results['message']['body']['track_list'][0]['track']['track_name']


    return json.jsonify(lyrics)