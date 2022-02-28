import telebot
import requests
import json
from urllib import request
from telebot import TeleBot,types

bot = telebot.TeleBot('5297547250:AAFvb8tirg-dLDEzOmVQcmF0hGtxxHQyBBs')

#beri pesan
@bot.message_handler(commands=['start'])
def start(message):
    #print(message)
    first_name = message.from_user.first_name
    text = (""" 
    Halo {}🙋🏻, perkenalkan aku ini bot. 
Kamu bisa mendapatkan info gempa bumi terkini menggunakan perintah /gempaterkini. Info 15 gempa bumi berkekuatan 5.0+ SR menggunakan perintah /datagempa. Info 15 gempa bumi yang dirasakan menggunakan perintah /gempaseluruh. Terima kasih, semoga bermanfaat.
Sumber : [BMKG](bmkg.go.id)""".format(first_name))
    bot.reply_to( message, text, parse_mode='markdown')


@bot.message_handler(commands=['gempaterkini'])
def gemp(message):
    api = requests.get('https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json')
    api_json = api.json()
    api_content = api_json
    for i in api_content:
        tgl = api_content['Infogempa']['gempa']['Tanggal']
        jam = api_content['Infogempa']['gempa']['Jam']
        mag = api_content['Infogempa']['gempa']['Magnitude']
        loc = api_content['Infogempa']['gempa']['Wilayah']
        dlm = api_content['Infogempa']['gempa']['Kedalaman']
        pot = api_content['Infogempa']['gempa']['Potensi']
        kirim = ('''
🌏*==Info Gempa Bumi Terkini==*🌏 
> Tanggal = {}
> Jam = {}
> Lokasi Gempa =  {}
> Kekuatan Gempa = {} SR
> Kedalaman Gempa = {}
> Potensi Gempa = {}
'''.format(tgl, jam, loc, mag, dlm, pot))
        bot.reply_to(message, kirim, parse_mode='markdown')

#info gempa berkekuatan 5.0+ SR
@bot.message_handler(commands=['datagempa'])
def gempa(message):
    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
    response = request.urlopen(url)
    data = json.loads(response.read())
    for d in data['Infogempa']['gempa']:
        tgl = f"{d['Tanggal']}"
        jam = f"{d['Jam']}"
        loc = f"{d['Wilayah']}"
        mag = f"{d['Magnitude']}"
        pot = f"{d['Potensi']}"
        kirim = ('''
🌏*==Data Gempa Bumi 5.0+ SR==*🌏
> Lokasi Gempa = {}
> Tanggal = {}
> Jam = {}
> Kekuatan Gempa = {} SR
> Potensi = {}
'''.format(loc, tgl, jam, mag, pot))
        bot.reply_to(message, kirim, parse_mode='markdown')

#info gempa bumi dirasakan
@bot.message_handler(commands=['gempaseluruh'])
def gempa(message):
    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json"    
    response = request.urlopen(url)
    data = json.loads(response.read())
    for e in data['Infogempa']['gempa']:
        tgl = f"{e['Tanggal']}"
        jam = f"{e['Jam']}"
        loc = f"{e['Wilayah']}"
        mag = f"{e['Magnitude']}"
        drs = f"{e['Dirasakan']}"
        kirim = ('''
        🌏*==Data Gempa Bumi yang Dirasakan==*🌏
> Lokasi Gempa = {}
> Tanggal = {}
> Jam = {}
> Kekuatan Gempa = {} SR
> Wilayah Jangkauan Gempa = {}
'''.format(loc, tgl, jam, mag, drs))
        bot.reply_to(message, kirim, parse_mode='markdown')

print("Bot is Running")
bot.polling()