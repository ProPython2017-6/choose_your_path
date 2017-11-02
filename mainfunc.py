import requests as req
import setbot

URL='https://api.telegram.org/bot' + setbot.bot_test + '/'
last_update_id = None

def get_update():
    url = URL + 'getupdates'
    r = req.get(url)
    return r.json()

def get_message():
    data = get_update()
    if data['result'] == []:
        while data['result'] == []:
            data = get_update()
    last_update = data['result'][-1]
    update_id = last_update['update_id']
    global last_update_id
    if last_update_id != update_id:
        last_update_id = update_id
        chat_id = last_update['message']['chat']['id']
        text = last_update['message']['text']
        message = {'chat_id': chat_id, 'text': text}
        return message
    return None

def prov_address(address):
    pass


def send_message(id, text='Мая твоя не панимать...((('):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(id, text)
    req.get(url)


def send_img(id, img):
    url = URL + 'sendPhoto?chat_id={}&photo={}'.format(id, img)
    req.get(url)


def inDict():
    pass

def addDict(key, text):
    print('Ключ - ', key)
    print('Записываю новый диалог...')
    with open('big_dict.txt', 'a') as file:
        print('key=', key)
        print('text=', text)
        file.write('{}:{}\n'.format(key, text))
    send_message(id, 'Добавлено. Продолжение диалога...')

def switch_case(funcname, dopPars = None, updateText = None):
    return {
    'addDict': addDict(dopPars, updateText),
    'prov_address': prov_address(updateText)
    }.get(funcname)

def gt(funcname, dopPars = None):
    while True:
        infMessage = get_message()
        if infMessage is not None:
            switch_case(funcname, dopPars, infMessage['text'])
            break
