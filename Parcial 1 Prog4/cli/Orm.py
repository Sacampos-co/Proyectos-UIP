
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Column, String, Table
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Inventario (Base, SerializerMixin):
    __tablename__ = "InventarioTabla"
    nombre = Column(String, primary_key=True)
    precio = Column(String)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


def createTable(engine):
    meta = MetaData()
    mydb = Table(
    'InventarioTabla',meta,
        Column('nombre',String(1000),primary_key=True),
        Column('precio',String(1000)),
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

    def editarItem(self,nombre, precio):
        resultado = self.session.query(Inventario).filter(Inventario.nombre == nombre).one()
        resultado.nombre = nombre
        resultado.precio = precio
        self.session.add(resultado)
        self.session.commit()

    def borrarItem(self,nombre):
        resultado = self.session.query(Inventario).filter(Inventario.nombre == nombre).one()
        self.session.delete(resultado)
        self.session.commit()

    def addItem(self, nombre, precio):
        self.session.add(Inventario(nombre, precio))
        self.session.commit()

    def getAll(self):
        resultado = self.session.query(Inventario).all()
        return resultado

""" 
dialectoSQLITE = 'sqlite:///'
sql = ORM('InventarioTabla', dialectoSQLITE)
sql.addAppointment('abc', '23434', 'mail@mail.com', "Las ads", "abc", "2021 - infity", "desde siempre")
data = sql.getAll()
print(data) """
