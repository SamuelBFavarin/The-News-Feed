import uuid
import datetime

from app.main import db
from app.main.model.news import News
from app.main.model.author import Author


def list_news(limit=12, tag_filter=None):
    """
       List all news in database
    """

    query = db.session.query(News)

    if tag_filter:
        query = query.filter_by(tag=tag_filter.upper())

    query = query.join(Author)

    query = query.with_entities(News.title.label('title'),
                                News.text.label('text'),
                                News.photo.label('photo'),
                                News.public_id.label('public_id'),
                                News.tag.label('tag'),
                                Author.name.label('author_name'),
                                Author.photo.label('author_photo'))

    query = query.order_by(db.desc(News.created_at))

    if limit:
        query = query.limit(limit)

    result = query.all()

    response = []
    for r in result:
        response.append({'title': r.title, 'text': r.text, 'photo': r.photo, 'public_id': r.public_id,
                         'tag': r.tag, 'author_name': r.author_name, 'author_photo': r.author_photo})

    return response


def create_news(news_data, author_id):
    """ 
        Create a news by parameter data.

        Parameters
        ----------
        data : dict
            The data to create a entity. The dict must have this structure:
            {
                'title': 'the news title',
                'text': 'the news content text',
                'tag': 'the news tag' (the value must be 'POLITICS', 'TECH', 'SCIENCE', 'SPORTS' or 'BUSINESS'),
                'photo': 'the news photo' (optional)
            } 

        author_id : int
            The author id entity 

        Raises
        ------
        Exception
            Not `title`, `text` or `tag` params in news dict
    """

    title = None
    text = None
    tag = None
    photo = None

    if 'title' not in news_data and 'text' not in news_data and 'tag' not in news_data:
        raise Exception('Not `title`, `text` or `tag` params in news dict')
    else:
        title = news_data['title']
        text = news_data['text']
        tag = news_data['tag']

    if 'photo' in news_data:
        photo = news_data['photo']

    new_news = News(
        public_id=str(uuid.uuid4()),
        author_id=author_id,
        title=title,
        text=text,
        photo=photo,
        tag=tag,
        created_at=datetime.datetime.utcnow()
    )

    db.session.add(new_news)
    db.session.commit()

    return new_news


def get_news(news_title):
    """ 
        Get news by news title.

        Parameters
        ----------
        news_title : str
            The news title to find the news
    """

    try:
        return News.query.filter_by(title=news_title).first()
    except:
        return False
