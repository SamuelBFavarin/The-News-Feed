import unittest
from datetime import datetime
import uuid


from app.main import db
from app.main.model.author import Author
from app.main.model.news import News

from app.test.base import BaseTestCase


class TestNewsModel(BaseTestCase):

    author_entity_id = None

    def setUp(self):
        db.create_all()
        db.session.commit()

        new_author = Author(
            public_id=str(uuid.uuid4()),
            name='samuelbfavarin',
            photo='https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            created_at=datetime.utcnow())

        self.author_entity_id = new_author.id

        db.session.add(new_author)
        db.session.commit()

    def test_create_news(self):

        news_data = {
            'public_id': str(uuid.uuid4()),
            'author_id': self.author_entity_id,
            'title': 'this is a title',
            'text': 'this is as text',
            'tag': 'TECH',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        _ = self.__create_news_entities(news_data)

        new_news = News.query.first()
        self.assertTrue(new_news.public_id == news_data['public_id'])
        self.assertTrue(new_news.author_id == news_data['author_id'])
        self.assertTrue(new_news.title == news_data['title'])
        self.assertTrue(new_news.text == news_data['text'])
        self.assertTrue(new_news.tag == news_data['tag'])
        self.assertTrue(new_news.photo == news_data['photo'])
        self.assertTrue(new_news.created_at == news_data['created_at'])

    def test_create_news_with_wrong_tag(self):

        news_data = {
            'public_id': str(uuid.uuid4()),
            'author_id': self.author_entity_id,
            'title': 'this is a title',
            'text': 'this is as text',
            'tag': 'WRONG',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        self.assertTrue(self.__create_news_entities(news_data) is False)

    def test_create_news_with_title_null(self):

        news_data = {
            'public_id': str(uuid.uuid4()),
            'author_id': self.author_entity_id,
            'title': None,
            'text': 'this is as text',
            'tag': 'WRONG',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        self.assertTrue(self.__create_news_entities(news_data) is False)

    def test_create_news_with_text_null(self):

        news_data = {
            'public_id': str(uuid.uuid4()),
            'author_id': self.author_entity_id,
            'title': 'this is a title',
            'text': None,
            'tag': 'WRONG',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        self.assertTrue(self.__create_news_entities(news_data) is False)

    def __create_news_entities(self, news):

        try:

            new_news = News(
                public_id=news['public_id'],
                author_id=news['author_id'],
                title=news['title'],
                text=news['text'],
                photo=news['photo'],
                tag=news['tag'],
                created_at=news['created_at']
            )

            db.session.add(new_news)
            db.session.commit()
            return new_news
        except:
            return False


if __name__ == '__main__':
    unittest.main()
