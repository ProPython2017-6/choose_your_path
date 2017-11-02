YaKEY = '8b30fb55-7ed3-4576-aef5-8e39c7cb2834'
URL = 'https://api.rasp.yandex.net/v3.0/search/?'
send_hi = 'Здравствуйте! Напишите ваш запрос в формате [Пункт отправления] - [Конечный пункт]'

def send_yandex(state_from, state_to):
    global URL
    url = URL + 'from={}&to={}&apikey={}'.format(state_from, state_to, YaKEY)
    r = req.get(url)
    return r.json()