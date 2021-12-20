from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy import String

engine = create_engine("sqlite:///db1.db")
session = sessionmaker(bind=engine)()
Base = declarative_base()

class User(Base):

    __tablename__ = "User"

    username = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

#user = User("Sergio", "some_password")
#user2 = User("Antonio","Another_password")
#session.add(user)
#session.add(user2)
#session.commit()

result = session.query(User).all()   
from pdb import set_trace; set_trace()

