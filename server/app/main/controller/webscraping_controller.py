from flask import request
from flask_restplus import Resource

from ..util.dto import WebScrapingDto

from ..util.decorator import token_required
from ..services.webscraping_service import generate_news

api = WebScrapingDto.api


@api.route('/')
class WebScraping(Resource):

    @ token_required
    @api.doc('api to generate news')
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
    def post(self):
        """Generate news """
        return generate_news()
