from . import db

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    increment = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.Integer)
    user_login = db.Column(db.String(50))
    user_name = db.Column(db.String(50))
    user_lang = db.Column(db.String(50))
    user_balance = db.Column(db.BigInteger)
    user_hold = db.Column(db.BigInteger)
    user_refill = db.Column(db.Integer)
    user_date = db.Column(db.DateTime)
    user_unix = db.Column(db.Integer)
    user_city = db.Column(db.String(50))
    user_address = db.Column(db.String(50))
    user_phone = db.Column(db.String(50))
    user_geocode = db.Column(db.String(50))
    user_role = db.Column(db.String(50))
    user_city_id = db.Column(db.BigInteger)
    promocode = db.Column(db.String(50))
    free_delivery_point = db.Column(db.BigInteger)
    delivery_rate = db.Column(db.BigInteger)
    new_prod_notify = db.Column(db.BigInteger)

    def __repr__(self):
        return f'<User {self.user_name}>'
