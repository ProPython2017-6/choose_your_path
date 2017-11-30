import YandexAPI_func as Yf
import class_Tbot
from telepot.namedtuple import ReplyKeyboardMarkup

token = '445749185:AAF6L-XwZsyLtcav--h-VPs0scjo-pJ59n0'
send_hi = 'Здравствуйте, {}! Желаете куда-то отправиться?'

Bot = class_Tbot.TelegramBot(token)

def write_last_update_id():
    print('write_last_update_id')
    print('Сообщение = ', Bot.message)
    Bot.last_update_id = Bot.update_id
    with open('last_update_id.txt', 'w') as f:
        f.write(str(Bot.last_update_id))

def space_in_plus(message):
    print('space_in_plus')
    categories = []
    rows = message.splitlines()
    for row in rows:
        if row:
            [categories.append('+'.join(item.split())) for item in row.split(',') if item]
    print(categories)
    return '+'.join(categories)

def yes_or_no(message):
    print('yes_or_no')
    if 'да' in str.lower(message):
        return True
    return False

def switch_case(func_name, message, add=None):
    print('switch')
    return {
        'yes_or_no': yes_or_no(message)
    }.get(func_name)

def while_if(func_name=None, add=None):
    print('while_if')
    while True:
        Bot.update()
        if Bot.update_id != Bot.last_update_id:
            if func_name is not None:
                result_func = switch_case(func_name, Bot.message, add)
                write_last_update_id()
                print(result_func)
                return result_func
            else:
                write_last_update_id()
                return Bot.message

def keyboard(geo):
    print('keyboard')
    i = 0
    text = []
    for key in geo:
        text.append(key)
        i += 1
    markup = ReplyKeyboardMarkup(keyboard=[
        [dict(text=text[j])] for j in range(i)
    ])
    Bot.TBot.sendMessage(Bot.chat_id, 'Пожалуйста, уточните местоположение...', reply_markup=markup)
    return geo.get(while_if())[1]

def send_info_button(rail):
    print('keyboard')
    text = []
    markup = ReplyKeyboardMarkup(keyboard=[
        [dict(text=rail[j])] for j in range(len(rail))
    ])
    Bot.TBot.sendMessage(Bot.chat_id, 'чем воспользуешься?', reply_markup=markup)
    return while_if()

def get_coordinate(obj):
    print('getCoordinate')
    #if type(obj) == type(dict()):
    if len(obj.keys()) > 1:
        return keyboard(obj)
    for k in obj:
        return obj.get(k)[1]

def work_dialog(from_point):
    work_message = ('Напишите ваш пункт отправления.', 'Напишите ваш пункт прибытия.')
    print('work_dialog')
    if from_point is None:
        if while_if('yes_or_no'):
            Bot.TBot.sendMessage(Bot.chat_id, work_message[0])
            from_point = get_coordinate(Yf.getPoint(space_in_plus(while_if())))
            print('from point = ', from_point)
            work_dialog(from_point)
        else:
            Bot.TBot.sendMessage(Bot.chat_id, 'Напишите, как будете готовы...')
    elif from_point:
        Bot.TBot.sendMessage(Bot.chat_id, work_message[1])
        to_point = get_coordinate(Yf.getPoint(space_in_plus(while_if())))

        depart = Yf.get_code_country(from_point)
        arrive = Yf.get_code_country(to_point)
        send_info_button(Yf.get_info_station(depart, arrive))


        '''from_station = Yf.search_nearest_station(from_point)
        to_station = Yf.search_nearest_station(to_point)
        Yf.create_route(from_station, to_station)'''


def main():
    while True:
        while_if()
        if Bot.message is '':
            continue
        Bot.TBot.sendMessage(Bot.chat_id, send_hi.format(Bot.user_name))
        work_dialog(None)
        print(Bot.TBot.getChat(Bot.chat_id))


if __name__ == '__main__':
    main()



