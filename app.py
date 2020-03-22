
# Задачи:

# 1. API для загрузки новости/текста/автора/даты для дальнейшего анализа
# 2. API для загрузки видео/трансформации в текст

import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister        
from resources.game import Game, GameList
from resources.school import School, SchoolList   # так добавляется Resource
from resources.turn import Turn, TurnList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'app'                          # should be long and secure
api = Api(app)


jwt = JWT(app, authenticate, identity)          # creates new endpoint /auth


api.add_resource(UserRegister, '/register')
api.add_resource(Game,         '/game/<string:name>')    # GET http://127.0.0.1:5000/game/ProtonMass
api.add_resource(GameList,     '/games')
api.add_resource(School,       '/school/<string:schoolName>')  # так добавляется Resource
api.add_resource(SchoolList,   '/schools')
api.add_resource(Turn,         '/turn/<string:turnName>')
api.add_resource(TurnList,     '/turns')


if __name__ == '__main__':        # запускаем только если этот файл запущен как главный
  from db import db               # если поставить наверх, будет циклический импорт
  db.init_app(app)
  app.run(port=5000, debug=True)


