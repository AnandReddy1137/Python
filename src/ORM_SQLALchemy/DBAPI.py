#################################################################################################
#                https://docs.sqlalchemy.org/en/14/core/engines.html
#                            @author : Anand kakaraddi
#                               SQLAlchemy Tutorial
#
##################################################################################################

import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql
from sqlalchemy import func
from datetime import datetime

'''
#psycopg2 way of connectivity
Connection = psycopg2.connect(
    host="10.75.153.103",
    database="Student",
    user="postgres", 
    password="postgres")
cursor = Connection.cursor()

cursor.execute("select * from STUDENTS")

stu_name=cursor.fetchone()[1]
print(stu_name)
cursor.close()
Connection.commit() '''

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)

    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>" \
            .format(self.title, self.author, self.pages, self.published)


DATABASE_URI = 'postgresql://postgres:postgres@10.75.153.103:5432/Student'

engine = create_engine(DATABASE_URI,echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Adding a Row
# b1 =Book(title='HARRY POTTER',author='J K ROWLING',pages=4000,published=datetime.now())
# session.add(b1)
# session.commit()
#
# more_books = [Book(title='BOOK1',author='author1',pages=4000,),
#               Book(title='BOOK2',author='author2',pages=4000),
#               Book(title='BOOK3',author='author3',pages=4000),
#               Book(title='BOOK14',author='author4',pages=4000)]
# #Adding multiple Rows
# session.add_all(more_books)
# session.commit()

#Reading the Rows
cs=session.query(Book).filter(Book.author=='author1').all()
print(cs)

#Learn about session.dirty porperty

#session.bulk_insert_mappings(Object,Insert_records_List)

#Aggregate Func
#session.query(Book.author,func.count())
