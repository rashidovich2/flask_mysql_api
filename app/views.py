from . import api
from .models import User
from .schemas import UserSchema


@app.route('/users')
async def get_users():
    users = await User.query.gino.all()
    user_schema = UserSchema(many=True)
    result = user_schema.dump(users)
    return jsonify(result)

api.add_resource(UserResource, '/users')