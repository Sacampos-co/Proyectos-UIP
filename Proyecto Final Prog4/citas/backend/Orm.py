
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Column, String, Table
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Appointment (Base, SerializerMixin):
    __tablename__ = "appointmentTable"
    name = Column(String, primary_key=True)
    phone = Column(String)
    email = Column(String)
    location = Column(String)
    symptom = Column(String)
    date = Column(String)
    time = Column(String)

    def __init__(self, name, phone, email, location, symptom, date, time):
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location
        self.symptom = symptom
        self.date = date
        self.time = time


def createTable(engine):
    meta = MetaData()
    mydb = Table(
    'appointmentTable',meta,
        Column('name',String(1000),primary_key=True),
        Column('phone',String(1000)),
        Column('email',String(1000)),
        Column('location',String(1000)),
        Column('symptom',String(1000)),
        Column('date',String(1000)),
        Column('time',String(1000))
        )
    meta.create_all(engine)


class ORM():
    def __init__(self, nameTable, dialect):
        self.nameTable = nameTable+'.db'
        self.dialect = dialect+self.nameTable + '?check_same_thread=False'
        self.engine = create_engine(self.dialect)
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            createTable(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def addAppointment(self, name, phone, email, location, symptom, date , time):
        self.session.add(Appointment(name, phone, email, location, symptom, date, time))
        self.session.commit()

    def getAll(self):
        resultado = self.session.query(Appointment).all()
        return resultado

""" 
dialectoSQLITE = 'sqlite:///'
sql = ORM('appointmentTable', dialectoSQLITE)
sql.addAppointment('abc', '23434', 'mail@mail.com', "Las ads", "abc", "2021 - infity", "desde siempre")
data = sql.getAll()
print(data) """
