from .. import db, flask_bcrypt


class Token(db.Model):

    __tablename__ = "Token"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(255), unique=True, nullable=False)
    user = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    expire_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Token '{}'>".format(self.token)
