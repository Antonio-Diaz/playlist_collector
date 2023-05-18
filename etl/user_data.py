import os
from dotenv import load_dotenv

from extraction_feature.user_feature import UserFeature
from extraction_feature.playlist_feature import PlaylistFeature
from extraction_feature.track_feature import TrackFeature
from extraction_feature.audio_feature import AudioFeatureFeature

from spotify_api.spotify_api import SpotifyAPI
load_dotenv()

class UserData:
    
    def __init__(self) -> None:
        self.spotify_api = SpotifyAPI(client_id=os.getenv('SPOTIFY_CLIENT_ID'), client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'), redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'))
        
    def get_user_profile(self):
        endpoint = 'me'
        params = {
            'scope': 'user-read-private user-read-email'
        }
        response = self.spotify_api.make_request('GET', endpoint)
        return response
    
    def get_user_playlists(self):
        endpoint = f'me/playlists'
        params = {
            'scope': 'playlist-read-private'
        }
        response = self.spotify_api.make_request('GET', endpoint, params)
        # convert dict to json
        return response
    
    def get_tracks_from_playlist(self, playlist_id):
        endpoint = f'playlists/{playlist_id}/tracks'
        params = {
            'scope': 'playlist-read-private playlist-read-collaborative'
        }
        response = self.spotify_api.make_request('GET', endpoint, params)
        # convert dict to json
        return response
    
    def get_audio_features_from_track(self, tracks_id):
        endpoint = f'audio-features?ids={tracks_id}'
        params = {
            'scope': 'user-read-private user-read-email'
        }
        response = self.spotify_api.make_request('GET', endpoint, params)
        # convert dict to json
        return response
          
if __name__ == '__main__':
    user_data = UserData()
    auth_url = user_data.spotify_api.get_authorization_url()
    print('Authorization URL:', auth_url)
    
    authorization_code = input('Introduce code: ')
    tokens = user_data.spotify_api.request_tokens(authorization_code)
    access_token = tokens['access_token']
    refresh_token = tokens['refresh_token']
    user_data.spotify_api.set_access_token(access_token)
    
    user_profile = user_data.get_user_profile()
    transform_user_profile = UserFeature(user_profile).serialize
    # print('User Profile:', transform_user_profile)
    
    user_playlists = user_data.get_user_playlists()
    transform_ids_playlist = PlaylistFeature(user_playlists).get_ids
    # print('User Playlists:', transform_ids_playlist)
    
    for id in transform_ids_playlist:
        raw_data_tracks = user_data.get_tracks_from_playlist(id)
        transform_tracks = TrackFeature(raw_data_tracks).serialize

        tracks_id = ','.join([track['id'] for track in transform_tracks])
        raw_data_audio_features = user_data.get_audio_features_from_track(tracks_id)
        transform_audio_features = AudioFeatureFeature(raw_data_audio_features).serialize
        print('Audio Features:', transform_audio_features)
    
    