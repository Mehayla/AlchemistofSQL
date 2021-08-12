"""CRUD operations."""

from model import db, User, Movie, Ratings, connect_to_db
from datetime import datetime


def create_user(email, password):
    """Create and return a new user."""

    user = User(email = email, password = password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title = title, overview = overview, release_date = release_date, poster_path = poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def create_rating(user, movie, score):
    """Creates and manifests a rating with movie/user relations"""
    
    rating = Ratings(user = user, movie = movie, score = score)
    
    db.session.add(rating)
    db.session.commit()
    
    return rating
    # Doesn't like one of the parameters in Ratings - 
    # Error is AttributeError: 'str' object has no attribute '_sa_instance_state'
    
    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)