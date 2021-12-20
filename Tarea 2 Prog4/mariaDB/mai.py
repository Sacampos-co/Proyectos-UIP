from sqlalchemy import create_engine, MetaData, Column, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class WordModel (Base):
    __tablename__ = "myTableName"
    palabra = Column(String, primary_key=True)
    definicion = Column(String)

    def __init__(self, palabra, definicion):
        self.palabra = palabra
        self.definicion = definicion


def createTable(engine):
    meta = MetaData()
    mydb = Table(
        'myTableName', meta,
        Column('palabra', String(1000), primary_key=True),
        Column('definicion', String(1000)))
    meta.create_all(engine)


class ORM():

    def __init__(self, nameTable, dialect):
        self.nameTable = nameTable+'.db'
        self.dialect = dialect+self.nameTable
        self.engine = create_engine(self.dialect)

        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            createTable(self.engine)

        self.session = sessionmaker(bind=self.engine)()

    def getWord(self, palabra):
        resultado = self.session.query(WordModel).filter(
            WordModel.palabra == palabra).one()
        print('Palabra:'+resultado.palabra+' Definicion:'+resultado.definicion)

    def addWord(self, palabra, definicion):
        self.session.add(WordModel(palabra, definicion))
        self.session.commit()

    def updateWord(self, palabra, newPalabra):
        resultado = self.session.query(WordModel).filter(
            WordModel.palabra == palabra).one()
        resultado.palabra = newPalabra
        self.session.add(resultado)
        self.session.commit()

    def deleteWord(self, palabra):
        resultado = self.session.query(WordModel).filter(
            WordModel.palabra == palabra).one()
        self.session.delete(resultado)
        self.session.commit()

    def getAll(self):
        resultado = self.session.query(WordModel).all()
        for informacion in resultado:
            print('Palabra:'+informacion.palabra +
                  ' Definicion:'+informacion.definicion+'\n')

    def updateDefinition(self, palabra, definicion):
        resultado = self.session.query(WordModel).filter(
            WordModel.palabra == palabra).one()
        resultado.definicion = definicion
        self.session.add(resultado)
        self.session.commit()


dialectoMARIADB = 'mysql+pymysql://myUserName:mypass@localhost/'
dialectoSQLITE = 'sqlite:///'
#sql = ORM('MyTableName',dialectoSQLITE)
# DIALECTO PARA MARIADB
sql = ORM('MyTableName', dialectoMARIADB)
# sql.getAll()
# sql.updateWord('xx','xxx')
# sql.updateDefinition('xx','xx')
# sql.deleteWord('xx')
# sql.addWord('xx','xx')
