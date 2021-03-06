import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import StoreList, Store 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') ##, 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = 'jim'



jwt = JWT(app, authenticate, identity)


api.add_resource(Store, '/store/<string:name>')  
api.add_resource(Item, '/item/<string:name>')  
api.add_resource(ItemList, '/items')  
api.add_resource(StoreList, '/stores')  
api.add_resource(UserRegister, '/register')  

if __name__ == '__main__':  ## if app.py is imported this will NOT run !!
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
