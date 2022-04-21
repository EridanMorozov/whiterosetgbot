import sqlalchemy
from db_session import SqlAlchemyBase


class Theme(SqlAlchemyBase):
    __tablename__ = 'themes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    theme = sqlalchemy.Column(sqlalchemy.String)