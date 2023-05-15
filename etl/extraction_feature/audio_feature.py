from pydantic import BaseModel

class AudioFeature(BaseModel):
    id: str
    danceability: float
    energy: float
    key: int
    loudness: float
    mode: int
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration_ms: int
    time_signature: int

class AudioFeatureFeature:
    
    def __init__(self, audio_feature):
        self.audio_feature = audio_feature
    
    def transform(self):
        return [
            AudioFeature(
                id=audio_feature['id'],
                danceability=audio_feature['danceability'],
                energy=audio_feature['energy'],
                key=audio_feature['key'],
                loudness=audio_feature['loudness'],
                mode=audio_feature['mode'],
                speechiness=audio_feature['speechiness'],
                acousticness=audio_feature['acousticness'],
                instrumentalness=audio_feature['instrumentalness'],
                liveness=audio_feature['liveness'],
                valence=audio_feature['valence'],
                tempo=audio_feature['tempo'],
                duration_ms=audio_feature['duration_ms'],
                time_signature=audio_feature['time_signature']
            )
            for audio_feature in self.audio_feature.get('audio_features', [])
        ]

    @property
    def serialize(self):
        return [audio_feature.dict() for audio_feature in self.transform()]
    
    @property
    def get_ids(self):
        return [audio_feature['id'] for audio_feature in self.audio_feature.get('audio_features', [])]
    
    @property
    def get_audio_features(self):
        return [audio_feature for audio_feature in self.audio_feature.get('audio_features', [])]
    
    @property
    def get_audio_features_mean(self):
        return {
            'danceability': sum([audio_feature['danceability'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'energy': sum([audio_feature['energy'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'key': sum([audio_feature['key'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'loudness': sum([audio_feature['loudness'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'mode': sum([audio_feature['mode'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'speechiness': sum([audio_feature['speechiness'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'acousticness': sum([audio_feature['acousticness'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'instrumentalness': sum([audio_feature['instrumentalness'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'liveness': sum([audio_feature['liveness'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'valence': sum([audio_feature['valence'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'tempo': sum([audio_feature['tempo'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'duration_ms': sum([audio_feature['duration_ms'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', [])),
            'time_signature': sum([audio_feature['time_signature'] for audio_feature in self.audio_feature.get('audio_features', [])]) / len(self.audio_feature.get('audio_features', []))
        }