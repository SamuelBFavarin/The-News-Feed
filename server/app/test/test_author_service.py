import unittest
from datetime import datetime
import uuid

from app.main import db
from app.main.model.author import Author
from app.main.services.author_service import get_author, create_author

from app.test.base import BaseTestCase


class TestAuthorService(BaseTestCase):

    def test_get_author(self):

        author = Author(
            public_id=str(uuid.uuid4()),
            name='Samuel Favarin',
            photo='https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            created_at=datetime.utcnow())

        db.session.add(author)
        db.session.commit()

        result = get_author('Samuel Favarin')

        self.assertTrue(result.name == author.name)
        self.assertTrue(result.photo == author.photo)
        self.assertTrue(result.public_id == author.public_id)
        self.assertTrue(result.created_at == author.created_at)

    def test_create_author(self):

        author_data = {
            'name': 'Samuel B Favarin',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek'
        }

        author_created = create_author(author_data)

        self.assertTrue(author_data['name'] == author_created.name)
        self.assertTrue(author_data['photo'] == author_created.photo)

        author_data = {
            'name': 'Samuel B Favarin 2'
        }

        author_created = create_author(author_data)
        self.assertTrue(author_data['name'] == author_created.name)


if __name__ == '__main__':
    unittest.main()
