from config.dbconfig import db
from models.user import User

from sqlalchemy import select

from config.appconfig import create_app

MP = create_app()

with MP.app_context():
    stm = select(User).order_by(User.user_id)
    user_query = db.session.execute(stm).all()
    print(user_query)

