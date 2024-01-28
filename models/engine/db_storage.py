#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """create engine"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        url = f'mysql+mysqldb://{user}:{password}@{host}/{db_name}'
        self.__engine = create_engine(url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        dictionary = {}
        if cls:
            res = self.__session.query(cls).all()
            for obj in res:
                key = f'{obj.__class__.__name__}.{obj.id}'
                dictionary[key] = obj
        else:
            classes = [State, City, Place, User, Amenity, Review]
            for cls in classes:
                res = self.__session.query(cls).all()
                for obj in res:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delte(self, obj=None):
        """ delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and the current session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
