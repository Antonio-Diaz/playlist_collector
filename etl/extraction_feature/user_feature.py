from pydantic import BaseModel

class User(BaseModel):
    id: str
    display_name: str
    email: str
    country: str
    product: str
    followers: int
    images: list

class UserFeature:
    
    def __init__(self, user):
        self.user = user
    
    def transform(self):
        return User(
            id=self.user['id'],
            display_name=self.user['display_name'],
            email=self.user['email'],
            country=self.user['country'],
            product=self.user['product'],
            followers=self.user['followers']['total'],
            images=self.user['images']
        )
    
    @property
    def serialize(self):
        return self.transform().dict()
    
    