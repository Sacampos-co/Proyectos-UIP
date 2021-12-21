import requests
import ujson as json

peopleUrl = 'https://swapi.dev/api/people'
films = 'https://swapi.dev/api/films/'
planets = 'https://swapi.dev/api/planets/'
film6 = 'https://swapi.dev/api/films/6/'
starships = 'https://swapi.dev/api/starships/'


def all_resource_urls(query, values):
    ''' Get all the URLs for every resource '''
    urls = []
    next = True
    while next:
        response = requests.get(query)
        json_data = json.loads(response.content)
        for resource in json_data['results']:
            newValue = {}
            for value in values:
                newValue[value] = (resource[value])
                urls.append(newValue)
        if bool(json_data['next']):
            query = json_data['next']
        else:
            next = False
    return urls


def query(url, param={}, queryParams=''):
    headers = {'User-Agent': 'swapi-python'}
    response = requests.get(url+queryParams, params=param, headers=headers)
    if response.status_code != 200:
        print('Resource does not exist')
    return response.json()


def filter(data, on, filter, onList=False):
    if onList:
        return [x for x in data if filter[0] in x[on]]
    return [x for x in data if x[on] in filter]


def aridPlanets():
    getPlanets = filter(all_resource_urls(
        planets, ['name', 'climate', 'url', 'films']), 'climate', ['arid'])
    filmWithAridPlanet = []
    for planet in getPlanets:
        for film in planet['films']:
            if not film in filmWithAridPlanet:
                filmWithAridPlanet.append(film)
    return str(len(filmWithAridPlanet))


def wookiesInMovie6():
    wookie = 'https://swapi.dev/api/species/3/'
    wookies = filter(all_resource_urls(
        peopleUrl, ['name', 'species', 'url']), 'species', [wookie], True)
    movi = query(film6)
    wookiesInMovi = []
    for wookie in wookies:
        if wookie['url'] in movi['characters']:
            wookiesInMovi.append(wookie)
    return (str(len(wookiesInMovi)))


def getBigStartShip():
    starShips = all_resource_urls(starships, ['name', 'length'])
    bigStarShip = {'length': 0}
    for starShip in starShips:
        if float(str(starShip['length']).replace(",", ".")) > float(str(bigStarShip['length']).replace(",", ".")):
            bigStarShip = starShip
    return bigStarShip['name']


print('a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?: - ' + aridPlanets())
print('b) ¿Cuántos Wookies aparecen en la sexta película? - ' + wookiesInMovie6())
print('c) ¿Cuál es el nombre de la aeronave más grande en toda la saga? - ' +
      getBigStartShip())
