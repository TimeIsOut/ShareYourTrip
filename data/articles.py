import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class Article(SqlAlchemyBase):
    __tablename__ = 'articles'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String(50), nullable=False)
    intro = sa.Column(sa.String(300), nullable=False)
    text = sa.Column(sa.Text, nullable=False)

    def __repr__ (self):
        return f'<Article {self.id}>'