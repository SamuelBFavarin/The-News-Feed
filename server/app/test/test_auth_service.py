import unittest
from datetime import datetime
from dateutil.relativedelta import relativedelta
import secrets

from app.main import db
from app.main.model.token import Token
from app.main.services.auth_service import generate_token, is_valid_token

from app.test.base import BaseTestCase


class TestAuthService(BaseTestCase):

    def test_is_valid_token(self):

        # first token
        mock_token = Token(
            token=secrets.token_urlsafe(20),
            user='samuelbfavarin',
            email='favarin.dev@gmail.com',
            created_at=datetime.utcnow(),
            expire_at=datetime.utcnow() + relativedelta(years=1))

        # second token, with wrong expire_at date
        mock_token_wrong_expire_at = Token(
            token=secrets.token_urlsafe(20),
            user='samuelbfavarin2',
            email='favarin.dev2@gmail.com',
            created_at=datetime.utcnow(),
            expire_at=datetime.utcnow() + relativedelta(years=-1))

        db.session.add(mock_token)
        db.session.add(mock_token_wrong_expire_at)
        db.session.commit()

        self.assertTrue(is_valid_token(mock_token.token) is True)
        self.assertTrue(is_valid_token(mock_token.token + 'blabla') is False)
        self.assertTrue(is_valid_token(
            mock_token_wrong_expire_at.token) is False)

    def test_generate_token(self):

        data = {
            'user': 'samuelbf',
            'email': 'samuelbfavarin@hotmail.com'
        }

        response = generate_token(data)

        self.assertTrue('token' in response and response['token'] is not None)
        self.assertTrue('user' in response and response['user'] == 'samuelbf')
        self.assertTrue(
            'email' in response and response['email'] == 'samuelbfavarin@hotmail.com')


if __name__ == '__main__':
    unittest.main()
