from flask_restful import Resource
from .models import User
from .schemas import UserSchema


class UserResource(Resource):
    def get(self):
        return get_users()
