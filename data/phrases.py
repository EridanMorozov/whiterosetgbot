import sqlalchemy
from . import db_session


class Phrase(db_session.SqlAlchemyBase):
    __tablename__ = 'phrases'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String)
    translate_content = sqlalchemy.Column(sqlalchemy.String)

    def add_phrase(self, content, trans_content):
        db_session.global_init("db/blogs.db")
        session = db_session.create_session()
        ph = Phrase()
        ph.content = content
        ph.translate_content = trans_content
        session.add(ph)
        session.commit()
