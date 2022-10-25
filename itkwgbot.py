import telebot
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="kwg_wifi"
)

print(mydb)

bot = telebot.TeleBot("5788661115:AAHvLegBaLmN4xVRnlA4-fm1HwCQAbNCN9w")
pic = "jadwal.jpg"
sql = mydb.cursor()

# Menghandle Pesan /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, """
    
    /JADWAL = UNTUK MELIHAT JADWAL IT

    /WIFI(SPASI)KODETOKO = UNTUK MELIHAT PASSWORD DAN NAMA WIFI YG ADA DI TOKO

    /SCANPDA = PANDUAN SETTING PDA

    /WIFIPDA = PANDUAN WIFI PDA

    /RESETSCAN = PANDUAN RESET SCANNER PDA

    /RESETPDA = PANDUAN RESET PDA

    /GLINET(SPASI)KODETOKO = UNTUK MELIHAT PASSWORD DAN NAMA GLINET YG ADA DI TOKO
    
    """)
@bot.message_handler(commands=['MENU'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, """
    
    /JADWAL = UNTUK MELIHAT JADWAL IT

    /WIFI(SPASI)KODETOKO = UNTUK MELIHAT PASSWORD DAN NAMA WIFI YG ADA DI TOKO

    /SCANPDA = PANDUAN SETTING PDA

    /WIFIPDA = PANDUAN WIFI PDA

    /RESETSCAN = PANDUAN RESET SCANNER PDA

    /RESETPDA = PANDUAN RESET PDA

    /GLINET(SPASI)KODETOKO = UNTUK MELIHAT PASSWORD DAN NAMA GLINET YG ADA DI TOKO
    
    """)

@bot.message_handler(commands=['JADWAL'])
def text(message):
    # membalas pesan
    chatid = message.chat.id
    bot.send_photo(chatid, open("jadwal.jpg","rb"))

@bot.message_handler(commands=['WIFIPDA'])
def text(message):
    # membalas pesan
    chatid = message.chat.id
    bot.send_document(chatid, open("SETTING_WIFI_PDA.pdf","rb"))

@bot.message_handler(commands=['SCANPDA'])
def text(message):
    # membalas pesan
    chatid = message.chat.id
    bot.send_document(chatid, open("SETTING_SCANNER_PDA.pdf","rb"))

@bot.message_handler(commands=['RESETSCAN'])
def text(message):
    # membalas pesan
    chatid = message.chat.id
    bot.send_document(chatid, open("RESET_SCANNER_PDA.pdf","rb"))

@bot.message_handler(commands=['WIFI'])
def text(message):
    #text split
    texts = message.text.split(' ') 
    #ambil parameter kdtoko
    kode_toko = texts[1]
    #sql nya
    sql.execute("select NAMA_WIFI from data_wifi where kode_toko='{}'".format(kode_toko))
    namawifi = sql.fetchall()

    pesan_nmwifi = 'NAMA_WIFI : '
    for x in namawifi:
        pesan_nmwifi = pesan_nmwifi + str(x) + '\n'
    
    sql.execute("select PASS_WIFI from data_wifi where kode_toko='{}'".format(kode_toko))
    passwifi = sql.fetchall()

    pesan_passwifi = 'PASSWORD WIFI : '
    for y in passwifi:
        pesan_passwifi = pesan_passwifi + str(y) + '\n'

    pesan_nmwifi = pesan_nmwifi.replace ("'","")
    pesan_nmwifi = pesan_nmwifi.replace (",","")
    pesan_passwifi = pesan_passwifi.replace ("'","")
    pesan_passwifi = pesan_passwifi.replace (",","")
  
    bot.reply_to(message, pesan_nmwifi)
    bot.reply_to(message, pesan_passwifi)

@bot.message_handler(commands=['GLINET'])
def text(message):
    #text split
    texts = message.text.split(' ') 
    #ambil parameter kdtoko
    kode_toko = texts[1]
    #sql nya
    sql.execute("select GLINET from data_wifi where kode_toko='{}'".format(kode_toko))
    glinet = sql.fetchall()

    pesan_glinet = 'SSID_GLINET : '
    for a in glinet:
        pesan_glinet = pesan_glinet + str(a) + '\n'
    
    sql.execute("select PASS_GLINET from data_wifi where kode_toko='{}'".format(kode_toko))
    passglinet = sql.fetchall()

    pesan_passglinet = 'PASSWORD GLINET : '
    for b in passglinet:
        pesan_passglinet = pesan_passglinet + str(b) + '\n'
    
    pesan_glinet = pesan_glinet.replace ("'","")
    pesan_glinet = pesan_glinet.replace (",","")
    pesan_passglinet = pesan_passglinet.replace ("'","")
    pesan_passglinet = pesan_passglinet.replace (",","")

  
    bot.reply_to(message, pesan_glinet)
    bot.reply_to(message, pesan_passglinet)

print("bot is running")
while True:
    try:
        bot.polling()
    except:
        pass