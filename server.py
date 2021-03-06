#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, render_template, jsonify

# Spotify API wrapper, documentation here: http://spotipy.readthedocs.io/en/latest/
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Authenticate with Spotify using the Client Credentials flow
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/')
def homepage():
    # Displays homepage
    return render_template('index.html')
  
@app.route('/new_releases', methods=['GET'])
def new_releases():
  
    # Use the country from the query parameters, if provided
    if 'country' in request.args:
        country = request.args['country']
    else:
        country = 'SE'
    
    # Send request to the Spotify API
    new_releases = sp.new_releases(country=country, limit=20, offset=0)
    
    # Return the list of new releases
    return jsonify(new_releases)
  
@app.route('/song_search', methods=['GET'])
def song_search():
  

  if 'song' in request.args:
      song = request.args['song']
  else:
      song = 'Not Valid Song'
      
      song_search = sp.new_releases(song=song, limit=5, offset=0)
      
      return jsonify(song_search)

if __name__ == '__main__':
    app.run()
    