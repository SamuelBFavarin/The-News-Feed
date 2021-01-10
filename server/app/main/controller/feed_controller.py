from flask import request
from flask_restplus import Resource
from ..util.dto import NewsDto
from ..util.decorator import token_required
from ..services.feed_service import list_news, save_news

api = NewsDto.api
_news = NewsDto.news


@api.route('/')
class News(Resource):
    @api.doc('list_of_registered_news')
    @api.param('tag', description='News tag to filter', type='string')
    @api.marshal_list_with(_news, envelope='data')
    def get(self):
        """List all news"""

        try:
            tag = request.args.get('tag')
        except:
            tag = None

        return list_news(tag)

    @ token_required
    @api.response(201, 'News successfully created.')
    @api.doc('create a news')
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    @api.expect(_news, validate=True)
    def post(self):
        """Creates a new News """
        data = request.json
        return save_news(data=data)
