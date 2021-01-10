import unittest
from datetime import datetime
import uuid


from app.main import db
from app.main.model.author import Author
from app.test.base import BaseTestCase


class TestAuthorModel(BaseTestCase):

    def test_create_author(self):

        author_data = {
            'public_id': str(uuid.uuid4()),
            'name': 'samuelbfavarin',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        _ = self.__create_author_entities(author_data)

        new_author = Author.query.first()
        self.assertTrue(new_author.public_id == author_data['public_id'])
        self.assertTrue(new_author.name == author_data['name'])
        self.assertTrue(new_author.photo == author_data['photo'])
        self.assertTrue(new_author.created_at == author_data['created_at'])

    def test_create_author_with_name_null(self):

        author_data = {
            'public_id': str(uuid.uuid4()),
            'name': None,
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        self.assertTrue(self.__create_author_entities(author_data) is False)

    def test_create_author_with_created_at_null(self):

        author_data = {
            'public_id': str(uuid.uuid4()),
            'name': 'Samuel Favarin',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': None
        }

        self.assertTrue(self.__create_author_entities(author_data) is False)

    def __create_author_entities(self, author):
        new_author = Author(
            public_id=author['public_id'],
            name=author['name'],
            photo=author['photo'],
            created_at=author['created_at'])

        try:
            db.session.add(new_author)
            db.session.commit()
            return new_author
        except:
            return False


if __name__ == '__main__':
    unittest.main()
