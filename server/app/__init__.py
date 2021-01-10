from flask_restplus import Api
from flask import Blueprint

from .main.controller.feed_controller import api as news
from .main.controller.auth_controller import api as auth
from .main.controller.webscraping_controller import api as webscraping


blueprint = Blueprint('api', __name__)


api = Api(blueprint,
          title='FEED NEWS FLASK RESTPLUS API',
          version='1.0',
          description='A awesome feed news api'
          )

api.add_namespace(news, path='/news')
api.add_namespace(auth, path='/auth')
api.add_namespace(webscraping, path='/webscraping')
