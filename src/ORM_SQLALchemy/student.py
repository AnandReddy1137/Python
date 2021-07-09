from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import cx_Oracle

CON_DIR = 'C:\\Users\\akakarad\\PycharmProjects\\Profiling\\Connection_list\\'
cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_19_11",
                             config_dir=r"C:\Oracle\Config")

e = create_engine(
    "oracle+cx_oracle://c03090595:c03090595@inglxora12.world", coerce_to_unicode=False)

Session = sessionmaker(bind=e)
session = Session()

Base = declarative_base()


class Student(Base):
    __table__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


Base.metadata.create_all(e)
