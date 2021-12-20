import redis

class REDIS():
    def __init__(self, host, port, db):
        self.host = host
        self.db = db
        self.redisdb = redis.Redis(host=self.host, port=self.port, db=self.db)
        self.port = port

    def updateWord(self, word, newPalabra):
        data = {'word': newPalabra}
        self.redisdb.hmset('Word:'+word, data)

    def getAll(self):
        res = self.redisdb.keys('Word:*')
        data = []
        for info in res:
            data.append(info.decode('utf-8'))
        result = []
        for info in data:
            result.append(self.getByKey(info))
        print(result)

    def updateDefiniton(self, word, definition):
        data = {'definition': definition}
        self.redisdb.hmset('Word:'+word, data)

    def deleteWord(self, word):
        self.redisdb.delete('Word:'+word)

    def addWord(self, word, definition):
        data = {'word': word, 'definition': definition}
        self.redisdb.hmset('Word:'+word, data)

    def getWord(self, word):
        resultado = self.redisdb.hgetall('Word:'+word)
        print(resultado)

    def getByKey(self, key):
        res = self.redisdb.hgetall(key)
        value = {}
        for k, v in res.items():
            value[k.decode('utf-8')] = v.decode('utf-8')
        res = value
        return res


RedisDB = REDIS('localhost', 6379, 0)
# RedisDB.addWord('xxx','xxx')
# RedisDB.updateDefiniton('xxx','xxx')
# RedisDB.getWord('xxx')
# RedisDB.getAll()
# RedisDB.deleteWord('xxx')
# RedisDB.updateWord('xxx','xxx')


