from .. import db, flask_bcrypt


class News(db.Model):

    __tablename__ = "News"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey(
        'Author.id'))
    public_id = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False, default=False)
    tag = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(2048), unique=False)
    created_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    author = db.relationship('Author', foreign_keys='Author.id',
                             lazy='joined', primaryjoin="Author.id == News.author_id")

    @db.validates('tag')
    def validate_tag(self, key, tag):
        valid_tags = ['POLITICS', 'SPORTS', 'TECH', 'SCIENCE', 'BUSINESS']

        assert tag is not None
        assert tag.upper() in valid_tags
        return tag.upper()

    def __repr__(self):
        return "<News '{}'>".format({self.id, self.title, self.author_id})
