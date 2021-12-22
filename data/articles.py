import sqlalchemy as sa
from .db_session import SqlAlchemyBase
from datetime import utcnow


class Article(SqlAlchemyBase):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(100), nullable=False)
    intro = sa.Column(sa.String(300), nullable=False)
    text = sa.Column(sa.Text, nullable=False)
    date = sa.Column(sa.DateTime, default=utcnow)

    def __repr__ (self):
        return '<Article %r>' % self.id