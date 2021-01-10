import unittest
from datetime import datetime
import uuid

from app.main import db

from app.main.model.author import Author
from app.main.model.news import News

from app.main.services.news_service import list_news, create_news, get_news

from app.test.base import BaseTestCase


class TestNewsService(BaseTestCase):

    author_entity_id = None
    news_data1 = None
    news_data2 = None

    def setUp(self):
        db.create_all()
        db.session.commit()

        new_author = Author(
            public_id=str(uuid.uuid4()),
            name='samuelbfavarin37',
            photo='https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            created_at=datetime.utcnow())

        db.session.add(new_author)
        db.session.commit()

        self.author_entity_id = new_author.id

        self.news_data1 = {
            'public_id': str(uuid.uuid4()),
            'author_id': self.author_entity_id,
            'title': 'this is a title',
            'text': 'this is as text',
            'tag': 'TECH',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        self.news_data2 = {
            'public_id': str(uuid.uuid4()),
            'author_id': self.author_entity_id,
            'title': 'this is a title2',
            'text': 'this is as text2',
            'tag': 'POLITICS',
            'photo': 'https://media-exp1.licdn.com/dms/image/C5603AQFz87ETwKMgLw/profile-displayphoto-shrink_200_200/0/1582764311959?e=1614816000&v=beta&t=KrCsZGGkBYWVbGZhfeuZQAxbYho83ZlxUkGLaG8Kmek',
            'created_at': datetime.utcnow()
        }

        self.__create_news_entities(self.news_data1)
        self.__create_news_entities(self.news_data2)

    def test_get_news(self):

        news = get_news(self.news_data1['title'])
        self.assertTrue(news.title == self.news_data1['title'])
        self.assertTrue(news.title != self.news_data2['title'])

        news = get_news('')
        self.assertTrue(news is None)

    def test_list_all_news(self):

        all_news = list_news()

        self.assertTrue(len(all_news) == 2)
        self.assertTrue(all_news[0]['title'] == self.news_data2['title'])
        self.assertTrue(all_news[1]['title'] == self.news_data1['title'])

    def test_list_with_filter_news(self):

        # filter by tech tag
        all_news = list_news(tag_filter='TECH')
        self.assertTrue(len(all_news) == 1)
        self.assertTrue(all_news[0]['title'] == self.news_data1['title'])
        self.assertTrue(all_news[0]['tag'] == 'TECH')

        # filter by politics tag
        all_news = list_news(tag_filter='POLITICS')
        self.assertTrue(len(all_news) == 1)
        self.assertTrue(all_news[0]['title'] == self.news_data2['title'])
        self.assertTrue(all_news[0]['tag'] == 'POLITICS')

        # filter by science tag (tag without values)
        all_news = list_news(tag_filter='SCIENCE')
        self.assertTrue(len(all_news) == 0)

    def test_create_news(self):

        # create a corret news
        news_data = {
            'title': 'this is a title',
            'text': 'this is a text',
            'photo': 'www.photo.com/thisisaphotourl.jpg',
            'tag': 'TECH'
        }
        result = create_news(news_data, self.author_entity_id)
        self.assertTrue(result.title == news_data['title'])
        self.assertTrue(result.text == news_data['text'])
        self.assertTrue(result.photo == news_data['photo'])
        self.assertTrue(result.tag == news_data['tag'])

        # create a news without a valid tag
        news_data = {
            'title': 'this is a title',
            'text': 'this is a text',
            'photo': 'www.photo.com/thisisaphotourl.jpg',
            'tag': 'WRONG'
        }
        try:
            create_news(news_data, self.author_entity_id)
            error = False
        except:
            error = True

        self.assertTrue(error is True)

        # create a news missing require attributes a valid tag
        news_data = {
            'tag': 'TECH'
        }
        try:
            create_news(news_data, self.author_entity_id)
            error = False
        except:
            error = True
        self.assertTrue(error is True)

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
