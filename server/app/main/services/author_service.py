import uuid
import datetime

from app.main import db
from app.main.model.author import Author


def get_author(search_data, get_by_attribute="name"):
    """
        Find a author by parameter data.

        If the argument `get_by_attribute` isn't passed in, the entity will be find by author name

        Parameters
        ----------
        search_data : str
            The data to find a entity 

        get_by_attribute : str
            attribute used to find the entity (default is ` name `)

        Raises
        ------
        Exception
            If invalid value is sended in `get_by_attribute` params
    """

    author = False

    if get_by_attribute == "name":
        author = Author.query.filter_by(name=search_data).first()

    elif get_by_attribute == "public_id":
        author = Author.query.filter_by(public_id=search_data).first()

    else:
        raise Exception(
            '`get_by_attribute` data unexpected, you must send a valid value ')

    return author


def create_author(data):
    """ 
        Create a author by parameter data.

        Parameters
        ----------
        data : dict
            The data to create a entity. The dict must have this structure:
            {
                'name': 'the author name',
                'photo': 'url_photo' (optional)
            } 

        Raises
        ------
        Exception
            Not name in dict data
    """

    name = None
    photo = None

    if 'name' not in data:
        raise Exception('Not name in dict data')
    else:
        name = data['name']

    if 'photo' in data:
        photo = data['photo']

    new_author = Author(
        public_id=str(uuid.uuid4()),
        name=name,
        photo=photo,
        created_at=datetime.datetime.utcnow()
    )

    db.session.add(new_author)
    db.session.flush()

    return new_author
