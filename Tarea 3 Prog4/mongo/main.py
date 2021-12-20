
from pymongo import MongoClient

class MONGO():
    def __init__(self,nombreDB,host,port=None,user=None,password=None):
        if(user != None and user != ''):
            self.mongoUser = MongoClient(host,int(port),user,password)
        else:
            self.mongoUser = MongoClient(host,int(port))
        self.db = self.mongoUser[nombreDB]
        self.database = self.db.myTableName

    def addWord(self,word,definicion):
        data = {'word':word,'definicion':definicion}
        self.database.insert_one(data)

    def editarDefinicion(self,word,newDefinicion):
        data = {'word':word}
        newData = {'definicion':newDefinicion}
        self.database.update_one(data,{"$set":newData})

    def getAll(self):
        resultado = self.database.find()
        print('Lista de palabras')
        for informacion in resultado:
            print(informacion['word']+'\n')

    def deleteWord(self,word):
        data = {'word':word}
        self.database.delete_many(data)    

    def getWord(self,word):
        data = {'word':word}
        resultado = self.database.find_one(data)
        print('word:'+resultado['word']+' definicion:'+resultado['definicion'])
    

    
    def updateWord(self,word,newPalabra):
        data = {'word':word}
        newData = {'word':newPalabra}
        self.database.update_one(data,{"$set":newData})




db = MONGO('myTableName','localhost',27017,'')
#db.addWord('myPalabra','myDefinicion')
#db.updateWord('myPalabra','newPalabra')
#db.updateDefinition('myPalabra','newDefinicion')
#db.getWord('myPalabra')
#db.getAll()
#db.deeletWord('myPalabra')
