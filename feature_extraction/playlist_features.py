import os

from dotenv import load_dotenv

import data_extraction.spotify_api as spotify_api

load_dotenv()

class PlaylistFeatures(spotify_api.SpotifyAPI):
    
        def __init__(self):
            super().__init__(os.getenv('SPOTIFY_CLIENT_ID'), os.getenv('SPOTIFY_CLIENT_SECRET'), os.getenv('SPOTIFY_REDIRECT_URI'))
    
        def get_audio_features(self, track_id):
            endpoint = f'audio-features/{track_id}'
            response = self.make_request(endpoint)
            return response
    
        def get_audio_features_multiple_tracks(self, track_ids):
            endpoint = 'audio-features'
            params = {'ids': ','.join(track_ids)}
            response = self.make_request(endpoint, params=params)
            return response
        
        def get_user_playlists(self, user_id):
            endpoint = f'users/{user_id}/playlists'
            response = self.make_request(endpoint)
            return response
        
    