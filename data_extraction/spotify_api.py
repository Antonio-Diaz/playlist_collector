import os
import requests
from urllib.parse import urlencode

class SpotifyAPI:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.base_url = 'https://api.spotify.com/v1/'
        self.access_token = None

    def get_authorization_url(self, scope, state=None):
        authorize_url = 'https://accounts.spotify.com/authorize'
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'scope': scope
        }

        if state:
            params['state'] = state

        return authorize_url + '?' + urlencode(params)

    def request_tokens(self, code):
        token_url = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve tokens')

    def refresh_tokens(self, refresh_token):
        token_url = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to refresh tokens')

    def set_access_token(self, access_token):
        self.access_token = access_token

    def make_request(self, method, endpoint, params=None, headers=None):
        if self.access_token is None:
            raise Exception('Access token not set')

        url = self.base_url + endpoint
        headers = headers or {}
        headers['Authorization'] = f'Bearer {self.access_token}'

        response = requests.request(method, url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Request failed with status code {response.status_code}')

    # Add more methods for accessing user data or other endpoints

