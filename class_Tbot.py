import telepot
class TelegramBot:
    def __init__(self, token):
        self.TBot = telepot.Bot(token)
        self.last_update_id = 0
        with open('last_update_id.txt', 'r') as f:
            for i in f:
                self.last_update_id = int(i)
        self.msg = None
        self.update_id = 0
        self.chat_id = 0
        self.from_id = 0
        self.user_name = ''
        self.message = ''
        self.TBot.getUpdates(self.last_update_id+1)

    def update(self):
        update_message = self.TBot.getUpdates()
        if len(update_message) != 0:
            self.update_id = update_message[-1]['update_id']
            update_message = update_message[-1]['message']
            self.chat_id = update_message['chat']['id']
            self.from_id = update_message['from']['id']
            self.user_name = update_message['from']['first_name']
            self.message = update_message['text']
