from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import random
app = Flask(__name__)

line_bot_api = LineBotApi('qsMozZovl2N0OYXCQ0awzX/WCrtWj0cAAsEuqt6bgjncKzf+G+H0Av5rG4k5aDuVsfrPX2TJQbWprk4iLQyoSkCkEjDkh5pOFk+IKtqLeeRqjVujLT3utyhCAXvSwnquJcI7Tbo9w13EFNOtC2QxGwdB04t89/1O/w1cDnyilFU=')
line_handler = WebhookHandler('5caa71b4621a20ec79f4394ccbb721f7')

@app.route('/')
def home():
    return 'Hello World'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


def myG():
    myW=['你好','吃飽了嗎','天氣如何']
    return random.choice(myW)

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text        

    if getA =='0' :        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(myG())))
   
    elif event.message.text == '2':        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='こんにちは'))

    elif event.message.text == '3':        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='안녕하세요'))
    
    elif event.message.text == '4':        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='สวัสดี'))
    
    elif event.message.text == '5':        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='ສະບາຍດີ'))

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="輸入0"))

if __name__ == "__main__":
    app.run()