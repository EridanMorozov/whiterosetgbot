import sqlalchemy
from . import db_session
# A1 - начальный
# A2 - ниже среднего
# B1 - средний
# B2 - выше среднего
# C1 - продвинутый
# C2 - профессиональный


class Education(db_session.SqlAlchemyBase):
    __tablename__ = 'education'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    lvl = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.String)
    translate_content = sqlalchemy.Column(sqlalchemy.String)
    theme = sqlalchemy.Column(sqlalchemy.String)

    def add_ed(self, lvl, content, trans_content, theme):
        ed = Education()
        ed.lvl = lvl
        ed.content = content
        ed.translate_content = trans_content
        ed.theme = theme
        session.add(ed)
        session.commit()


# db_session.global_init("db/blogs.db")
# session = db_session.create_session()
# ed = Education()
# ed.add_ed('A1', 'World', 'Мир', 'The world around us')
# ed.add_ed('A1', 'Wind', 'Ветер', 'The world around us')
# ed.add_ed('A1', 'East', 'Восток', 'The world around us')
# ed.add_ed('A1', 'West', 'Запад', 'The world around us')
# ed.add_ed('A1', 'North', 'Север', 'The world around us')
# ed.add_ed('A1', 'South', 'Юг', 'The world around us')

