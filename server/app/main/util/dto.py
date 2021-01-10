from flask_restplus import Namespace, fields


class NewsDto:
    api = Namespace('news', description='news related operations')
    news = api.model('news', {
        'title': fields.String(required=True, description='news title'),
        'text': fields.String(required=True, description='news text'),
        'tag': fields.String(required=True, description='news tag'),
        'public_id': fields.String(readonly=True, description='user Identifier'),
        'photo': fields.String(required=False, description='news photo'),
        'author_name': fields.String(required=True, description='author news name'),
        'author_photo': fields.String(required=False, description='author news photo')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    auth = api.model('auth', {
        'token': fields.String(readonly=True, description='The valid token generated'),
        'user': fields.String(required=True, description='The api owner user '),
        'email': fields.String(required=True, description='The api owner email '),
        'expire_at': fields.DateTime(readonly=True, description='The expire token date')
    })


class WebScrapingDto:
    api = Namespace(
        'webscraping', description='webscraping related operations')
