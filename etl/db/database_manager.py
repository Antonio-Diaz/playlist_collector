from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound

Base = declarative_base()

class DatabaseManager:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create(self, obj):
        self.session.add(obj)
        self.session.commit()

    def update(self, obj):
        self.session.commit()

    def delete(self, obj):
        self.session.delete(obj)
        self.session.commit()

    def get_by_id(self, cls, id):
        try:
            return self.session.query(cls).filter_by(id=id).one()
        except NoResultFound:
            return None

    def get_all(self, cls):
        return self.session.query(cls).all()

    def close(self):
        self.session.close()
