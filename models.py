import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
"""Models for Blogly."""

db = SQLAlchemy()

#Models go below:
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    
    first_name = db.Column(db.String(50),
                     nullable = False,
                     unique = False)
    
    last_name = db.Column(db.String(50),
                          nullable = False,
                          unique = False)
    
    image_url = db.Column(db.Text,
                          nullable = False)
    
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Return full name of user"""

        return f"{self.first_name} {self.last_name}"
    
class Post(db.Model):
    """Blog Post"""

    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text,
                      nullable=False)
    content = db.Column(db.Text,
                        nullable = False)
    create_at = db.Column(db.DateTime, 
                          nullable = False,
                          default=datetime.datetime.now)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable = False)
    
    @property
    
    def format_date(self):
        """Return a formated date"""
        
        return self.create_at.strftime("%a %b %-d  %Y, %-I:%M %p")

def connect_db(app):
    """Connect db to Flask app"""

    db.app = app
    db.init_app(app)