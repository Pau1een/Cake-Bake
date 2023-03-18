from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String, nullable=True)

    favorites_recipes = db.relationship("Favorite_recipe", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} fname={self.fname} email={self.email}>"


class Favorite_recipe(db.Model):

    __tablename__ = "favorite_recipes"

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True)
    favorite_name = db.Column(db.String)
    favorite_img = db.Column(db.String)
    favorite_ingredients = db.Column(db.String)
    favorite_source = db.Column(db.String)
    recipe_link = db.Column(db.String)
    review = db.Column(db.Text)

    user = db.relationship("User", back_populates="favorites_recipes")

    def __repr__(self):
        return f"<Favorite recipe id={self.favorite_id} by user_id={self.user_id} >"



def connect_to_db(flask_app, db_uri="postgresql:///cake", echo=False):
    """Connect to database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app


    connect_to_db(app)