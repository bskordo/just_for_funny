import telebot
from jinja2 import Template
#from os import getenv
#from models import session, Pizza
#from catalog import catalog
#from sqlalchemy.orm import joinedload


'''TOKEN = os.environ['690553045:AAHrrHFYIZRF6IJPskpMh0w8CsmtMOcJpB0']
if not TOKEN:
    raise Exception('BOT_TOKEN should be specified')'''

bot = telebot.TeleBot("690553045:AAHrrHFYIZRF6IJPskpMh0w8CsmtMOcJpB0")

with open('templates/catalog.md', 'r') as catalog_file:
    catalog_tmpl = Template(catalog_file.read())

with open('templates/greetings.md', 'r') as greetings_file:
    greetings_tmpl = Template(greetings_file.read())

with open('templates/pohvali_chiku.md', 'r') as greetings_file:
    pohvali_chiku_tmpl = Template(greetings_file.read())

with open('templates/porugai_chiku.md', 'r') as greetings_file:
    porugai_chiku_tmpl = Template(greetings_file.read())

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, greetings_tmpl.render())

strings = {
    "ru": {
        "ro_msg": "Вам запрещено отправлять сюда сообщения в течение 10 минут."
    },
    "en": {
        "ro_msg": "You're not allowed to send messages here for 10 minutes."
    }
}
GROUP_ID = -1001224868730
restricted_messages = ["лаза", "i am vegan"]

@bot.message_handler(func=lambda message: message.text and message.text.lower() in restricted_messages and message.chat.id == GROUP_ID)
def set_ro(message):
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time()+600)
    bot.send_message(message.chat.id, strings.get(get_language(message.from_user.language_code)).get("ro_msg"),
                     reply_to_message_id=message.message_id)


@bot.message_handler(commands=['pohvali_chiku'])
def pohvali_chiku(message):
    bot.send_message(message.chat.id, pohvali_chiku_tmpl.render())

@bot.message_handler(commands=['porugai_chiku'])
def porugai_chiku(message):
    bot.send_message(message.chat.id, porugai_chiku_tmpl.render())

if __name__ == '__main__':
    bot.polling(none_stop=True)
