import mainfunc as f
import YandexAPI_func as Yf

big_dict = open('big_dict.txt', 'r')


hi = ['Здаров', 'Привет', 'Здорова', 'Здарова',
      'Hi', 'Hello', 'Хай', 'Дратути',
      'Дратутай', '\start', 'Здравствуй',
      'Здравствуйте', 'Здорово']
yes = ['да', 'Да', 'Yes', 'yes']

def main():
    while True:
        infMessage = f.get_message()
        if infMessage is not None:
            id = infMessage['chat_id']
            text = infMessage['text']
            if text in hi:
                f.send_message(id, Yf.send_hi)
                f.gt('prov_address')
            else:
                f.send_message(id, 'К сожалению я вас не понимаю...')




print('start')

main()


'''elif
                for line in big_dict:
                    if text in line:
                        send_mes=line.split(':')[1]
                        f.send_message(id, send_mes)'''