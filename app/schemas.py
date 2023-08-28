from . import ma
from .models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    increment = ma.auto_field()
    user_id = ma.auto_field()
    user_login = ma.auto_field()
    user_name = ma.auto_field()
    user_lang = ma.auto_field()
    user_balance = ma.auto_field()
    user_hold = ma.auto_field()
    user_refill = ma.auto_field()
    user_date = ma.auto_field()
    user_unix = ma.auto_field()
    user_city = ma.auto_field()
    user_address = ma.auto_field()
    user_phone = ma.auto_field()
    user_geocode = ma.auto_field()
    user_role = ma.auto_field()
    user_city_id = ma.auto_field()
    promocode = ma.auto_field()
    free_delivery_point = ma.auto_field()
    delivery_rate = ma.auto_field()
    new_prod_notify = ma.auto_field()
