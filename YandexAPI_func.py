import requests as req
import datetime
import re

YaKEY1 = '8b30fb55-7ed3-4576-aef5-8e39c7cb2834'
YaKEY = 'dc9e1723-7c70-4285-885c-eb0cdd663f8f'
URL = 'https://api.rasp.yandex.net/v3.0/'

def getPoint(address):
    print('getPoint')
    urlGEO = 'https://geocode-maps.yandex.ru/1.x/?geocode=' + address
    text = req.get(urlGEO).text
    geo_position = {}
    with open('geo.txt', 'w') as f:
        for s in text:
            f.write(s)
    i = 0
    with open('geo.txt', 'r') as f:
        for s in f:
            if 'text' in str(s):
                text = ' '.join(re.findall('[А-Яа-я,]+', str(s)))
                i += 1
            if 'name' in str(s):
                name = ' '.join(re.findall('[А-Яа-я,]+', str(s)))
                i += 1
            if "pos" in str(s):
                pos = re.findall('\d+\.\d{6}', str(s))
                geo_position.update({text: [pos, name]})
    if i is 1:
        return geo_position
    return geo_position

def search_nearest_station(coordinate):
    print('search_nearest_station')
    print('coordinate = ', coordinate)
    global URL
    url = URL + 'nearest_stations/?distance=5&station_types=train_station&lat={}&lng={}&apikey={}'.format(float(coordinate[1]), float(coordinate[0]), YaKEY)
    print(url)
    r = req.get(url)
    print(r.json())

def get_code_country(city):
    print('get_code_country', city)
    with open('station.txt', 'r') as f:
        for line in f:
            #print(str(re.findall('\040[А-Яа-я]+', line)))
            if '- '+city+' -' in line:
                print(re.findall('c[0-9]+', line)[0])
                return re.findall('c[0-9]+', line)[0]

def get_info_station(dep, arr):
    rail = []
    print(dep, arr)
    url = '''https://api.rasp.yandex.net/v3.0/search/?from={}&to={}&format=json&
    lang=ru_RU&apikey=dc9e1723-7c70-4285-885c-eb0cdd663f8f&date={}'''
    date = re.findall('\d{4}-\d{2}-\d{2}', str(datetime.datetime.now()))[0]
    data = req.get(url.format(dep, arr, date)).json()
    print(data)
    for k in range(len(data['segments'])):
        depart = data['segments'][k]['departure']
        arrive = data['segments'][k]['arrival']
        a = data['segments'][k]['from']['title']+' - '+data['segments'][k]['to']['title']+'\nВремя отправления:' +\
            depart[11:16]+'\nВремя прибытия:'+arrive[11:16]+'\n'
        rail.append(str(a))
        print(rail)
        return rail

def create_route(state_from, state_to):
    print('create_route')
    global URL
    url = URL + 'search/?from={}&to={}&apikey={}'.format(state_from, state_to, YaKEY)
    r = req.get(url)
    print(r.json())
