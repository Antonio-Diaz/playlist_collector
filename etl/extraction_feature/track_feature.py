from pydantic import BaseModel

class Track(BaseModel):
    id: str
    name: str
    artists: list
    album: str
    duration_ms: int
    explicit: bool
    popularity: int
    
class TrackFeature:
    
    def __init__(self, raw_track):
        self.raw_track = raw_track
        
    def transform(self):
        temp = []
        for track in self.raw_track.get('items', []):
            temp.append(Track(
                id=track['track']['id'],
                name=track['track']['name'],
                artists=[artist['name'] for artist in track['track']['artists']],
                album=track['track']['album']['name'],
                duration_ms=track['track']['duration_ms'],
                explicit=track['track']['explicit'],
                popularity=track['track']['popularity'],
            ))
        return temp
    
    @property
    def serialize(self):
        return [track.dict() for track in self.transform()]