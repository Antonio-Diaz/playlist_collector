import os

from dotenv import load_dotenv
from data_extraction.spotify_api import SpotifyAPI

load_dotenv()

class UserFeature(SpotifyAPI):
    
        def __init__(self):
            super().__init__(os.getenv('SPOTIFY_CLIENT_ID'), os.getenv('SPOTIFY_CLIENT_SECRET'), os.getenv('SPOTIFY_REDIRECT_URI'))
    
        def get_user_profile(self):
            endpoint = 'me'
            response = self.make_request('GET', endpoint)
            return response

if __name__ == '__main__':
    
    UserFeature = UserFeature()
    # Step 1: Obtain the authorization URL
    scope = 'user-read-private user-read-email'  # Specify the required scopes
    auth_url = UserFeature.get_authorization_url(scope)
    print('Authorization URL:', auth_url)
    
    # Step 2: User authorization
    # After the user grants permission, Spotify will redirect to the redirect_uri with an authorization code
    
    # Step 3: Retrieve access and refresh tokens
    authorization_code = input('Introduce code: ')  # Replace with the code obtained from the redirect URI
    tokens = UserFeature.request_tokens(authorization_code)
    access_token = tokens['access_token']
    refresh_token = tokens['refresh_token']
    UserFeature.set_access_token(access_token)
    
    # Step 4: Make authenticated requests
    user_profile = UserFeature.get_user_profile()
    print('User Profile:', user_profile['id'])
    
    # Step 5: Refresh access token
    # new_tokens = UserFeature.refresh_tokens(refresh_token)
    # new_access_token = new_tokens['access_token']
    
    # Step 6: Make authenticated requests using the new access token
    # UserFeature.set_access_token(new_access_token)
    # user_profile = UserFeature.get_user_profile()
    # print('User Profile:', user_profile)
    
    # Step 7: Revoke access token
    # UserFeature.revoke_token()
    
    # Step 8: Make authenticated requests using the revoked access token
    # user_profile = UserFeature.get_user_profile()
    # print('User Profile:', user_profile)
    

