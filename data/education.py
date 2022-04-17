import sqlalchemy
from .db_session import SqlAlchemyBase
# A1 - начальный
# A2 - ниже среднего
# B1 - средний
# B2 - выше среднего
# C1 - продвинутый
# C2 - профессиональный


class Education(SqlAlchemyBase):
    __tablename__ = 'education'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    lvl = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.String)
    translate_content = sqlalchemy.Column(sqlalchemy.String)
    photo = sqlalchemy.Column(sqlalchemy.String)