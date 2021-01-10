from datetime import datetime
from dateutil.relativedelta import relativedelta
import secrets

from app.main import db
from app.main.model.token import Token


def is_valid_token(auth_token):
    """ 
        Verify if token is valid.

        Parameters
        ----------
        data : string
            The token data

    """

    current_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    res = Token.query.filter(
        db.and_(Token.expire_at > current_date, Token.token == str(auth_token))).first()

    if res:
        return True
    else:
        return False


def generate_token(data):
    """ 
        Generate token.

        Parameters
        ----------
        data : dict
            The data to create generate a token. The dict must have this structure:
            {
                'user': 'the user name',
                'email': 'the user email'
            } 

        Raises
        ------
        Exception
            Not user or email in dict data
    """

    user = None
    email = None

    if 'user' not in data or 'email' not in data:
        raise Exception('user or email not in dict data')
    else:
        user = data['user']
        email = data['email']

    new_token = Token(
        token=secrets.token_urlsafe(20),
        user=user,
        email=email,
        created_at=datetime.utcnow(),
        expire_at=datetime.utcnow() + relativedelta(years=1))

    db.session.add(new_token)
    db.session.flush()

    result = {
        'token': new_token.token,
        'user': new_token.user,
        'email': new_token.email,
        'expire_at': new_token.expire_at
    }

    db.session.commit()

    return result
