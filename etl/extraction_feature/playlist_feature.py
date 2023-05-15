from pydantic import BaseModel

class Playlist(BaseModel):
    id: str
    name: str
    description: str
    owner: str
    public: bool
    collaborative: bool

class PlaylistFeature:
    def __init__(self, playlists):
        self.playlists = playlists
    
    def transform(self):
        return [
            Playlist(
                id=playlist['id'],
                name=playlist['name'],
                description=playlist['description'],
                owner=playlist['owner']['display_name'],
                public=playlist['public'],
                collaborative=playlist['collaborative']
            )
            for playlist in self.playlists.get('items', [])
        ]
    
    @property
    def serialize(self):
        return [playlist.dict() for playlist in self.transform()]
    
    @property
    def get_ids(self):
        return [playlist['id'] for playlist in self.playlists.get('items', [])]
