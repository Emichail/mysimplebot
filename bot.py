import telebot
from telebot import types
import requests
from BeautifulSoup import BeautifulSoup as bs
from urllib2 import urlopen as open
import re



token ="166123695:AAG3-1LvkmzO3dntex3b22BMNBa2aKzJHYo"

if __name__ == "__main__":
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def send_start(message):
        bot.send_message(message.chat.id, "Hello, wolrd!")

    @bot.message_handler(commands=['help'])
    def send_help(message):
        output = []
        output.append("This is a simple bot.\n")
        output.append("/start - Hello,world\n")
        output.append("/help - All commands\n")
        output.append("/rfpl - Table of Russian Football Premier League\n");
        output.append("/bible - Get random verse from Bible\n")
        bot.send_message(message.chat.id, "".join(output))

    @bot.message_handler(commands=['rfpl'])
    def send_football(message):
        pattern = r"(?<=\>).+?(?=\<)"
        url = bs(open('http://eng.rfpl.org').read())
        out = []
        for i in range(1,17):
            footballTeam = str(re.findall(pattern, str(url('table')[7].findAll('tr')[i].findAll('td')[2].findAll('a'))))[2:-2]
            currentPoints=str(re.findall(pattern, str(url('table')[7].findAll('tr')[i].findAll('td')[8])))[2:-2]
            out.append('\n'+ footballTeam + (20-len(footballTeam))*' ' + currentPoints )
        bot.send_message(message.chat.id, " ".join(out))

    @bot.message_handler(commands=['bible'])
    def send_random_verse_from_bible(message):
        pattern = r"(?<=\>).+?(?=\<)"
        adress = 'http://www.sandersweb.net/bible/verse.php'
        res=[]
        url = bs(open(adress).read())
        output = re.findall(pattern, str(url('div')[0]))
        for i in output:
            if i[0] is not '<':
                res.append(i)
                res.append('\n')
        bot.send_message(message.chat.id, ' '.join(res))

    bot.polling(none_stop=True)
