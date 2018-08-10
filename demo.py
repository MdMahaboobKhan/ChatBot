from flask import Flask,render_template, url_for, request, json
import time
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

app = Flask(__name__)

mybot = ChatBot('MyBot',storage_adapter="chatterbot.storage.SQLStorageAdapter")
mybot.set_trainer(ChatterBotCorpusTrainer)
#mybot.train("chatterbot.corpus.english")



#for files in os.listdir('C:/Users/z002z6ma\Downloads\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
#    data = open('C:/Users/z002z6ma\Downloads\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files).readlines()
#    mybot.train(data)
'''@app.route('/' , methods = ['GET', 'POST'])
def index():
    global messages_lst
    if request.method == "POST":
        msg = request.form['chat']
        you_str = 'You : '+ str(msg)
        messages_lst.append(you_str)
        if msg.strip() =='bye':
            result = 'bye bye'
            messages_lst = []
            print('Bot : ', result)
            messages = json.dumps(messages_lst)
            return render_template('x.html', messages = messages)
            #time.sleep(3000)
        else:
            #msg = request.form['chat']
            #print('you: '+ msg)
            #print('you: '+ msg)
            result = mybot.get_response(msg)
            #result = str(res)+'hello'
            #time.sleep(2)
            res_str = 'Chatbot : '+ str(result)
            print('Bot : ', result)
            messages_lst.append(res_str)
            messages = json.dumps(messages_lst)
            return render_template('x.html',messages = messages)
    else:
        return render_template('x.html')'''
@app.route("/")
def home():
    return render_template("x.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(mybot.get_response(userText))


if __name__ == "__main__":
	app.run(debug=True)


"""while True:
    msg = input('You: ')
    if msg.strip()=='Bye':
        print('chatbot: Bye')
        break
    else:
        reply = mybot.get_response(msg)
        print('chatbot:', reply)"""
