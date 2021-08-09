"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        primary_key=True,
                        autoincrement=True
                        )

    email = db.Column(db.String, nullable=False, unique=True) #nullable False default?

    password = db.Column(db.String(20), nullable=False)

     # ratings = a list of Rating objects

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Movie(db.Model):
    """ A movie """

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True
                        )
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

     # ratings = a list of Rating objects

    def __repr__(self):
        return f"<Movie movie_id = {self.movie_id} title = {self.title}>"

class Ratings(db.Model):
    """User ratings"""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer,
                        primary_key  = True,
                        autoincrement = True
                        )
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", backref = "ratings") #Why Movie? Which movie? Class or table? what is backref
    user = db.relationship ("User", backref = "ratings")
    
    # class Parent(Base):
    # __tablename__ = 'parent'
    # id = Column(Integer, primary_key=True)
    # children = relationship("Child", backref="parent")
    
    

    def __repr__(self):
        return f"<Rating rating_id = {self.rating_id} score = {self.score}>"

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

    db.drop_all()
    db.create_all()
    
    test_user = User(email = 'TestytestTest@poatato.mash', password = 'garlic')
    db.session.add(test_user)
    db.session.commit()

    test_movie = Movie(title = 'Fast and the Furriest', overview = 'Furry and Fast Muppets take over', release_date = datetime.now(), poster_path = 'www.imdb.com/fast+furriest')
    db.session.add(test_movie)
    db.session.commit()

    test_rating = Ratings(score=90, movie=test_movie, user=test_user)
    db.session.add(test_rating)
    db.session.commit()
