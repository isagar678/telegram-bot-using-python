from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
from bs4 import BeautifulSoup
import requests
import json
import random
import re

Token = ''

with open('intents.json') as j :
        loader =json.load(j)


# load responses

def response_data(file):
    with open(file) as bot_response:
        return json.load(bot_response)
get_response_data = response_data("intentes1.json")


# response user


def resonder(input_data):
    input1 = re.findall(r"[\w']+", input_data.lower())
    for i in get_response_data["intents"]:
        flag =0
        for j in i["patterns"]:
            output = re.findall(r"[\w']+",j.lower())
            if input1==output:
                flag = flag+1
        if flag!=0:
            responses1 = i["responses"]
            return responses1[random.randrange(0,len(responses1))]
        
# shows heading of newsreport

def headliners(category):
    url =f"https://www.hindustantimes.com/{category}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        soup = BeautifulSoup(response.text,'html.parser')
        news_report = soup.find_all('h2')
        headings = ''
        for i in news_report:
            headings = headings +"--> "+i.get_text().strip()+'\n'+'\n'
        return headings
    return 'None'

# which enable when @img tag

def images(category):
    url = f'https://www.istockphoto.com/search/2/image-film?phrase={category}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    images1 = soup.find_all('img')
    list_img = list([])
    for img in images1:
        if img['src'].startswith('https'): 
            list_img.append(str(img['src']))
    print('hello')
    return list_img[random.randrange(0,len(list_img))]

# command line for coding starts with '/' 

async def start_command(update=Update,context=ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello ! Thanks for joining Here")

async def image_command(update=Update,context=ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("For images type '@img' also type category of image you want" )

async def newsreport(update=Update,context=ContextTypes.DEFAULT_TYPE):
    string1 = ''
    for i in loader['category']:
        string1= string1 + "->"+i+'\n'
    await update.message.reply_text(f"select news report you are intersted in \n {string1} \n tag me with '@news' while selecting the category")


# messaging in telegram


def Message_response(text) :
    textl = str(text.lower())
    return str(resonder(textl))

# handle message


async def handle_message(update=Update,context=ContextTypes.DEFAULT_TYPE):
    message_type = str(update.message.chat.type)
    text = str(update.message.text)

    print(f'Messaging {update.message.chat.id} {message_type}')
    print(filters.TEXT)

    bool = True
    
    if message_type == 'private':
        if '@news' in text:
            for i in loader['category']:
                if i in text :
                    response = str(headliners(i))
        elif '@img' in text:
            print(text)
            category = text.strip('@img ')
            response = images(category)
            print(response)
            bool = False

        else:
            response = str(Message_response(text))
        print(text)
        
    print('bot responding')
    if bool ==True:
        await update.message.reply_text(response)
    else :
        await update.message.reply_photo(response)


#  Error handler


async def error_handler(update=Update,context=ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cause error {context.error}')

# main tag 

print('starting')
app = Application.builder().token(Token).build()
app.add_handler(CommandHandler('start',start_command))
app.add_handler(CommandHandler('image',image_command))
app.add_handler(CommandHandler('news',newsreport))
app.add_handler(MessageHandler(filters.TEXT,handle_message))

app.add_error_handler(error_handler)

print('polling...')
app.run_polling(poll_interval=3)