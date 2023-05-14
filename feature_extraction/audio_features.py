import os

from dotenv import load_dotenv
from data_extraction.spotify_api import SpotifyAPI

load_dotenv()


class AudioFeatures(SpotifyAPI):

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

if __name__ == '__main__':
    audio_features = AudioFeatures()
    # Step 1: Obtain the authorization URL
    scope = 'user-read-private user-read-email'  # Specify the required scopes
    auth_url = audio_features.get_authorization_url(scope)
    print('Authorization URL:', auth_url)

    # Step 2: User authorization
    # After the user grants permission, Spotify will redirect to the redirect_uri with an authorization code

    # Step 3: Retrieve access and refresh tokens
    authorization_code = input('Introduce code: ')  # Replace with the code obtained from the redirect URI
    tokens = audio_features.request_tokens(authorization_code)
    access_token = tokens['access_token']
    refresh_token = tokens['refresh_token']
    audio_features.set_access_token(access_token)

    # Step 4: Make authenticated requests
    user_profile = audio_features.get_user_profile()
    print('User Profile:', user_profile)
