from .. import db, flask_bcrypt


class Author(db.Model):

    __tablename__ = "Author"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(2048), unique=False)
    created_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return "<Author '{}'>".format(self.name)
