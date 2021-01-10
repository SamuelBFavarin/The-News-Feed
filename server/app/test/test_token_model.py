import unittest
from datetime import datetime
from dateutil.relativedelta import relativedelta
import secrets

from app.main import db
from app.main.model.token import Token
from app.test.base import BaseTestCase


class TestTokenModel(BaseTestCase):

    def test_create_token(self):

        token_data = {
            'secret_token_generate': secrets.token_urlsafe(20),
            'user': 'samuelbfavarin',
            'email': 'favarin.dev@gmail.com',
            'created_at': datetime.utcnow(),
            'expire_at': datetime.utcnow() + relativedelta(years=1)
        }

        _ = self.__create_token_entities(token_data)

        new_user = Token.query.first()

        self.assertTrue(new_user.token == token_data['secret_token_generate'])
        self.assertTrue(new_user.user == token_data['user'])
        self.assertTrue(new_user.email == token_data['email'])
        self.assertTrue(new_user.created_at == token_data['created_at'])
        self.assertTrue(new_user.expire_at == token_data['expire_at'])

    def test_create_token_with_user_null(self):

        token_data = {
            'secret_token_generate': secrets.token_urlsafe(20),
            'user': None,
            'email': 'favarin.dev@gmail.com',
            'created_at': datetime.utcnow(),
            'expire_at': datetime.utcnow() + relativedelta(years=1)
        }

        self.assertTrue(self.__create_token_entities(token_data) is False)

    def test_create_token_with_email_null(self):

        token_data = {
            'secret_token_generate': secrets.token_urlsafe(20),
            'user': 'samuelbfavarin',
            'email': None,
            'created_at': datetime.utcnow(),
            'expire_at': datetime.utcnow() + relativedelta(years=1)
        }

        self.assertTrue(self.__create_token_entities(token_data) is False)

    def test_create_token_with_created_at_null(self):

        token_data = {
            'secret_token_generate': secrets.token_urlsafe(20),
            'user': 'samuelbfavarin',
            'email': 'favarin.dev@gmail.com',
            'created_at': None,
            'expire_at': datetime.utcnow() + relativedelta(years=1)
        }

        self.assertTrue(self.__create_token_entities(token_data) is False)

    def test_create_token_with_expire_at_null(self):

        token_data = {
            'secret_token_generate': secrets.token_urlsafe(20),
            'user': 'samuelbfavarin',
            'email': 'favarin.dev@gmail.com',
            'created_at': datetime.utcnow(),
            'expire_at': None
        }

        self.assertTrue(self.__create_token_entities(token_data) is False)

    def __create_token_entities(self, token):
        new_token = Token(
            token=token['secret_token_generate'],
            user=token['user'],
            email=token['email'],
            created_at=token['created_at'],
            expire_at=token['expire_at'])

        try:
            db.session.add(new_token)
            db.session.commit()
            return new_token
        except:
            return False


if __name__ == '__main__':
    unittest.main()
