import sqlalchemy
from .db_session import SqlAlchemyBase


class Phrase(SqlAlchemyBase):
    __tablename__ = 'phrases'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String)