#!/usr/bin/python3
""" Modules for DBstorage """
import os
from sqlalchemy import (create_engine)
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """ Class for the DB """
    __engine = None
    __session = None

    def __init__(self):
        """ attrs of storage """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv("HBNB_MYSQL_USER"),
                                              os.getenv("HBNB_MYSQL_PWD"),
                                              os.getenv("HBNB_MYSQL_HOST"),
                                              os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """ all objects of cls d = dict"""
        classes = [City, State]
        d = {}
        query = []

        if cls:
            query = self.__session.query(cls)
        else:
            for cls in classes:
                query += self.__session.query(cls)

        d = {type(value).__name__ + "." + value.id: value for value in query}
        return d

    def new(self, obj):
        """ add obj in the DB """
        if obj:
            self.__session.add(obj)

        if not obj:
            return

    def save(self):
        """ Commit in the DB """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create tables """
        Base.metadata.create_all(self.__engine)

        maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(maker)

        self.__session = Session()
